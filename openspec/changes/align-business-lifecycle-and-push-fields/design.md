## Context

本计划以 2026-11-12 的本地 checkout 为实现基线，输入路径和 SHA256 见 [baseline.json](baseline.json)。
手机项目为 `C:/Users/admin/IdeaProjects/carvex-carplay-research/android`，
接收项目为 `C:/Users/admin/IdeaProjects/DiPlay`。历史 GalaxyPlay 观察与 DiPlay 源码联测分开记录，
不由 DiPlay 解析通过推断所有实车行为一致。

### 证据入口

所有以下链接相对本文件，实施时还须回到对应原始切片/调用链复核依赖的结论。

- [NowPlaying 规范](../../../research/protocol/iap2_input_business_lifecycle/spec/02-nowplaying.md)
- [导航规范](../../../research/protocol/iap2_input_business_lifecycle/spec/03-navigation-hud.md)
- [门控与顺序](../../../research/protocol/iap2_input_business_lifecycle/spec/05-gating-and-order.md)
- [生命周期](../../../research/protocol/iap2_input_business_lifecycle/spec/06-lifecycle.md)
- [资源清理](../../../research/protocol/iap2_input_business_lifecycle/spec/07-cleanup.md)
- [NowPlaying 原镜像数据流](../../../research/protocol/iap2_input_business_lifecycle/analysis/14-nowplaying-dataflow-audit.md)
- [SUS/ACK 与空参数原镜像审计](../../../research/protocol/iap2_input_business_lifecycle/analysis/12-lifecycle-and-empty-param-audit.md)
- [导航核心现有实现](../../../android/docs/fixes/2026-11-11-navigation-cluster-chain.md)
- [协商缓存容量修正](../../../android/docs/fixes/2026-11-11-receiver-navigation-capacity.md)
- [转向后道路文字修正](../../../android/docs/fixes/2026-11-12-navigation-after-road.md)
- [全程距离试验](../../../android/docs/fixes/2026-11-12-navigation-total-distance-trial.md)
- [完整原始输入诊断](../../../android/docs/fixes/2026-11-12-navigation-full-input.md)
- [可选接收源码联测](../../../android/tools/receiver-interop/README.md)

### 当前可定位差异与边界

| 项目 | 当前观察 | 后续处理 |
|---|---|---|
| 音乐早期订阅 | `SessionController` 在 bootstrap 回调写入全局 `NowPlayingUpdate.pendingSubscription`；当前源码搜索未见消费位置 | 核查 source/runtime endpoint、认证及控制会话归属，移除失效全局交接或实现同一 owner 的有效交接 |
| 音乐在途发送 | `AirSession` 的音乐发布走 `RuntimeIap.send`；导航走 `sendGuarded` | 区分链路代际保护与业务订阅撤销，复现 STOP/重订阅之后尚未分配序号的音乐任务 |
| 换曲增量 | `NowPlayingPublisher.update(replaceMedia=true)` 重置本地合并基线后发送 delta | 核查接收端缺失字段保留是否导致旧歌手/专辑/封面残留，按证据确定显式清除字段 |
| 接收播放状态 | `CarPlayPlaybackStatus` 仅状态 1 为 playing；`ClusterSongState` 将 1/3/4 视为 playing | 核查不同消费者需要的语义，保留实际 wire 状态并形成明确映射/测试，不能只统一布尔值掩盖差异 |
| 导航核心 | 已有 5201 状态、5202 定义、p13 引用、p7/p10 距离、容量复用与 guard | 按当前源码和接收解析器核查边界，复用已完成能力 |
| 接收显示能力 | DiPlay 声明导航组件 42、机动容量 8；START 为组件及两个空选项 | 手机消费实际协商数据；样本 ID/容量不是发送端默认值 |
| 路线概览 | afterRoad 已接通；`total_distance` 经用户要求作为 p7 试验值；时间/ETA/车道仍缺来源 | 保留试验标记，逐字段取证；缺来源的扩展任务待办 |
| 输出生命周期 | DiPlay 各 vendor 输出有 worker，断开会 clear；无线替换可保留展示 | 核查在途 worker 与新 owner 的隔离；展示缓存不能携带新会话发送授权 |

这些是候选差异，不是已证明的实车根因。当前计划没有执行新的行为测试。

## Goals / Non-Goals

### Goals

- 以实际会话、方向能力、订阅、组件和宿主来源决定每条业务消息是否可发布。
- 音乐与导航共享传输时仍各自管理业务状态、队列失效与资源清理。
- 明确未知、未携带、显式清空、零值和结束事件的区别。
- 把待办拆为可独立复现、验证和提交的任务，缺证据项保持 OPEN。

### Non-Goals

- 本文档提交不实施代码、不运行 Gradle、不打包或安装。
- 不更换已有连接状态机、认证流程、媒体协议或构建依赖。
- 不把单台车机样本、固定延迟或无条件重发当作协议修复。
- 不将没有 provider 的通话/车辆字段或没有来源的导航字段虚构为完整业务数据。

## Decisions

### 1. 先完成对账，再按可证差异实施

阶段 0 逐项记录原始依据、当前发送位置、接收位置、字段类型/长度/单位、声明与订阅条件。
`research/` 仍是正式协议结论入口；本变更的 delta specs 是本地实现验收合同。
现有已实现行为由回归覆盖，只有实际缺口形成生产修改。

### 2. 订阅绑定 owner，交接不制造授权

owner 至少区分 endpoint/承载、link generation/epoch、认证/识别上下文、业务订阅代际。
bootstrap 和 runtime 是否同一 owner 必须沿实际调用链确认；新传输不能自动继承旧订阅。
若早期命令属于当前仍有效的 owner，交接须保留原命令顺序、STOP 和失败语义；
否则关闭旧域并等待新端点实际订阅。业务快照可缓存，但不携带发送权限。

先沿用既有 RuntimeIap/IapLink 的串行与可靠传输结构，再补业务级有效性。
STOP、订阅替换、失效和断开撤销尚未提交的任务；已提交分片依原可靠传输完成。
guard 不持有 publisher/relay 锁，避免 writer 与业务回调锁顺序倒置。

### 3. 分别处理挂起、恢复和断开

SUS 是链路控制帧，不是业务消息。Apple 24A446 包型与局部路径见原审计，
完整对端恢复时序/订阅保留仍有 OPEN。平台休眠、AirPlay 流挂起不能直接代替 iAP2 挂起。
本地策略是在已确认的失效/挂起边界关业务门并撤销旧工作，保留链路 ACK/重传/恢复任务；
有效性重新确认前不自动重放业务。断开后清除 owner 授权，清理须可重复执行。

### 4. 字段按能力、订阅及来源发布

| 业务 | 对端控制消息 | 手机更新 | 核心约束 |
|---|---|---|---|
| 音乐 | 5000 START / 5002 STOP；5003 另作播放器请求 | 5001 的媒体组 0、播放组 1；其他组逐项核查 | START 参数 0/1/2 的布局不同；封面通过文件传输与引用 |
| 导航 | 5200 START / 5203 STOP | 5201 路线、5202 机动、可选 5204 车道 | 组件/选项来自 START，文字/容量来自 Identification，定义与引用一致 |

音乐保留原 wire 播放状态，按消费者用途推导状态；换曲需明确哪些已订阅字段被清除。
5003 的解析接受、平台请求发出与实际执行分别记录，不能用本地改 snapshot 冒充播放器执行。
初始、增量和封面交付继续按已核编码链/测试约束，失败不提升为发送成功。

导航保留 currentRoad 与 afterRoad、p7 全程剩余距离与 p10 机动距离的区别。
未知/清除引起接收旧值风险时，采用已有可证 reset/重建合同，而不自行推断抵达或取消原因。
多组件按实际能力限制，机动容量复用、单槽顺序和 U16 边界由实际解析器验证。
文字的 NUL、长度计量和容量规则需原证据闭合后实施；不得凭字段名按字节/字符换算。

### 5. 接收端修改以实际缺陷和输出用途为依据

DiPlay 的音乐状态、音乐卡、导航快照及各输出分别拥有状态。
音乐暂停不得清除活动路线；导航结束不得改变真实音乐状态。
无线切换保留的展示缓存只供展示，须有明确失效边界，不能跨 owner 继续接受旧 worker 回调。
部分字段无效不能破坏其他完整域；非法父/子 TLV 的更新策略须按现有解析合同复核。

### 6. 独立任务独立提交

任务号见 [tasks.md](tasks.md)。后续每项实施包含：复现/证据、备份、最小修改、必要测试、验证记录、提交。
一个任务若同时修改手机和车机，两个仓库分别提交，以相同任务号交叉引用；
根仓库的子模块指针更新单独关联，不混入未授权或无关的已有改动。
只读对账/取证任务完成后提交其文档与证据；没有有效来源的实现任务保持未勾选。
任务复选框只能在自身验收满足时完成，Gradle up-to-date、SKIP 和实车观察分开记录。

## Risks / Trade-offs

- 将早期订阅直接传入 runtime 可跨 endpoint 错授权限；任务 1.1 必须先核归属。
- 换曲全字段清零可能制造未知值，纯 delta 又可能留下旧值；任务 2.2 需逐字段确定清除合同。
- 取消未提交帧与中断已提交分片的效果不同；任务 1.2 保持可靠传输边界。
- vendor 调用可能长时间阻塞；清理策略要覆盖在途任务，不能依赖任意等待时间。
- `total_distance` 可能为道路切换时缓存的机动距离，试验映射可能显示跳变；保持现有标记直到现场核实。
- 旧修复记录有失效路径及不可用外部证据；新的对账不能只依其文字关闭任务。

## Migration Plan

按阶段 0 → 1 → 2 → 3 → 4 → 5 推进，每项可独立提交。需要原始宿主/设备输入的
阶段 4 子项先完成来源调查，证据不足时保持待办，其余独立项仍可推进。
实现前核对双方新 HEAD；每个提交记录适用证据与检查结果，实车包由用户按匹配提交构建安装。
回退以每项提交为单位，保留前后证据，不回滚用户无关工作。

## Open Questions

1. bootstrap 收到的音乐命令是否存在可持续使用的同一控制端点/owner？当前全局暂存未见消费。
2. 原会话 SUS/Resume 后哪些订阅保留条件可由原路径证明？任意 ACK 不构成恢复授权。
3. 5003 的 elapsed/queue 请求如何连接实际播放器，单位及执行失败反馈是什么？
4. 歌手/专辑/封面未知或缺失时，怎样发送有效清除而不制造虚假的实时值？
5. DiPlay 的音乐状态消费者对 seek/paused/unknown 应分别采取何种行为？
6. remaining time、ETA、目的地及车道的可靠宿主来源、单位、枚举及文字长度合同何时具备？
7. `total_distance` 的现场角色、活动导航中音乐暂停的同窗事件及各输出实际显示是什么？
