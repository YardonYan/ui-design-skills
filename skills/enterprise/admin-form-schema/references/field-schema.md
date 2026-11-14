# 字段 Schema

后台页面做不好的根因，九成在字段没有定义就直接写界面。字段定义清楚之后，列表页、详情页、编辑页、导入校验、接口参数、数据库表都是它的投影，改动只改一处。

## 一个字段的十二个属性

| 属性 | 含义 | 不填的后果 |
|---|---|---|
| `fieldname` | 英文标识，入库与接口用 | 后期改一次动全链路 |
| `label` | 中文名，界面用 | 用户看不懂 |
| `type` | 字段类型，见下表 | 控件选错，校验无从谈起 |
| `required` | 是否必填 | 脏数据入库 |
| `options` | 下拉/关联的来源 | 选项写死在代码里 |
| `group` | 属于哪个分组 | 一百多个字段平铺 |
| `order` | 组内排序 | 顺序随缘 |
| `in_list` | 是否进列表页 | 列表塞二十列 |
| `default` | 默认值 | 每次都要手填 |
| `depends_on` | 联动条件 | 不该出现的字段一直显示 |
| `readonly_when` | 何时只读 | 已审核单据还能改 |
| `help` | 填写说明 | 用户反复来问 |

其中 `in_list` 最容易漏。列表页的列不是全字段，是选出来的 6 到 9 个。选谁：编号、名称、状态、金额、关键日期、负责人。其余进详情页。

## 字段类型与控件对应

| type | 界面控件 | 入库类型 | 校验要点 |
|---|---|---|---|
| text | Input | varchar | 长度上限 |
| textarea | Textarea | text | 长度上限 |
| richtext | 富文本编辑器 | text | 需白名单过滤 |
| number | Input[type=number] | numeric | 精度与范围 |
| integer | Input[type=number] step=1 | int | 非负或范围 |
| money | 金额输入（千分位） | numeric(18,2) | 不用 float |
| percent | 百分比输入 | numeric(5,2) | 0 到 100 |
| date | DatePicker | date | 允许的范围 |
| datetime | DatePicker + TimePicker | timestamptz | 存 UTC |
| select | Select | varchar | 值必须在字典内 |
| multiselect | 多选 / 标签 | jsonb 或关联表 | 同上 |
| reference | 关联选择（弹窗搜） | 外键 id | 目标必须存在 |
| checkbox | Switch / Checkbox | boolean | 无 |
| file | 上传（单/多） | 附件表 | 类型与大小 |
| table | 明细表格 | 子表 | 行内校验 |
| formula | 只读计算 | 不存或落冗余 | 后端复算 |
| section | 分组标题 | 不存 | 仅布局 |
| column_break | 分列标记 | 不存 | 仅布局 |

ERPNext 的销售订单定义里，176 个字段有 58 个是 `Section Break` / `Column Break` / `Tab Break`，真正承载数据的只有一百来个。这个比例说明一件事：字段多不可怕，可怕的是没有分层。分组用的不是数据字段，是布局标记，它们不进数据库、不进接口、只影响渲染。

## 三层分组

```
Tab（页签）      ：一屏放不下时按业务阶段切，2 到 5 个
  Section（段落）：一个业务动作一组，一组 5 到 12 个字段
    Column Break：组内两列排布，左右各一列
```

判断一段该不该独立：如果这组字段由同一个人在同一步填完，就独立成段。如果填的人是两个，说明该拆成两个单据或两步流程。

## 联动与只读

联动用条件表达式，别用散落的 if：

```json
{ "fieldname": "po_date", "depends_on": "eval:doc.po_no", "label": "客户订单日期" }
```

含义是"填了客户订单号才显示订单日期"。要点：

- 隐藏时清空该字段的值，否则会存进去一个用户看不见的数据。
- 只读条件与联动分开写。已审核、已归档的单据整体只读，这是状态决定的，不是字段决定的。
- 联动链不要超过三层。A 影响 B、B 影响 C、C 影响 D 的时候，用户已经无法预测界面变化。

## 校验分级

校验不是"通过/不通过"两态，是三态：

| 级别 | 例子 | 处置 |
|---|---|---|
| 阻断 | 必填缺失、类型不符、关联对象不存在 | 不允许提交，不允许入库 |
| 警告 | 字典外的值、疑似重复、日期倒挂 | 允许忽略并继续，但要记录 |
| 提示 | 金额偏离历史均值、数量异常大 | 只提示，不拦 |

导入场景里这个分级决定用户体验。128 行里 7 行有问题，如果全部阻断，用户要改完再来一次；分级之后可以"忽略 7 行继续"，先把 121 行推进去。

## 一个完整的 Schema 示例

通用制造业单据，字段结构可直接改用途。完整文件见 `templates/field-schema.example.json`。

```json
{
  "doc": "production_order",
  "label": "生产单",
  "numbering": { "prefix": "PO", "date_segment": "YYYYMM", "seq_length": 4 },
  "groups": [
    { "key": "basic", "label": "基本信息", "order": 1 },
    { "key": "product", "label": "产品与工艺", "order": 2 },
    { "key": "delivery", "label": "交付", "order": 3 }
  ],
  "fields": [
    {
      "fieldname": "customer_id",
      "label": "客户",
      "type": "reference",
      "options": "customer",
      "required": true,
      "group": "basic",
      "order": 1,
      "in_list": true
    },
    {
      "fieldname": "material",
      "label": "材质",
      "type": "select",
      "options": "dict:material_type",
      "required": true,
      "group": "product",
      "order": 1,
      "in_list": false
    },
    {
      "fieldname": "qty",
      "label": "数量",
      "type": "integer",
      "required": true,
      "group": "product",
      "order": 3,
      "min": 1,
      "in_list": false
    },
    {
      "fieldname": "delivery_date",
      "label": "交期",
      "type": "date",
      "required": true,
      "group": "delivery",
      "order": 1,
      "min_field": "order_date",
      "in_list": true
    }
  ],
  "validations": [
    { "level": "block", "rule": "delivery_date >= order_date", "message": "交期不能早于下单日" },
    { "level": "warn", "rule": "material in dict:material_type", "message": "材质不在字典内，请确认" },
    { "level": "info", "rule": "qty > 1000", "message": "数量偏大，请复核" }
  ]
}
```

## 落地顺序

1. 先出字段清单，用业务方的话写 label，不翻译成技术词。
2. 再定类型与必填。这一步要业务签字，因为改起来最贵。
3. 再分组排序。拿一张 A4 打印出来看，能不能一眼找到关键字段。
4. 再定校验分级。跟业务确认哪些能"忽略继续"。
5. 最后才是界面。Schema 稳定之前写组件都是返工。

## 与校验类 Agent 的关系

如果要做的是"上传文件 → 校验 → 出问题清单"这类智能体，这份 Schema 就是它的规则源。要点：

- 字段清单从真实文件里学，没出现过的字段不写进 Schema。尤其是下拉、手填、备注格都要覆盖。
- 校验只依据上传资料与这份 Schema，不联网、不猜测、不补充行业惯例。
- 输出问题清单时带行号、列名、原值、期望，四样齐全用户才能改。
- Schema 要能增量更新。业务加了新字段，追加即可，不要重建整份定义。
