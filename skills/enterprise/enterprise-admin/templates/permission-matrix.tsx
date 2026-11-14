// 权限矩阵：角色 × 资源 × 动作，行内开关，改动即生效前二次确认
// 依赖：react、shadcn/ui（Switch/Table/Select/AlertDialog）

import * as React from 'react'
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, AlertDialogHeader, AlertDialogTitle } from '@/components/ui/alert-dialog'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Switch } from '@/components/ui/switch'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'

// 动作固定六个，全站不要发明新动词
export const ACTIONS = ['read', 'create', 'update', 'delete', 'export', 'approve'] as const
export type Action = (typeof ACTIONS)[number]

export const ACTION_LABEL: Record<Action, string> = {
  read: '查看',
  create: '新建',
  update: '编辑',
  delete: '删除',
  export: '导出',
  approve: '审批',
}

export type Scope = 'own' | 'dept' | 'all'

export type Role = {
  key: string
  label: string
  userCount: number
}

export type Resource = {
  key: string
  label: string
  actions: Action[]
}

export type PermState = Record<string, Partial<Record<Action, boolean>>> // resource.key -> action -> allowed

const SCOPE_LABEL: Record<Scope, string> = {
  own: '仅本人',
  dept: '本部门',
  all: '全部',
}

export function PermissionMatrix({
  roles,
  resources,
  value,
  scope,
  onChange,
  onSave,
}: {
  roles: Role[]
  resources: Resource[]
  value: PermState
  scope: Scope
  onChange: (next: PermState) => void
  onSave: (payload: { role: string; perms: PermState; scope: Scope }) => void
}) {
  const [role, setRole] = React.useState(roles[0]?.key ?? '')
  const [pending, setPending] = React.useState<{ resource: Resource; action: Action; next: boolean } | null>(null)

  const currentRole = roles.find((r) => r.key === role)

  function toggle(resource: Resource, action: Action, next: boolean) {
    // 提升权限前确认，降权直接生效
    const was = value[resource.key]?.[action] ?? false
    if (next && !was) {
      setPending({ resource, action, next })
      return
    }
    commit(resource, action, next)
  }

  function commit(resource: Resource, action: Action, next: boolean) {
    onChange({ ...value, [resource.key]: { ...value[resource.key], [action]: next } })
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-3">
        <span className="text-sm text-muted-foreground">角色</span>
        <Select value={role} onValueChange={setRole}>
          <SelectTrigger className="w-48">
            <SelectValue />
          </SelectTrigger>
          <SelectContent>
            {roles.map((r) => (
              <SelectItem key={r.key} value={r.key}>
                {r.label}（{r.userCount} 人）
              </SelectItem>
            ))}
          </SelectContent>
        </Select>

        <span className="ml-4 text-sm text-muted-foreground">数据范围</span>
        <Select value={scope} onValueChange={(v) => onSave({ role, perms: value, scope: v as Scope })}>
          <SelectTrigger className="w-36">
            <SelectValue />
          </SelectTrigger>
          <SelectContent>
            {(Object.keys(SCOPE_LABEL) as Scope[]).map((s) => (
              <SelectItem key={s} value={s}>
                {SCOPE_LABEL[s]}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>

      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead className="w-48">资源</TableHead>
              {ACTIONS.map((a) => (
                <TableHead key={a} className="w-20 text-center">
                  {ACTION_LABEL[a]}
                </TableHead>
              ))}
            </TableRow>
          </TableHeader>
          <TableBody>
            {resources.map((r) => (
              <TableRow key={r.key}>
                <TableCell className="font-medium">{r.label}</TableCell>
                {ACTIONS.map((a) => {
                  const supported = r.actions.includes(a)
                  return (
                    <TableCell key={a} className="text-center">
                      <Switch
                        checked={!!value[r.key]?.[a]}
                        disabled={!supported}
                        onCheckedChange={(v) => toggle(r, a, v)}
                        aria-label={`${r.label} ${ACTION_LABEL[a]}`}
                      />
                    </TableCell>
                  )
                })}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>

      <p className="text-xs text-muted-foreground">
        功能权限管能不能做，数据范围管能看到谁的记录，两者独立。前端隐藏按钮只影响体验，接口必须校验同一张表。
      </p>

      <AlertDialog open={!!pending} onOpenChange={(o) => !o && setPending(null)}>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>确认授予权限</AlertDialogTitle>
            <AlertDialogDescription>
              将给角色 {currentRole?.label}（{currentRole?.userCount} 人）开放资源 {pending?.resource.label} 的
              {pending ? ACTION_LABEL[pending.action] : ''}权限。该角色下所有人立即生效。
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>取消</AlertDialogCancel>
            <AlertDialogAction
              onClick={() => {
                if (pending) {
                  commit(pending.resource, pending.action, pending.next)
                  onSave({ role, perms: value, scope })
                }
                setPending(null)
              }}
            >
              确认授予
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  )
}

// 三条约束：
// 1. 动作固定六个。新增动词会让后端权限表跟着分裂。
// 2. 提权确认、降权即时生效。反过来的话管理员会不敢点。
// 3. 保存要带角色、完整权限、数据范围三件套，局部保存会导致覆盖丢失。
