## Why

用户要求根据文档分阶段优化业务生命周期和推送字段，并指定 DiPlay 为接收端对账项目。
2026-11-12 的当前实现已包含导航状态、5202 机动定义、容量复用和发送前撤销；
不能按旧问题记录重复添加这些行为。仍需核查音乐早期订阅归属、音乐与导航的发送有效性、
字段清除、接收端状态消费和业务输出清理。

用户随后要求先形成 OPSX 文档，未来逐项实施。本变更当前只交付计划与验收合同；
生产代码未修改，所有实施任务保持待办。此前“完成一项提交一次”的约定继续适用于后续实施。

基线为手机端 `6b6addc44273f6b294a52bcb45cd381c3a35a1a3`、
DiPlay `615b32ce0b40cd0b99ce94ba23a512001553684f`；详见 [设计](design.md) 和
[输入快照](baseline.json)。根仓库已有 `.gitignore` 修改及未跟踪的 91 号问题记录，
本计划提交不包含这些既有改动。

## What Changes

- 建立当前文档、固件证据、发送端与接收端的逐消息/逐字段差异清单。
- 逐项收口订阅、退订、挂起、恢复、断开、重连及迟到回调的所有权和有效性检查。
- 核对 NowPlaying 初始与增量更新、换曲清除、播放状态、进度和封面传输。
- 核对导航组件/选项/容量、机动定义与引用、路线状态、距离和结束处理。
- 按证据完善道路、路线概览与车道字段，并检查 DiPlay 各输出的缓存及清理。
- 使用当前实际接收解析器联测，逐任务记录检查、提交与实车边界。

`total_distance` 的全程剩余里程角色仍为用户指定试验；剩余时间、ETA、车道来源继续待证。
本计划不将这些字段改写为 CONFIRMED，也不把音乐暂停与导航消失直接认定为同一根因。

## Capabilities

### New Capabilities

- `business-subscription-lifecycle`: 当前会话的业务门、订阅归属、提交前撤销及清理合同。
- `business-push-fields`: 音乐/导航的字段选择、增量/清除、能力约束和证据合同。
- `receiver-output-isolation`: DiPlay 音乐、导航及不同输出之间的状态归属和联测合同。

### Modified Capabilities

无既有 OpenSpec capability。正式协议事实仍维护在 `research/`，这里定义拟实施的验收要求。

## Impact

- 手机：`android/protocol-carplay`、`bridge`，以及确有字段来源变更时的 `protocol-api`、
  `host-api`、`host-carlife-mixing` 和 `platform-android`。
- 车机：DiPlay 的 `iap2/message`、`transport`、`media`、`hud` 与相关消费者；
  对账确认缺陷后再实施对应修改。
- 验证：现有 `android/tools/receiver-interop/`、受影响模块回归及各仓库要求的检查。
- 文档：本 OPSX 变更、对应 fix/evidence 记录及每项提交的验证记录。

开始实施前重新检查双方 HEAD 和工作区，不以本快照替代当时的代码审查。
