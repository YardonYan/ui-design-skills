// 列表页列定义范式（TanStack Table + shadcn/ui）
// 依赖：@tanstack/react-table、shadcn-admin 的 DataTableColumnHeader
// 用法：列定义与表格分离，表格组件只负责渲染

import type { ColumnDef } from '@tanstack/react-table'
import { Badge } from '@/components/ui/badge'
import { Checkbox } from '@/components/ui/checkbox'
import { DataTableColumnHeader } from '@/components/data-table/column-header'
import { DataTableRowActions } from './row-actions'

export type Order = {
  id: string
  orderNo: string
  customerName: string
  status: 'draft' | 'pending' | 'approved' | 'done'
  amount: number
  deliveryDate: string
  updatedBy: string
}

// 状态到文案与颜色的映射，全站只此一份
export const STATUS_MAP: Record<Order['status'], { label: string; variant: 'secondary' | 'outline' | 'default' | 'destructive' }> = {
  draft: { label: '草稿', variant: 'outline' },
  pending: { label: '待审核', variant: 'secondary' },
  approved: { label: '已审核', variant: 'default' },
  done: { label: '已完成', variant: 'secondary' },
}

// 金额以分为单位存储，展示时格式化，避免浮点误差
const fmtMoney = (cents: number) =>
  new Intl.NumberFormat('zh-CN', { style: 'currency', currency: 'CNY' }).format(cents / 100)

export const columns: ColumnDef<Order>[] = [
  {
    id: 'select',
    header: ({ table }) => (
      <Checkbox
        checked={table.getIsAllPageRowsSelected()}
        onCheckedChange={(v) => table.toggleAllPageRowsSelected(!!v)}
        aria-label="全选"
      />
    ),
    cell: ({ row }) => (
      <Checkbox
        checked={row.getIsSelected()}
        onCheckedChange={(v) => row.toggleSelected(!!v)}
        aria-label="选择本行"
      />
    ),
    enableSorting: false,
    enableHiding: false,
  },
  {
    accessorKey: 'orderNo',
    header: ({ column }) => <DataTableColumnHeader column={column} title="单号" />,
    cell: ({ row }) => <span className="font-mono text-[13px]">{row.original.orderNo}</span>,
    enableHiding: false,
  },
  {
    accessorKey: 'customerName',
    header: ({ column }) => <DataTableColumnHeader column={column} title="客户" />,
    // 客户名允许折两行，超出省略并给 title
    cell: ({ row }) => (
      <span className="line-clamp-2 max-w-[220px]" title={row.original.customerName}>
        {row.original.customerName}
      </span>
    ),
  },
  {
    accessorKey: 'status',
    header: ({ column }) => <DataTableColumnHeader column={column} title="状态" />,
    cell: ({ row }) => {
      const s = STATUS_MAP[row.original.status]
      return <Badge variant={s.variant}>{s.label}</Badge>
    },
    // 服务端筛选时这里只控制显示，不参与本地过滤
    filterFn: (row, id, value: string[]) => value.includes(row.getValue(id)),
  },
  {
    accessorKey: 'amount',
    header: ({ column }) => <DataTableColumnHeader column={column} title="金额" />,
    cell: ({ row }) => <span className="tabular-nums">{fmtMoney(row.original.amount)}</span>,
    meta: { align: 'right' },
  },
  {
    accessorKey: 'deliveryDate',
    header: ({ column }) => <DataTableColumnHeader column={column} title="交期" />,
    cell: ({ row }) => <span className="tabular-nums text-[13px]">{row.original.deliveryDate}</span>,
  },
  {
    accessorKey: 'updatedBy',
    header: ({ column }) => <DataTableColumnHeader column={column} title="更新人" />,
    enableSorting: false,
  },
  {
    id: 'actions',
    cell: ({ row }) => <DataTableRowActions row={row} />,
    enableSorting: false,
    enableHiding: false,
  },
]

// 三个约定：
// 1. 列定义只描述数据，不请求接口。取数与分页由页面层负责。
// 2. 服务端分页时，pageSize 与 pageIndex 由外部受控，表格不自己维护。
// 3. 金额/日期列加 tabular-nums，数字才对得齐。
