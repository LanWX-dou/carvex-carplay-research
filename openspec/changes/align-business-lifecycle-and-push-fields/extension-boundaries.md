# 扩展来源与接收输出边界（2026-11-14，任务4）

本轮源调查使用手机 `7ac992c` 与 DiPlay `5436f91d`，后续接收修正另记提交。
原协议依据仍为[九消息核对](protocol-contract.md)与 R-3.12；本轮未扩大未证字段准入。

| 任务 | 实际来源/当前行为 | 本轮结果与剩余条件 |
|---|---|---|
| 4.1 | CarWithNavigation `road_name`→maneuver.afterRoad→5202/p4；没有 currentRoad、destination、maneuver.description 赋值provider | 已有角色保持独立，新增实际parser多语言/NUL/孤立surrogate/空清除合同。Identification文字计量及上限仍未证，4096字节只是本地防御；完整任务OPEN |
| 4.2 | 用户2026-11-14否定`total_distance`的全程角色，已撤下映射；仅保留缓存参考诊断 | 另找到SDK `destinationRemainingDistance`与原生TITLE候选，当前混合回调无真实provider；来源/单位/屏显仍OPEN，见[复查](../../../research/protocol/carwith_4_0_23/ROUTE_DISTANCE.md) |
| 4.3 | HostNavigationDelta有timeRemainingSeconds/arrivalEpochSeconds模型；真实host适配器无Value赋值 | 模型/接收字段存在不等于provider，继续省略p5/p6；单位与未知/清除待闭合，OPEN |
| 4.4 | HostNavigationLanes模型及原5204编码器存在；适配器没有真实lane赋值 | 无完整源模型/枚举/容量，不发布5204。新增实际lane解析仅使用人工测试值检查跨域隔离，不当作真实来源；OPEN |
| 4.5 | worker原先只在入队时检查accepting，clear只清队列；输出与控制回调没有owner参数 | 新增controller owner、link有效性与worker原子代际；旧queued/init/failure/cleanup拒绝，溢出及执行失败停止增量流，清理后必须start。已进入厂商服务的调用无法强制中断，返回后clear先于新initialize；完整项目验证见execution |
| 4.6 | 音乐/路线/车道各自消息分派和接收模型 | 新增实际parser全播放状态、路线结束、非法音乐/车道、文字清除及展示120s到期回归；实车另外验证 |

来源入口：
[宿主适配器](../../../android/host-carlife-mixing/src/main/java/io/github/iamr0s/carvex/host/vendor/CarWithNavigation.kt)、
[宿主模型](../../../android/host-api/src/main/java/io/github/iamr0s/carvex/sessioncore/HostNavigation.kt)、
[relay](../../../android/bridge/src/main/java/io/github/iamr0s/carvex/session/HostNavigationRelay.kt)、
[编码准入](../../../android/protocol-carplay/src/main/java/io/github/iamr0s/carvex/carplay/core/NavigationPublisher.kt)。

DiPlay修改为本地输出所有权策略，沿用原wire格式；不把接收实现当作Apple原协议证据。
保留overlay只作展示，原`staleRouteNs=120_000_000_000`到期检查继续有效；不携带发送权限。
回调guard只读原子代际、volatile channel/controller状态；不从worker获取controller/publisher锁。
所有已知来源外的字段继续OPEN，实车任务保留未完成。

本轮还复核本地 CarWith 4.0.23 APK SHA256为
`c897a45d92c84f06e670fc4edd323824093a093f67d8e7d7b058fee2a737d06c`，8份已提取DEX与该APK原条目逐字节一致。
既有原字节反汇编索引位于`local-backups/carwith-navigation-apk/`：混合回调`LauncherDataBusClient.F`
code item `classes2:17abdc`只输出当前HUD字段；通用`TITLE_1/TITLE_2`在原生CarLink出口，
不在混合Intent中。EasyConn剩余时间/车道定义缺业务调用及动态BMapBridgeImpl，不能作为可用provider。
本轮复核输入身份和当前适配器源链，没有重跑全部DEX反汇编或宣称完成动态平台取证。
