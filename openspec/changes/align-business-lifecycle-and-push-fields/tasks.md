## 实施约定

执行已开始，逐项状态与验证见 [execution.md](execution.md)。实施前重新检查 HEAD/工作区并备份受影响文件。
按用户2026-11-13最新要求，完成一个大项（0–5阶段）统一提交，小项只更新实现与验收记录；跨仓库分别提交并交叉引用。
每项完成记录包括证据地址/分支、当前差异、修改、实际检查结果和实车状态。
按用户后续要求，本轮以代码编译为验收范围，实车另行验证；2026-11-13用户要求先提交当前代码，尚未完成的编译/联测不记为通过。
缺证据、缺真实 provider、SKIP 或只有局部测试时，不勾选对应完整验收任务。

## 0. 当前基线与逐字段对账

- [x] 0.1 复核双方 HEAD、受影响源文件哈希及既有改动；补齐 `baseline.json` 与证据可用性清单。验收：每个实际输入可定位，历史快照与当前实现分开。
- [x] 0.2 从原字节/调用链核对 5000–5003、5200–5204 的方向、声明、字段/长度/顺序与失败路径。位置：`research/protocol/iap2_input_business_lifecycle`。验收：逐条列出 CONFIRMED/INFERRED/OPEN 及依据。
- [x] 0.3 建立“宿主 → 快照 → 发布器 → wire → DiPlay 消费者”字段表，记录缺失/清除/零值、单位及能力。位置：两端相关 Kotlin 与 change 对账记录。验收：每个候选差异有复现入口或明确待证条件。

## 1. 业务生命周期与订阅归属

- [x] 1.1 核查并修正音乐 bootstrap 订阅的 owner 归属及全局 `pendingSubscription` 路径。位置：`SessionController`、`Bootstrap`、`AirSession`、`NowPlayingUpdate`。验收：同 owner 早期 START/STOP 顺序正确；其他端点及旧会话不能授予新 runtime 订阅。
- [x] 1.2 为音乐未提交消息补业务订阅/会话有效性检查，覆盖 STOP、重订阅、失效和关闭。位置：`NowPlayingPublisher`、`AirSession`、`RuntimeIap`/`IapLink`。依据：R-6.8/6.14、本地在途任务策略。验收：writer 分配序号前拒绝过期任务，已提交分片保持可靠传输。
- [ ] 1.3 对账实际挂起/恢复与业务门，区分 iAP2、平台休眠和流关闭。位置：实际生命周期 owner 及相关发布器。依据：R-6.1–6.6/6.13–6.15。验收：未确认恢复不放行业务，链路 ACK/重传不中断；未证恢复分支继续 OPEN。
- [x] 1.4 收口断开、失败、取消和新连接的快照授权/回调/定时器清理。位置：`SessionController`、`AirSession`、各业务 relay/资源 owner。验收：重复清理安全，迟到完成不影响新 owner，应用缓存不携带旧发送权限。

## 2. NowPlaying 字段与传输

- [x] 2.1 核对 5000 参数 0/1/2 的空子项、0x11 U32、未知项、顺序/重复及非法替换行为。位置：`NowPlayingUpdate.selection`。依据：R-2.2–2.5/2.11、A14。验收：非法 START 不改变有效旧选择，更新按实际选择编码。
- [x] 2.2 完善 5001 初始/增量与换曲清除合同。位置：`NowPlayingPublisher`、`HostMusicRelay` 及元数据来源。验收：初始化不被实时值越过；省略保留、显式清除有效；换曲不残留旧歌手/专辑，同时不虚构未知数值。
- [ ] 2.3 核对 5003 解析、订阅子项门和实际播放器请求。位置：`NowPlayingPublisher.setInfo` 及平台接口。依据：A14.3。验收：请求、平台接受、实际状态分别记录；没有 provider 的操作明确待实现，不能用回写 snapshot 冒充执行。
- [x] 2.4 核对封面引用、曲目身份、订阅变化和失败清理。位置：`NowPlayingArtwork`、`AirSession` 与 DiPlay 文件接收/封面消费者。依据：R-2.9。验收：图像走文件通道，旧曲目/旧 owner 的迟到图片不覆盖新封面。
- [x] 2.5 统一播放状态的模型及各消费者用途。位置：手机 `PlaybackStatus`，DiPlay `CarPlayPlaybackStatus`/`ClusterSongState`。验收：PLAYING/PAUSED/STOPPED/SEEK/未知值各有明确行为和回归，音乐暂停不清活动导航。

## 3. 导航核心与能力

- [x] 3.1 复核 5200/5203 的组件/选项与消息能力、Identification 的显示声明。位置：`NavigationGuidance`/`NavigationDisplayCapabilities` 与 DiPlay `Iap2Messages`/`Iap2IdentificationClient`。验收：组件来自实际订阅，样本 42/8 不成为发送端默认，无组件或未声明能力保持明确门控。
- [x] 3.2 核对 5202 定义 → 5201 引用/状态/距离的字段及在途一致性。位置：`NavigationWireEncoding`/`NavigationPublisher` 和 `BydHudRouteState`。验收：多组件、最小容量、单槽顺序、100 次机动及 U16 边界均覆盖。
- [x] 3.3 收口重算、未知转向/距离、结束、退订与新路线。位置：`HostNavigationRelay`、发布器和接收快照。验收：只使用已有可证 reset/重建语义，不推断抵达原因；STOP 后无新更新，START 后旧任务失效。

## 4. 扩展字段与接收输出

- [ ] 4.1 核对 currentRoad/afterRoad/目的地/机动文字的来源、NUL 和识别长度限制。位置：宿主适配器、`NavigationWireEncoding` 与 DiPlay parser/output。验收：文字角色不混用；长度计量未证字段保持待办；显式清除与多语言边界覆盖。
- [ ] 4.2 查找并核实真实全程剩余距离来源。2026-11-14用户否定`total_distance`后，另明确授权`destinationRemainingDistance`先按米接入实车试验；同名extra映射、p7及清除已实现。位置：实际宿主输入、CarWith适配器与现场日志。验收：真实provider、类型/单位、缺失/清除及raw→normalized→p7→屏显闭合；真实输入及实车仍待核实，完整任务保持OPEN。
- [ ] 4.3 取证并接入全程剩余时间/ETA/其他路线概览字段。2026-11-14用户授权`destinationRemainingTime`先按秒试验，已启用同名extra→timeRemainingSeconds→p6 U64及清除；ETA仍未启用。位置：实际宿主输入、host-api、发布器和接收消费者。验收：真实字段来源、类型、单位、未知/清除及屏显全闭合；实时来源与实车仍OPEN，按用户授权先启用试验不代表完成完整验收。
- [ ] 4.4 取证并接入 5204 车道信息，定位每条车道的小箭头显示上个路口的症状。位置：原宿主完整输入、导航快照/发布器及 DiPlay `Iap2LaneGuidance`。验收：源 lane 模型、wire 枚举/布局、组件容量和换路口/结束清除有证据；无声明/来源不发布。用户2026-11-14明确症状为车道小箭头，尚未解决或完成实车复核。
- [x] 4.5 修正对账确认的 DiPlay 输出所有权/worker 在途缺陷。位置：`BydNavigationOutputs`、`NavigationOutputWorker`、各 HUD/仪表输出。验收：旧 owner 不更新新输出，阻塞/队列满后的清理明确，保留展示有失效边界。
- [x] 4.6 覆盖音乐、路线和车道的独立更新/清理。位置：DiPlay 分派、快照和消费者。验收：暂停/结束音乐不清有效导航；导航结束不改音乐；字段清空和非法更新不串域。

## 5. 联测与交付

- [x] 5.1 刷新实际 DiPlay parser 联测输入和哈希，覆盖此次确认的修正。位置：`android/tools/receiver-interop`。验收：实际源码/原 body 可追溯，默认生产编译不包含接收源码；缺文件/失败/跳过不能报通过。
- [ ] 5.2 对修改模块执行必要回归和手机 Kotlin 编译，若修改 DiPlay 执行其 AGENTS.md 指定完整 CI 检查。验收：按每项实际变更记录命令、退出码、失败/跳过、报告和适用提交，不把旧报告算成本轮新测试。
- [x] 5.3 逐任务补齐 fix/evidence、任务复选框、提交号及必要子模块指针。验收：按大项统一提交、跨仓库可关联，既有无关改动不入提交。
- [ ] 5.4 分场景实车验收：导航持续有效时播放→暂停→恢复→结束导航；重算/换曲；退订/重订阅；挂起/恢复；断开/重连。验收：从连接开始完整日志与屏显时间对应，分别报告 PASS/PARTIAL/FAIL/OPEN；本地检查不代替实车完成。
