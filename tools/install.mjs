#!/usr/bin/env node
// Zero-dependency installer for UI Design Skills. Node 18+.
// Usage: node tools/install.mjs --list
//        node tools/install.mjs --skill saas-landing --ai workbuddy
//        node tools/install.mjs --skill all --ai all --dry-run
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const SKILLS = path.join(ROOT, "skills");
const HOME = os.homedir();
const TARGETS = {
  workbuddy:  path.join(HOME, ".workbuddy", "skills"),
  codebuddy:  path.join(HOME, ".codebuddy", "skills"),
  "trae-cn":  path.join(HOME, ".trae-cn", "skills"),
  qoder:      path.join(HOME, ".qoder", "skills"),
  "qwen-code":path.join(HOME, ".qwen", "skills"),
  openclaw:   path.join(HOME, ".openclaw", "skills"),
  claude:     path.join(HOME, ".claude", "skills"),
  codex:      path.join(HOME, ".codex", "skills"),
  cursor:     path.join(HOME, ".cursor", "skills"),
};

const argv = process.argv.slice(2);
function opt(name, fallback = null) {
  const i = argv.indexOf(name);
  return i >= 0 ? (argv[i + 1] && !argv[i + 1].startsWith("--") ? argv[i + 1] : true) : fallback;
}
const has = (f) => argv.includes(f);

function allSkills() {
  const out = [];
  for (const cat of fs.readdirSync(SKILLS, { withFileTypes: true })) {
    if (!cat.isDirectory()) continue;
    for (const d of fs.readdirSync(path.join(SKILLS, cat.name), { withFileTypes: true })) {
      if (d.isDirectory()) out.push({ cat: cat.name, name: d.name, src: path.join(SKILLS, cat.name, d.name) });
    }
  }
  return out.sort((a, b) => a.name.localeCompare(b.name));
}

function die(msg) { console.error("[错误] " + msg); process.exit(1); }
function copyDir(from, to) {
  fs.mkdirSync(to, { recursive: true });
  for (const e of fs.readdirSync(from, { withFileTypes: true })) {
    const s = path.join(from, e.name), t = path.join(to, e.name);
    if (e.isDirectory()) copyDir(s, t);
    else fs.copyFileSync(s, t);
  }
}

const skills = allSkills();
const q = opt("--search"), catFilter = opt("--category");
const matches = (s) =>
  (!q || q === true || s.name.includes(String(q))) &&
  (!catFilter || catFilter === true || s.cat === String(catFilter));

if (has("--list")) {
  const pool = skills.filter(matches);
  const byCat = {};
  for (const s of pool) (byCat[s.cat] ||= []).push(s.name);
  console.log(q || catFilter ? `匹配 ${pool.length} 个技能（共 ${skills.length} 个）` : `共 ${skills.length} 个技能`);
  for (const c of Object.keys(byCat).sort()) console.log(`  ${c} (${byCat[c].length}): ${byCat[c].join(", ")}`);
  if (!pool.length) console.log("  没有匹配项，用 --list 查看全部");
  process.exit(0);
}

const pick = opt("--skill");
if (!pick) die("需要 --skill <名> 或 --skill all，或用 --list 查看清单");
const selected = pick === "all"
  ? skills.filter(matches)
  : skills.filter((s) => s.name === pick);
if (!selected.length) die(`找不到技能 ${pick}，用 --list 查看全部`);

// Hard gate: refuse to install a half-broken skill.
for (const s of selected) {
  if (!fs.existsSync(path.join(s.src, "SKILL.md"))) die(`${s.cat}/${s.name} 根目录缺 SKILL.md，整体拒绝安装`);
}

const ai = opt("--ai");
const dirOverride = opt("--dir");
let targets = [];
if (dirOverride && dirOverride !== true) targets = [dirOverride];
else if (ai === "all") targets = Object.values(TARGETS);
else if (ai && ai !== true) {
  if (!TARGETS[ai]) die(`未知助手 ${ai}，可用：${Object.keys(TARGETS).join(", ")}`);
  targets = [TARGETS[ai]];
} else die("需要 --ai <id>、--ai all 或 --dir <路径>");
if (has("--project")) targets = targets.map((t) => path.join(process.cwd(), ".workbuddy", "skills"));

const dry = has("--dry-run"), force = has("--force"), remove = has("--uninstall");
let n = 0;
for (const base of targets) {
  for (const s of selected) {
    const dest = path.join(base, s.name);
    if (remove) {
      if (dry) { console.log(`[dry-run] 删除 ${dest}`); continue; }
      if (fs.existsSync(dest)) { fs.rmSync(dest, { recursive: true, force: true }); console.log(`删除 ${dest}`); n++; }
      continue;
    }
    if (fs.existsSync(dest) && !force) { console.log(`跳过 ${dest}（已存在，--force 覆盖）`); continue; }
    if (dry) { console.log(`[dry-run] ${s.src} -> ${dest}`); n++; continue; }
    if (fs.existsSync(dest)) fs.rmSync(dest, { recursive: true, force: true });
    copyDir(s.src, dest);
    console.log(`安装 ${s.name} -> ${dest}`);
    n++;
  }
}
console.log(`完成，处理 ${n} 项${dry ? "（dry-run，未写入）" : ""}`);
