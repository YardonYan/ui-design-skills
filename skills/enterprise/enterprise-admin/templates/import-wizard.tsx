// 导入向导骨架：上传 → 字段映射 → 预检报告 → 结果回执
// 核心约束：第 3 步之前不写库。用户看到问题清单并确认后才入库。
// 依赖：react、lucide-react、shadcn/ui（Button/Alert/Table/Progress/Select）

import * as React from 'react'
import { AlertCircle, CheckCircle2, Download, FileSpreadsheet, Upload } from 'lucide-react'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { Button } from '@/components/ui/button'
import { Progress } from '@/components/ui/progress'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'

export type IssueLevel = 'block' | 'warn'

export type PrecheckIssue = {
  row: number
  column: string
  value: string
  level: IssueLevel
  message: string
}

export type PrecheckReport = {
  batchId: string
  total: number
  pass: number
  issues: PrecheckIssue[]
}

export type ImportResult = {
  batchId: string
  inserted: number
  failed: number
  elapsedMs: number
}

type Step = 'upload' | 'mapping' | 'precheck' | 'done'

const STEPS: { key: Step; label: string }[] = [
  { key: 'upload', label: '上传文件' },
  { key: 'mapping', label: '字段映射' },
  { key: 'precheck', label: '预检结果' },
  { key: 'done', label: '完成' },
]

// 系统字段与表格列名的对应关系由后端给出候选，不要在前端猜
export type ColumnMapping = { source: string; target: string | null }

export function ImportWizard({
  systemFields,
  onUpload,
  onPrecheck,
  onCommit,
}: {
  systemFields: { key: string; label: string; required: boolean }[]
  onUpload: (file: File) => Promise<{ columns: string[]; mapping: ColumnMapping[] }>
  onPrecheck: (payload: { file: File; mapping: ColumnMapping[] }) => Promise<PrecheckReport>
  onCommit: (report: PrecheckReport, skipInvalid: boolean) => Promise<ImportResult>
}) {
  const [step, setStep] = React.useState<Step>('upload')
  const [file, setFile] = React.useState<File | null>(null)
  const [mapping, setMapping] = React.useState<ColumnMapping[]>([])
  const [report, setReport] = React.useState<PrecheckReport | null>(null)
  const [result, setResult] = React.useState<ImportResult | null>(null)
  const [busy, setBusy] = React.useState(false)

  const stepIndex = STEPS.findIndex((s) => s.key === step)
  const blockCount = report?.issues.filter((i) => i.level === 'block').length ?? 0
  const warnCount = report?.issues.filter((i) => i.level === 'warn').length ?? 0

  async function handleFile(f: File) {
    setBusy(true)
    try {
      const res = await onUpload(f)
      setFile(f)
      setMapping(res.mapping)
      setStep('mapping')
    } finally {
      setBusy(false)
    }
  }

  async function handlePrecheck() {
    if (!file) return
    // 必填字段没映射上就不该继续，省得跑一趟后端
    const missing = systemFields.filter(
      (f) => f.required && !mapping.some((m) => m.target === f.key),
    )
    if (missing.length > 0) {
      alert(`以下必填字段还没有映射：${missing.map((m) => m.label).join('、')}`)
      return
    }
    setBusy(true)
    try {
      setReport(await onPrecheck({ file, mapping }))
      setStep('precheck')
    } finally {
      setBusy(false)
    }
  }

  async function handleCommit(skipInvalid: boolean) {
    if (!report) return
    setBusy(true)
    try {
      setResult(await onCommit(report, skipInvalid))
      setStep('done')
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="mx-auto w-full max-w-3xl space-y-6 p-6">
      {/* 步骤条：不可跳步，只能回退到已完成的步骤 */}
      <ol className="flex items-center gap-2 text-sm">
        {STEPS.map((s, i) => (
          <li key={s.key} className="flex items-center gap-2">
            <span
              className={
                i === stepIndex
                  ? 'flex size-6 items-center justify-center rounded-full bg-primary text-primary-foreground'
                  : i < stepIndex
                    ? 'flex size-6 items-center justify-center rounded-full bg-muted text-foreground'
                    : 'flex size-6 items-center justify-center rounded-full border text-muted-foreground'
              }
            >
              {i < stepIndex ? <CheckCircle2 className="size-4" /> : i + 1}
            </span>
            <span className={i === stepIndex ? 'font-medium' : 'text-muted-foreground'}>{s.label}</span>
            {i < STEPS.length - 1 && <span className="mx-1 h-px w-8 bg-border" />}
          </li>
        ))}
      </ol>

      {step === 'upload' && (
        <label className="flex cursor-pointer flex-col items-center gap-3 rounded-lg border border-dashed p-10 text-center hover:bg-muted/40">
          <FileSpreadsheet className="size-8 text-muted-foreground" />
          <div className="text-sm">
            拖入 .xlsx 或 .csv，或点击选择文件
            <div className="mt-1 text-xs text-muted-foreground">单次不超过 5000 行，超过请拆批</div>
          </div>
          <Button variant="outline" size="sm" type="button" disabled={busy}>
            <Upload className="mr-1 size-4" /> 选择文件
          </Button>
          <input
            type="file"
            accept=".xlsx,.xls,.csv"
            className="hidden"
            onChange={(e) => {
              const f = e.target.files?.[0]
              if (f) void handleFile(f)
            }}
          />
          {/* 模板下载：不给模板是最常见的失败原因 */}
          <a className="text-xs text-primary underline" href="/templates/import-template.xlsx" download>
            <Download className="mr-1 inline size-3" /> 下载导入模板
          </a>
        </label>
      )}

      {step === 'mapping' && (
        <div className="space-y-4">
          <p className="text-sm text-muted-foreground">
            共识别 {mapping.length} 列，请确认对应关系。可以不映射，未映射的列不入库。
          </p>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>表格列</TableHead>
                <TableHead>系统字段</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {mapping.map((m, idx) => (
                <TableRow key={m.source}>
                  <TableCell className="font-mono text-[13px]">{m.source}</TableCell>
                  <TableCell>
                    <Select
                      value={m.target ?? '__skip__'}
                      onValueChange={(v) =>
                        setMapping((prev) =>
                          prev.map((x, i) => (i === idx ? { ...x, target: v === '__skip__' ? null : v } : x)),
                        )
                      }
                    >
                      <SelectTrigger className="w-64">
                        <SelectValue placeholder="忽略此列" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="__skip__">忽略此列</SelectItem>
                        {systemFields.map((f) => (
                          <SelectItem key={f.key} value={f.key}>
                            {f.label}
                            {f.required ? ' *' : ''}
                          </SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
          <div className="flex justify-between">
            <Button variant="ghost" onClick={() => setStep('upload')}>
              上一步
            </Button>
            <Button onClick={handlePrecheck} disabled={busy}>
              {busy ? '校验中…' : '开始预检'}
            </Button>
          </div>
        </div>
      )}

      {step === 'precheck' && report && (
        <div className="space-y-4">
          <div className="grid grid-cols-3 gap-3">
            <Stat label="总行数" value={report.total} />
            <Stat label="可入库" value={report.pass} tone="ok" />
            <Stat label="有问题" value={report.issues.length} tone={blockCount > 0 ? 'bad' : 'warn'} />
          </div>

          {blockCount > 0 && (
            <Alert variant="destructive">
              <AlertCircle className="size-4" />
              <AlertTitle>{blockCount} 行存在阻断问题，必须修正后才能入库</AlertTitle>
              <AlertDescription className="text-xs">
                可以下载问题清单，改完重新上传；也可以忽略这些行，先入库其余 {report.pass} 行。
              </AlertDescription>
            </Alert>
          )}

          {warnCount > 0 && (
            <Alert>
              <AlertCircle className="size-4" />
              <AlertTitle>{warnCount} 行有警告，可选择忽略并继续</AlertTitle>
            </Alert>
          )}

          {/* 问题清单必须精确到行号与列名，只说条数等于没说 */}
          <div className="max-h-80 overflow-auto rounded-md border">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead className="w-16">行号</TableHead>
                  <TableHead className="w-28">列</TableHead>
                  <TableHead className="w-28">原值</TableHead>
                  <TableHead>原因</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {report.issues.map((i, idx) => (
                  <TableRow key={`${i.row}-${i.column}-${idx}`}>
                    <TableCell className="tabular-nums">{i.row}</TableCell>
                    <TableCell>{i.column}</TableCell>
                    <TableCell className="max-w-28 truncate font-mono text-xs">{i.value || '（空）'}</TableCell>
                    <TableCell className={i.level === 'block' ? 'text-destructive' : 'text-muted-foreground'}>
                      {i.message}
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>

          <div className="flex items-center justify-between">
            <Button variant="ghost" onClick={() => setStep('mapping')}>
              返回修改
            </Button>
            <div className="flex gap-2">
              <Button variant="outline" onClick={() => handleCommit(true)} disabled={busy || report.pass === 0}>
                忽略 {report.issues.length} 行，入库 {report.pass} 行
              </Button>
              <Button onClick={() => handleCommit(false)} disabled={busy || blockCount > 0}>
                全部入库
              </Button>
            </div>
          </div>
        </div>
      )}

      {step === 'done' && result && (
        <div className="space-y-4 rounded-lg border p-6 text-center">
          <CheckCircle2 className="mx-auto size-10 text-emerald-600" />
          <div className="text-lg font-medium">导入完成</div>
          <div className="text-sm text-muted-foreground">
            入库 {result.inserted} 条 · 失败 {result.failed} 条 · 耗时 {(result.elapsedMs / 1000).toFixed(1)} 秒
          </div>
          <div className="text-xs text-muted-foreground">批次号 {result.batchId}，可据此回溯</div>
          <Progress value={100} className="mx-auto max-w-xs" />
          <div className="flex justify-center gap-2">
            <Button variant="outline" onClick={() => location.assign(`/imports/${result.batchId}`)}>
              查看导入记录
            </Button>
            <Button
              onClick={() => {
                setStep('upload')
                setFile(null)
                setMapping([])
                setReport(null)
                setResult(null)
              }}
            >
              再导一批
            </Button>
          </div>
        </div>
      )}
    </div>
  )
}

function Stat({ label, value, tone }: { label: string; value: number; tone?: 'ok' | 'warn' | 'bad' }) {
  const color =
    tone === 'ok' ? 'text-emerald-600' : tone === 'bad' ? 'text-destructive' : tone === 'warn' ? 'text-amber-600' : ''
  return (
    <div className="rounded-lg border p-4">
      <div className="text-xs text-muted-foreground">{label}</div>
      <div className={`mt-1 text-2xl font-semibold tabular-nums ${color}`}>{value}</div>
    </div>
  )
}

// 四条不可省的实现约束：
// 1. 上传只解析列名，不入库。
// 2. 必填字段未映射时前置拦截，不要交给后端报错。
// 3. 预检报告要能下载，用户离线改。
// 4. 入库带批次号，全量事务或按行记录失败，不能静默丢数据。
