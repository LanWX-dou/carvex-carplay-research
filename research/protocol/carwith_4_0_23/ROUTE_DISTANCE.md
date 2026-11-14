# 全程剩余距离字段复查（2026-11-14）

用户已明确否定`total_distance`的全程距离角色。原APK也显示它只是在道路提示变化时缓存机动距离。
本次查找的是到目的地的全程剩余距离；不将单个路段距离、机动参考值或已规划路线总长混用。

## 查到的其他字段

| 字段 | 实际位置与数据流 | 当前可用性 |
|---|---|---|
| `destinationRemainingDistance` | EasyConn `ECP_P2C_PHONE_HUDINFO`，命令`0x20110`；`HUDINFO.k:int`经getter写入同名JSON键 | 独立于道路剩余距离的目的地剩余距离字段；未找到当前业务赋值或消息构造调用，单位/真实provider仍OPEN |
| `BMapBridge.NavigationInfo.remainDistance` | EasyConn地图桥模型，`int`，getter/setter直接读写模型字段 | 仅模型定义；全DEX引用索引无getter/setter调用，不能证明其当前值是全程距离或已传出 |
| `ucar.map.bundle.TITLE_1` / `TITLE_2` | `UCarMapInfo.fromBundle`读字符串→`LauncherDataBusClient.G/F`→原生`NavigationInfo.title1/title2` | 现有原生导航输入的候选概要文本；没有固定距离/时间语义，混合HUD Intent未复制它们，须上游样本确认 |

首项是此次找到的最明确的替代字段：消息同时编码`roadRemainingDistance`与
`destinationRemainingDistance`，分别来自`HUDINFO.i`与`HUDINFO.k`，并非同一数值的别名。
它还编码`destinationRemainingTime`、`arriveTime`和`arriveTimeZone`。
`destinationRemainingTime`用于`Calendar.add(13, value)`计算到达时间，
在这段SDK代码内按秒使用；这不证明CarWith当前导航已提供这些值或距离单位已经闭合。

## 原字节与引用核对

输入`CarWith_4.0.23-20261016.apk`，SHA256
`c897a45d92c84f06e670fc4edd323824093a093f67d8e7d7b058fee2a737d06c`。
本轮重新比较全部8个缓存DEX与APK条目，并用SDK36.0.0 `dexdump -d -n`
重新反汇编9个相关类，逐字节比较既有反汇编缓存。
详细身份及哈希见[机器审计](inventory/route_distance_audit.json)。

| 原指令/代码偏移 | 已核数据流 |
|---|---|
| classes8 `200444` getter，`200454`指令 | `getDestinationRemainingDistance`读取`HUDINFO.k:I` |
| classes8 `2005cc` setter，`2005dc`指令 | `setDestinationRemainingDistance(int)`写入`HUDINFO.k:I` |
| classes8 `20048c` getter，`20049c`指令 | `getRoadRemainingDistance`读取另一个字段`HUDINFO.i:I` |
| classes8 `200cf4`消息body，`200dee..200dfe` | 字符串键→目的地距离getter→`JSONObject.put(String,int)` |
| classes8 `200cec` | 返回命令`0x20110` |
| classes2 `17ae52..17ae84` | `where`比较及缓存机动距离→混合HUD的`total_distance` |
| classes2 `17afd0` / `17afd8` | 原生导航读取`UCarMapInfo.getTitle1/getTitle2` |
| classes5 `1b8be4` | `fromBundle`读取`ucar.map.bundle.TITLE_1/TITLE_2` |

本轮扫描既有完整DEX引用索引中的222,476个有代码方法：目的地距离setter调用0个，
getter调用1个且仅为上述JSON封装；`setHudinfo`调用0个，HUD消息构造调用0个；
`BMapBridge.NavigationInfo`距离getter/setter调用均0个。
这些计数覆盖DEX直接引用，不排除反射/JNI/外部动态实现；不能据此宣称整个SDK绝对不会运行。
`BMapBridge`反射目标`net.carman.baidumap.bridge.BMapBridgeImpl`仍不在本APK的8个DEX内。

`TITLE_1`在本地导航UI中可直接交给TextView展示，未按路线距离标量解析；
所以不能把`TITLE_1`固定视为距离、`TITLE_2`固定视为时间。
对现有地图导航继续取证，应在`UCarMapInfo.fromBundle`、`LauncherDataBusClient.G/F`
简化之前记录这两个字段的实际类型、文本和地图屏显，而不是给当前混合回调增加猜测的Extra名。

## 实现处理（首次撤下旧试验）

CarVeX撤下此前用户要求的`total_distance`试验映射。活动HUD明确清除
`HostNavigationDelta.distanceRemainingMeters`，使旧试验值不能保留；
`total_distance`仍只供`observation.referenceDistanceMeters`及原始诊断使用。
`remain_distance`继续供机动距离。不自动解析上述SDK/原生候选字段，没有虚构全程值。

4.2的试验候选已被否定，但真实全程距离provider尚未接通，因此该任务仍OPEN。
修改与本轮回归见[修正记录](../../../android/docs/fixes/2026-11-14-navigation-route-distance-source.md)。

复现：

```powershell
python -X utf8 -B research/protocol/carwith_4_0_23/tools/audit_route_distance.py --apk C:/Users/admin/Desktop/CarWith_4.0.23-20261016.apk --cache local-backups/carwith-navigation-apk --dexdump C:/Users/admin/AppData/Local/Android/Sdk/build-tools/36.0.0/dexdump.exe --output local-backups/2026-11-14-route-distance/audit
```

本次不安装或运行APK，不代替实车来源/单位验证。原反汇编只保留在local-backups；工具可由同一APK复现。

## 后续用户授权的目的地距离/时间试验

2026-11-14用户明确要求`destinationRemainingDistance`先按米、
`destinationRemainingTime`先按秒设置，实车不符后调整。
CarVeX已审版本的活动mixing HUD启用两个同名extra的输入映射；
距离→`distanceRemainingMeters`→5201/p7 U32，时间→`timeRemainingSeconds`→5201/p6 U64。
缺失/非法时清除旧值，显式0直传，保留用户试验来源标签；不恢复`total_distance`映射。
此次按用户授权启用候选输入，不将静态getter/JSON封装记为真实mixing provider证据；
如实际回调未携带对应字段，日志将显示absent，继续追踪上游来源。
单位和实时来源仍待实车核对，4.2/4.3完整验收保持OPEN。
详见[试验实现与验证](../../../android/docs/fixes/2026-11-14-navigation-destination-distance-time-trial.md)。
