#!/usr/bin/env node
// Regenerate the observatory board dataset from this repository's skills and board/content copy.
// Usage: node tools/sync_board.mjs [--out <path>] [--site <site-project-dir>]
// With --site, also writes <site>/data/skills.json and checks demo coverage there.
import fs from 'node:fs';
import path from 'node:path';
import { execSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const argv = process.argv.slice(2);
const flag = (n) => { const i = argv.indexOf(n); return i >= 0 && argv[i + 1] ? path.resolve(argv[i + 1]) : null; };
const site = flag('--site');
const out = flag('--out') || path.join(repo, 'board', 'skills.json');

const base = [];
const skillsDir = path.join(repo, 'skills');
for (const cat of fs.readdirSync(skillsDir)) {
  const catDir = path.join(skillsDir, cat);
  if (!fs.statSync(catDir).isDirectory()) continue;
  for (const name of fs.readdirSync(catDir)) {
    const skillFile = path.join(catDir, name, 'SKILL.md');
    if (!fs.existsSync(skillFile)) continue;
    const text = fs.readFileSync(skillFile, 'utf8');
    const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
    const fm = {};
    if (m) {
      let key = null;
      for (const line of m[1].split(/\r?\n/)) {
        const kv = line.match(/^([a-zA-Z_-]+):\s*(.*)$/);
        if (kv) { key = kv[1]; fm[key] = kv[2].replace(/^["']|["']$/g, ''); }
        else if (key && /^\s+/.test(line)) fm[key] += ' ' + line.trim();
      }
    }
    base.push({ id: name, category: cat, path: `skills/${cat}/${name}`, name: fm.name || name, description: fm.description || '' });
  }
}

const content = new Map();
const contentDir = path.join(repo, 'board', 'content');
for (const f of fs.readdirSync(contentDir)) {
  if (!f.endsWith('.json')) continue;
  for (const e of JSON.parse(fs.readFileSync(path.join(contentDir, f), 'utf8'))) content.set(e.id, e);
}

function walk(dir) {
  let files = 0, bytes = 0;
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { const r = walk(p); files += r.files; bytes += r.bytes; }
    else { files++; bytes += fs.statSync(p).size; }
  }
  return { files, bytes };
}

const git = (cmd) => execSync(cmd, { cwd: repo, encoding: 'utf8' }).trim();
const fileCount = git('git ls-files').split('\n').length;
const commits = git('git log -8 --format="%cs|%s"').split('\n').map((l) => { const [d, ...s] = l.split('|'); return { d, s: s.join('|') }; });
const licenseRaw = fs.readFileSync(path.join(repo, 'LICENSE'), 'utf8').split(/\r?\n/).map((l) => l.trim()).find((l) => l) || '';
const license = /MIT/i.test(licenseRaw) ? 'MIT' : /Apache/i.test(licenseRaw) ? 'Apache-2.0' : licenseRaw.slice(0, 24);

const skills = [];
const missing = [];
let totalBytes = 0;
for (const b of base) {
  const st = walk(path.join(repo, b.path));
  totalBytes += st.bytes;
  const c = content.get(b.id);
  const hasDemo = site ? fs.existsSync(path.join(site, 'demos', `${b.id}.html`)) : true;
  if (!c || !hasDemo) missing.push(`${b.id}${!c ? ' [copy]' : ''}${!hasDemo ? ' [demo]' : ''}`);
  const zhDesc = c?.descZh || (/[一-鿿]/.test(b.description) ? b.description : '');
  const enDesc = c?.descEn || (!/[一-鿿]/.test(b.description) ? b.description : '');
  skills.push({
    id: b.id, category: b.category, path: b.path, name: b.name,
    nameZh: c?.nameZh || b.id, nameEn: c?.nameEn || b.name,
    taglineZh: c?.taglineZh || zhDesc.slice(0, 40), taglineEn: c?.taglineEn || enDesc.slice(0, 60),
    descZh: zhDesc, descEn: enDesc,
    keywords: c?.keywords || [b.category, b.id],
    keywordsEn: c?.keywordsEn || [],
    outputZh: c?.outputZh || '技能文档', outputEn: c?.outputEn || 'Skill docs',
    demoCaptionZh: c?.demoCaptionZh || '输出示例', demoCaptionEn: c?.demoCaptionEn || 'Sample output',
    files: st.files, bytesKB: Math.round(st.bytes / 1024),
    demo: hasDemo ? `demos/${b.id}.html` : null,
  });
}
const data = {
  repo: { name: 'ui-design-skills', url: 'https://github.com/YardonYan/ui-design-skills', branch: 'main', updated: commits[0].d, license, fileCount, skillCount: skills.length, bytesKB: Math.round(totalBytes / 1024), commits },
  skills,
};
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, JSON.stringify(data));
if (site) {
  fs.mkdirSync(path.join(site, 'data'), { recursive: true });
  fs.writeFileSync(path.join(site, 'data', 'skills.json'), JSON.stringify(data));
}
console.log('skills:', skills.length, 'repo files:', fileCount, 'KB:', data.repo.bytesKB, '->', out);
if (site) console.log('site data written:', path.join(site, 'data', 'skills.json'));
console.log('missing:', missing.length ? missing.join(', ') : 'none');