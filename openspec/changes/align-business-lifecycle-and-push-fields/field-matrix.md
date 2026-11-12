# 宿主到 DiPlay 的字段与生命周期对账

任务 0.3；2026-11-12。输入：手机 `6b6addc`、DiPlay `615b32c`，身份见
[执行基线](execution-baseline.json)。原固件依据见 [协议核对](protocol-contract.md)。
本表描述当前实现合同，不把 Kotlin 代码当作 Apple 证据。

## 音乐实际链路

[SessionController](../../../android/bridge/src/main/java/io/github/iamr0s/carvex/session/SessionController.kt)
接收 HostCallbacks.music/musicProgress、[音乐 Intent](../../../android/bridge/src/main/java/io/github/iamr0s/carvex/session/CarLifeMusicIntent.kt)
和匹配到的 MediaSession 状态 → 会话内
[HostMusicRelay](../../../android/bridge/src/main/java/io/github/iamr0s/carvex/session/HostMusicRelay.kt)
→ AirSession.nowPlaying → [NowPlayingPublisher/编码](../../../android/protocol-carplay/src/main/java/io/github/iamr0s/carvex/carplay/core/NowPlayingUpdate.kt)
→ RuntimeIap → 5001 → DiPlay CarPlayPlaybackStatus / ClusterSongState
→ Android MediaSession、音乐卡、仪表歌曲、CarPlayGlance。
封面由 ArtworkLoader → [NowPlayingArtwork](../../../android/protocol-carplay/src/main/java/io/github/iamr0s/carvex/carplay/core/NowPlayingArtwork.kt)
→ 5001 引用 + file session → DiPlay 文件接收/封面队列。

DiPlay 文件均相对 `C:/Users/admin/IdeaProjects/DiPlay`：
`shared/src/main/java/com/shilapi/xcertplay/` 下的 `media/CarPlayPlaybackStatus.kt`、
`hud/BydClusterSong.kt`、`glance/CarPlayGlance.kt`；
`common/src/main/java/com/shilapi/xcertplay/` 下的 `CarPlayMediaKeys.kt`、
`NowPlayingArtworkQueue.kt`、`AlbumTrackIdentity.kt`、`ClusterMusicState.kt`。
完整源文件/截取 body 的哈希在 receiver-interop manifest 登记。

基线 DiPlay 5000 选择媒体 `{1,4,6,12,26}`、播放 `{0,1,7}`。
其他可编码属性必须被实际 START 选中才可输出，不能推断当前 DiPlay 已消费。
Track null=未知/本次缺失；merge 保留旧值。空文本=单 NUL，接收端清为空。
零是显式值，不能由未知生成。独立 START 初始默认消息的零不代表真实播放器状态。

| 来源 → Track | 5001 组/项、布局 | DiPlay 消费、缺失/清除/零与单位 |
|---|---|---|
| song/title → title；artist → artist；Intent album → album | 0/1、0/12、0/6 UTF-8+NUL | playback/歌曲/音乐卡。缺失保留，空清除；换曲只发 delta 会留下旧歌手/专辑 |
| HostMusic.duration / Intent duration → durationMs | 0/4 U32 | durationMillis。HostMusic 仅 1..U32MAX；来源/线上毫秒对应是本地假设，实车单位 OPEN |
| progress/curTime → elapsedMs | 1/1 U32 | elapsedMillis；0有效，范围外拒绝。缺失保留；单位同上 OPEN |
| MediaPlaybackMonitor → status | 1/0 U8：STOPPED0/PLAYING1/PAUSED2/SEEK3,4 | playback 仅1=true；歌曲1/3/4=true。未知不发布；需保留实际 wire 状态并按用途映射 |
| index/playlistSize → queueIndex/queueCount | 1/2、1/3 U32 | 当前 DiPlay 不选择。index>=0，count>0；基数/执行有效值 OPEN |
| source / Intent app → appName | 1/7 文本 | sourceApp/音乐卡；应用跨换曲独立，null不自动清空 |
| 匹配曲目图片 → Artwork缓存 | 0/26 U8 transfer ID，图片走 file session | playback→NowPlayingArtworkQueue；旧引用/transfer必须失效；无图清除线上值未证，不伪造ID |
| 当前无 provider → persistentId、专辑序号/数量/盘号/盘数 | 0/0 U64；0/7,8,9,10 U16 | 不选择；未知省略，数字清除合同未证，不补0 |
| 无 provider → genre/composer | 0/16、0/18 文本 | 不选择；未知省略，显式空文本可清 |
| 无 provider → like/ban supported、liked/banned、chapterCount | 0/21..24 U8 bool；0/27 U16 | 不选择；false/0只取显式输入或独立初始化 |
| 无 provider → queueChapterIndex/shuffle/repeat | 1/4 U32；1/5,6 U8 | 不选择；非空按范围校验，未知省略 |
| 无 provider → libraryUid/radioStation/appBundleId | 1/8,10,16 文本 | 不选择；未知省略，显式空可清 |
| 无 provider → radioAd/radioPlaylistId/speed/setElapsedAvailable | 1/9 U8；1/11 U64；1/12 U16；1/13 U8 | 不选择；speed业务单位 OPEN |
| 5003 → elapsed/queueIndex/window | 顶层0/1/2 U32；p2 auto=ffffffff | 手机暂无真实请求provider。基线 setInfo 回写snapshot冒充执行；解析/请求发出/实际状态须拆开；p2即时请求受START子项门控 |

文本当前防御：禁止内嵌NUL、孤立surrogate，最多4096 UTF-8字节。
这是本地资源上限，不是已证Apple/车机最大字符数。完整队列输出暂无provider。

## 导航实际链路

[CarWithNavigation](../../../android/host-carlife-mixing/src/main/java/io/github/iamr0s/carvex/host/vendor/CarWithNavigation.kt)
原事件+source/binding/evidence → [HostNavigationRelay](../../../android/bridge/src/main/java/io/github/iamr0s/carvex/session/HostNavigationRelay.kt)
immutable NavigationSnapshot → [NavigationPublisher/Encoding](../../../android/protocol-carplay/src/main/java/io/github/iamr0s/carvex/carplay/core/NavigationPublisher.kt)
/ [NavigationGuidance](../../../android/protocol-carplay/src/main/java/io/github/iamr0s/carvex/carplay/core/NavigationGuidance.kt)
→ guarded RuntimeIap → 5202定义 → 5201引用 → DiPlay BydHudRouteState
→ BYD HUD/仪表/工厂导航/FCE/CarPlayGlance。5204为独立通道，目前没有完整真实来源。

DiPlay读取入口：`shared/src/main/java/com/shilapi/xcertplay/` 下的
`hud/BydHudRouteState.kt`、`hud/BydNavigationOutputs.kt`、`hud/NavigationOutputWorker.kt`、
`iap2/message/Iap2Messages.kt`、`iap2/message/Iap2LaneGuidance.kt`、
`transport/Iap2IdentificationClient.kt`。

| 来源 → 快照 | wire | DiPlay消费与缺失/清除合同 |
|---|---|---|
| source/binding/route/revision/maneuverGeneration | 本地代际，不编码 | 新owner/STOP/替换撤销未提交消息；已提交片继续可靠传输 |
| 实际 START.components + Identification | 各消息p0 U16组件 | 样本42；识别p2/p4文字64、p6机动8、p7车道文字64/p8车道8；手机不得默认42/8；未声明组件不发布 |
| ACTIVE/REROUTING/ENDED/INVALIDATED | 5201 p1 U8 | routeActive/reset；未知结束原因不补到达，音乐域独立 |
| currentRoad/destination | 5201 p3/p4 UTF-8+NUL | routeState保留；当前CarWith未证明来源；与afterRoad角色不同 |
| road_name → maneuver.afterRoad | 5202 p4文本 | roadFor优先afterRoad，空回退currentRoad；用户已确认来源角色；缺失变化使用reset/重建；长度计量OPEN |
| maneuver.description（暂无来源） | 5202 p2文本 | 当前核心显示不使用，不用道路名拼造机动描述 |
| navi_turn → 部分已证turn enum | 5202 p3 U8；p8驾驶侧 | BydManeuverCodes；未知不造默认箭头/驾驶侧 |
| remain_distance → maneuver.distanceMeters | 5201 p10 U32；5202 p5 U32 | 距离米；当前来源1..IntMAX-1；0/缺失来源有效性未证，走未知/reset |
| total_distance → route.distanceRemainingMeters | 5201 p7 U32 | remainingMeters；用户试验，保留user-test evidence；0可输入试验，角色/屏显对应OPEN |
| timeRemainingSeconds/arrivalEpochSeconds（暂无provider） | 5201 p6/p5 U64 | remainingSeconds/arrivalEpochSeconds；单位/清除/来源未闭合不启用，不由距离估算 |
| maneuver identity / capacity复用 | 5202 p1 U16 → 5201 p13 repeated U16 refs、p14 count | cache/activeIndex；最小已选容量；单槽先reset再定义/引用；未知内容清旧重建 |
| lanes（暂无完整provider） | 5204 p1 U16、p2子组、p3文本；5201 p16..18 | Iap2LaneGuidance→laneListener；独立音乐/路线；无来源/声明/容量不发布，不由图标反推 |
| 其余路线/机动扩展项 | 编码器p8/9/11/12/15/19..26等 | 当前完整链路未启用；布局/业务含义/来源未证保持OPEN |

HostNavigationField区分Absent/Unknown/Clear/Value；发布器已有reset/重建合同。
接收 omitted 常保留旧值，具体顺序须实际parser验证。无线展示缓存可保留，但不能携带旧worker授权。

## 候选差异与复现入口

类名为当前测试或明确待新增测试；本表没有宣称测试已运行。
[receiver-interop](../../../android/tools/receiver-interop/README.md) 使用实际完整Kotlin/原body。

| 任务 | 当前差异/待证项 | 复现或完成条件 |
|---|---|---|
| 1.1 | pendingSubscription只有写入；source/runtime认证不同 | Bootstrap/RuntimeIap测试；待新增未支持早期callback与独立owner场景 |
| 1.2 | music emit无业务guard | 待新增NowPlayingGuardedTransportTest：writer暂停，排队后STOP/START/link失效，旧任务不分配序号 |
| 1.3 | SUS/恢复与平台睡眠不能混用 | RuntimeIapTest/实际IapLink生命周期测试；未证完整恢复保持OPEN |
| 1.4 | HostMusicRelay无close；迟到图片/来源回调 | HostMusicRelayTest/HostNavigationRelayTest/NowPlayingArtworkTest：close后拒绝attach/update、幂等清理 |
| 2.1 | 既有selection需复核空项/重复/非法替换 | NowPlayingUpdateTest/NowPlayingInitialStateTest；组2高ID限制是本地防御 |
| 2.2 | replaceMedia重置缓存却只发delta | HostMusicRelayTest/NowPlayingInitialStateTest/ReceiverProtocolContractTest：新曲省artist/album时清旧文本，未知数字不补零，初始顺序独立 |
| 2.3 | setInfo伪造执行 | 新增请求测试：无provider不产生5001；真实provider/单位/反馈仍OPEN |
| 2.4 | reference无guard，file guard读取对象锁 | NowPlayingArtworkTest/待新增guarded测试：STOP/换曲取消旧引用，迟到ACK不推进新transfer |
| 2.5 | SEEK被压成不同boolean，丢原状态 | DiPlay CarPlayPlaybackStatusTest/BydClusterSongTest，Android MediaSession映射，未知U8/跨域测试 |
| 3.1 | 既有组件/能力门复核 | NavigationGuidanceTest/NavigationPublisherTest；DiPlay Iap2RouteGuidanceSubscriptionTest |
| 3.2 | 既有定义/引用/容量边界复核 | NavigationWireEncodingTest/NavigationPublisherTest/NavigationGuardedTransportTest/ReceiverProtocolContractTest：多组件/最小容量/单槽/100次/U16 |
| 3.3 | 既有reset路径复核 | HostNavigationRelayTest/NavigationPublisherTest/实际route parser：未知/重算/结束/重订阅 |
| 4.1 | afterRoad已接通，长度计量未闭合 | CarWithNavigationTest/NavigationWireEncodingTest/实际parser；多语言/NUL/surrogate；未证计量保持OPEN |
| 4.2 | total_distance试验 | 同路线完整raw→normalized→p7→屏显日志；非本地测试可完成 |
| 4.3 | 无ETA/时间来源 | 实际宿主字段、类型、单位、未知/清除和消费者证据；当前OPEN |
| 4.4 | 无完整lane来源 | 完整源模型、原wire枚举、容量和清除证据；当前OPEN |
| 4.5 | worker无queued/in-flight owner代际 | NavigationOutputWorkerTest：阻塞vendor后clear/start、队列满、终止清理；已进vendor不可中断调用须记录限制 |
| 4.6 | 独立分派，非法lane清除需核 | DiPlay glance/route/song/lane测试与实际interop逐域frame |
| 5.1–5.4 | 版本/报告/提交/实车 | 新manifest哈希与本轮Gradle、逐项execution和commit；无现场输入实车OPEN |

任务0.3完成源链、字段与复现条件的登记。生产代码、Gradle与实车行为尚未改变或验证。
