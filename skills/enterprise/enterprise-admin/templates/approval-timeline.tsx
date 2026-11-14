// 审批流时间轴：节点状态 + 处理人 + 时间 + 意见，当前节点只对处理人显示操作
// 依赖：react、lucide-react、shadcn/ui（Button/Textarea/AlertDialog/Avatar）

import * as React from 'react'
import { Check, Circle, Clock, X } from 'lucide-react'
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, AlertDialogHeader, AlertDialogTitle } from '@/components/ui/alert-dialog'
import { Avatar, AvatarFallback } from '@/components/ui/avatar'
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'

export type NodeState = 'done' | 'current' | 'waiting' | 'rejected' | 'skipped'

export type ApprovalNode = {
  key: string
  label: string
  state: NodeState
  approverName?: string
  handledAt?: string
  comment?: string
  // 会签：需要多人处理时才用到
  mode?: 'any' | 'all'
}

export function ApprovalTimeline({
  nodes,
  canAct,
  onApprove,
  onReject,
}: {
  nodes: ApprovalNode[]
  canAct: boolean
  onApprove: (comment: string) => Promise<void>
  onReject: (comment: string) => Promise<void>
}) {
  const [comment, setComment] = React.useState('')
  const [rejecting, setRejecting] = React.useState(false)
  const [busy, setBusy] = React.useState(false)
  const current = nodes.find((n) => n.state === 'current')

  return (
    <div className="space-y-1">
      {nodes.map((n, i) => (
        <div key={n.key} className="flex gap-3">
          {/* 左侧圆点与连线 */}
          <div className="flex flex-col items-center">
            <Dot state={n.state} />
            {i < nodes.length - 1 && (
              <span className={n.state === 'done' ? 'my-1 w-px flex-1 bg-foreground/20' : 'my-1 w-px flex-1 bg-border'} />
            )}
          </div>

          <div className="pb-5">
            <div className="flex flex-wrap items-center gap-2">
              <span className={n.state === 'current' ? 'text-sm font-medium' : 'text-sm'}>{n.label}</span>
              {n.mode === 'all' && <span className="text-xs text-muted-foreground">会签</span>}
              {n.state === 'current' && <span className="text-xs text-muted-foreground">处理中</span>}
              {n.state === 'skipped' && <span className="text-xs text-muted-foreground">已跳过</span>}
            </div>

            <div className="mt-1 flex items-center gap-2 text-xs text-muted-foreground">
              {n.approverName ? (
                <>
                  <Avatar className="size-4">
                    <AvatarFallback className="text-[10px]">{n.approverName.slice(0, 1)}</AvatarFallback>
                  </Avatar>
                  <span>{n.approverName}</span>
                </>
              ) : (
                <span>{n.state === 'waiting' ? '未开始' : '待指派'}</span>
              )}
              {n.handledAt && <span className="tabular-nums">{n.handledAt}</span>}
            </div>

            {n.comment && (
              <div className="mt-2 rounded-md bg-muted/60 px-3 py-2 text-xs leading-relaxed">{n.comment}</div>
            )}
          </div>
        </div>
      ))}

      {/* 操作区只对当前处理人显示，其他人看到的是等待提示 */}
      {canAct && current ? (
        <div className="space-y-2 rounded-lg border p-3">
          <div className="text-xs text-muted-foreground">当前节点：{current.label}</div>
          <Textarea
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            placeholder="填写审批意见（驳回时必填）"
            className="min-h-20 text-sm"
          />
          <div className="flex justify-end gap-2">
            <Button variant="outline" size="sm" onClick={() => setRejecting(true)} disabled={busy}>
              <X className="mr-1 size-4" /> 驳回
            </Button>
            <Button
              size="sm"
              disabled={busy}
              onClick={async () => {
                setBusy(true)
                try {
                  await onApprove(comment)
                  setComment('')
                } finally {
                  setBusy(false)
                }
              }}
            >
              <Check className="mr-1 size-4" /> 同意
            </Button>
          </div>
        </div>
      ) : (
        current && (
          <div className="flex items-center gap-2 rounded-lg bg-muted/50 px-3 py-2 text-xs text-muted-foreground">
            <Clock className="size-3.5" /> 等待 {current.approverName ?? '当前处理人'} 处理
          </div>
        )
      )}

      <AlertDialog open={rejecting} onOpenChange={setRejecting}>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>确认驳回</AlertDialogTitle>
            <AlertDialogDescription>
              将退回至发起人，已填写内容保留，需要修改后重新提交。驳回原因将记入审批记录。
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>取消</AlertDialogCancel>
            <AlertDialogAction
              disabled={!comment.trim()}
              onClick={async () => {
                setBusy(true)
                try {
                  await onReject(comment)
                  setComment('')
                  setRejecting(false)
                } finally {
                  setBusy(false)
                }
              }}
            >
              确认驳回
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  )
}

function Dot({ state }: { state: NodeState }) {
  const base = 'flex size-6 shrink-0 items-center justify-center rounded-full border'
  if (state === 'done') return <span className={`${base} border-foreground bg-foreground text-background`}><Check className="size-3.5" /></span>
  if (state === 'rejected') return <span className={`${base} border-destructive bg-destructive text-destructive-foreground`}><X className="size-3.5" /></span>
  if (state === 'current') return <span className={`${base} border-primary text-primary`}><Circle className="size-2.5 fill-current" /></span>
  return <span className={`${base} border-border text-muted-foreground`}><Circle className="size-2.5" /></span>
}

// 四条约束：
// 1. 节点顺序与跳过条件写在配置里，不散在代码 if。
// 2. 驳回必须填原因，且是退回而非作废。
// 3. 时间轴四要素齐全：节点、人、时间、意见。
// 4. 会签要显示本轮还需几人，否则处理人不知道要等谁。
