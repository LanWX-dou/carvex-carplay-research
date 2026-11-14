# CarWith 全程剩余距离与时间候选复查

2026-11-14。输入为桌面 `device-log (1).txt` 与 `CarWith_4.0.23-20261016.apk`。本次只做日志及静态数据流核查，没有修改 Android 实现、构建或安装 APK。

结论：当前实测混合 HUD 没有另一组全程剩余距离/时间字段。原生地图输入的 `ucar.map.bundle.TITLE_1/TITLE_2` 是优先取证的候选；它们确实沿当前原生导航链传递，但内容、顺序和单位仍未取得运行样本。EasyConn 的剩余信息回调与模型是另一条候选链，尚无当前业务调用证据。

## 日志中的实际字段

日志共 8,665 行。原始诊断捕获 9 次 `mix_notify_start_navi` 与 16 次 `carlife_show_hud_info`。

HUD 的完整键集合为 `action, navi_turn, remain_distance, road_name, total_distance, turn_icon_data`，没有时间字段、`TITLE_1/TITLE_2` 或两个 `destinationRemaining*` 字段。

| 字段 | 16 次 HUD 中的值 | 判断 |
|---|---|---|
| `remain_distance` | 0 共 11 次；44 共 5 次 | 机动距离，不是独立全程剩余距离 |
| `total_distance` | 0 共 10 次；44 共 6 次 | 缓存机动参考值；不能当作全程剩余距离 |
| `destinationRemainingDistance` | 未携带 | 没有目的地剩余距离数值 |
| `destinationRemainingTime` | 未携带 | 没有目的地剩余时间数值 |

日志中其他 `curTime/duration` 来自 `carlife_vehicle_music_progress/info`，属于音乐进度和时长。

## 其他候选与数据流

| 候选 | 核实内容 | 当前限制 |
|---|---|---|
| `ucar.map.bundle.TITLE_1/TITLE_2` → `UCarMapInfo.title1/title2` | `fromBundle` 读取两个字符串；地图服务转给导航监听器，随后原生导航继续传递 | 通用文本，不能固定认定某个是距离、另一个是时间；当前 mixing HUD 不复制它们 |
| `BMapBridge.NavigationInfo.remainDistance/remainTime` | 两个公开 `int` 字段及对应 getter/setter | getter/setter 无 DEX 直接调用；单位和实时值未知 |
| `BMapBridge.NaviDataInterface.onRemainInfoUpdate(int,int)` | 存在剩余信息回调定义 | 没有直接调用；参数顺序和单位尚未证实 |
| `onViaListRemainInfoUpdate(int[],int[])` | 存在途经点剩余信息数组回调定义 | 没有直接调用；不能把途经点数据直接当作目的地剩余值 |
| EasyConn HUD `arriveTime/arriveTimeZone` | `arriveTime` 是当前 Calendar 加上正的 `destinationRemainingTime` 后的毫秒值；时区来自本机默认时区 | 与 `destinationRemainingTime` 同源，并非另一条独立时间来源；没有当前 mixing 提供证据 |
| `roadRemainingDistance/roadRemainingTime` | EasyConn HUD 同时定义道路与目的地两组字段 | 道路剩余量与目的地剩余量需区分，不能互换 |

骑行模型 `BikeNaviInfo` 另有 `remainDistance/remainTime` 及文本版本，对应回调也存在，但没有直接调用证据，不作为当前驾车导航输入。路线规划数据也不能仅凭字段名字当作动态剩余量。

## 已追踪的原生输入边界

1. `IUCarMapServiceStub.showNavInfo(Bundle,Bundle)`，classes5 `1ba0bc`：确认调用方包名，将其写入 Bundle；`1ba12a` 调用 `UCarMapInfo.fromBundle`，`1ba13e` 将模型交给导航监听器。
2. `UCarMapInfo.fromBundle`，classes5 `1b8be4`：`1b8c34..1b8c4a` 读取 `TITLE_1/TITLE_2`，类型为字符串。
3. `com.carwith.launcher.map.m$a.a`，classes2 `1bb4b0`：`1bb56c/1bb574` 读取两个 title。
4. `LauncherDataBusClient.G`，classes2 `17af64`：`17afd0/17afd8` 读取两个 title，再调用 `F`。
5. `LauncherDataBusClient.F`，classes2 `17abdc`：构造原生 `NavigationInfo` 并进入 `H`（`17ad08`）；另行构造 mixing HUD，未复制两个 title。不能把原生链上有字段等同于 CarVeX 的 mixing 回调已经收到。

EasyConn `BMapBridge` 通过反射加载地图桥实现；本 APK 八个 DEX 都没有 `BMapBridgeImpl` 类。未找到 DEX 直接调用不能排除外部实现、反射或 JNI。

## 本次验证范围

重新比较八个 APK DEX 与缓存 DEX，逐字节一致，APK DEX 哈希与既有 [审计身份](../../protocol/carwith_4_0_23/inventory/route_distance_audit.json) 一致。

扫描八份完整引用索引，共 222,476 个有代码方法：

- `NavigationInfo.getRemainTime/setRemainTime`：各 0 个直接调用。
- `HUDINFO.getDestinationRemainingTime`：1 个调用方法，仅 `ECP_P2C_PHONE_HUDINFO.preRequest@200cf4`；同一方法中读取两次。setter：0 个调用。
- `onRemainInfoUpdate/onViaListRemainInfoUpdate`：各 0 个直接调用。
- 骑行 `onRemainDistanceUpdate/onRemainTimeUpdate`：各 0 个直接调用。
- `UCarMapInfo.fromBundle`：1 个调用方法，即 `IUCarMapServiceStub.showNavInfo`。
- `UCarMapInfo.getTitle1/getTitle2`：分别 4/2 个调用方法，包含原生导航及本地导航 UI。

因此下一处取证点是 CarWith 内部 `showNavInfo` 或 `fromBundle` 的原始输入，记录 `TITLE_1/TITLE_2` 与地图包名并对照地图屏显。这需要上游观测，单纯在当前 mixing 回调添加同名 Extra 读取不会产生这些值。

此前目的地候选的原字节核查见 [ROUTE_DISTANCE.md](../../protocol/carwith_4_0_23/ROUTE_DISTANCE.md)。
