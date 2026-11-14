# CarWith 4.0.23：字段与接口静态分析

分析日期：2026-11-12。输入：`C:\Users\admin\Desktop\CarWith_4.0.23-20261016.apk`。

本报告依据 APK 原始字节、Manifest、DEX 类型/注解/常量/反汇编、包内 Protobuf 和 JSON 资源整理。未安装 APK、未调用远端接口、未抓取运行时流量。接口“存在于包内”与“当前运行时可以调用”分别标明。

## 1. 阅读入口与证据等级

- [HTML 阅读版及可搜索字段表](CarWith字段与接口分析.html)：双击即可离线查看。
- [附录：完整 Protobuf 字段及枚举](APPENDIX_PROTO.md)：342 个字段，含编号、类型、可选性、原注释与源码行号。
- [附录：完整 Binder 接口](APPENDIX_BINDER.md)：122 个接口、616 个方法，关联可恢复的事务编号。
- [附录：业务模型与配置字段](APPENDIX_MODELS.md)：业务模型、明确 JSON 名称与包内配置键。
- [完整机器清单](INVENTORY.md)：全部 DEX 字段/方法、URL、参数键、JNI、动态导出符号等 CSV/JSON。

| 等级 | 含义 | 能支持的结论 |
| --- | --- | --- |
| A：调用/写入代码 | 请求构造、Intent 写入、Protobuf builder、封包函数可直接定位 | 代码确实构造或消费这些字段；调用是否实际执行仍需运行样本 |
| B：定义 | DEX 接口、类字段、序列化注解或 Protobuf 声明 | 定义存在；不自动表示业务已经接通 |
| C：候选 | URL、相对路径、UUID、SDK 常量等字面量 | 候选入口；用途、拼接结果或可用性尚未完全确认 |

每个 CSV 使用 UTF-8 BOM，便于 Windows 表格工具识别中文。`class` 是 DEX 描述符，`code_offset` 是 code item 的文件偏移，`instruction_offset` 是实际指令文件偏移，均按十六进制记录；它们不是进程内存地址。混淆后的 `a/b/c` 等名称按原样保存，没有猜测并替换为“原始源码名”。

## 2. APK 身份与覆盖范围

| 项目 | 值 |
| --- | --- |
| 应用名称 | CarWith |
| 包名 | `com.miui.carlink` |
| versionName | `4.0.23-20261016` |
| versionCode | `104000023` |
| APK 大小 | 56,209,661 字节 |
| SHA-256 | `c897a45d92c84f06e670fc4edd323824093a093f67d8e7d7b058fee2a737d06c` |
| minSdk / targetSdk / compileSdk | 29 / 33 / 35 |
| ABI | `arm64-v8a` |
| ZIP 条目 / DEX / 原生库 | 4,969 / 8 / 25 |

| 静态提取项目 | 数量 |
| --- | --- |
| 类定义 | 33418 |
| 全量字段定义 | 497769 |
| 全量方法定义 | 233147 |
| Binder 接口/方法 | 122 / 616 |
| 明确 JSON 名称 | 266 |
| Protobuf 字段/枚举值 | 342 / 157 |
| 实际编译 Protobuf tag 匹配 | 300 |
| 静态键使用/不同键 | 2185 / 1137 |
| JSON 配置路径 | 1128 |
| native 方法 | 182 |

统计以所有 DEX 中的实际类定义、字段定义和方法定义为准，含依赖 SDK、生成的 Protobuf、资源类和混淆类。完整规模与各 DEX 哈希见 [manifest.json](manifest.json)。全部 33,418 个类的缓存反汇编均已与 Android SDK 36.0.0 `dexdump -d -n` 从原 DEX 重新生成的文本逐字节核验：[核验记录](inventory/assembly_verification.json)。

“能获取到的字段”在本报告中包含协议字段、方法参数类型、序列化名称、Bundle/Intent/JSON 键、配置字段和类成员。未恢复的参数原始名称、字段业务语义或线上样本不会编造。Java 字段不等于 HTTP 参数；SDK 定义不等于本应用向车机发送的数据。

## 3. HTTP / WebSocket 接口

### 3.1 CarWith 云端配置

**GET `https://carwith.link.miui.com/api/carLink/getConfig`**，等级 A。

| 参数 | 位置/类型 | 来源与行为 |
| --- | --- | --- |
| `uCarAppVersion` | Query / string | 常规分支读取本包 `PackageInfo.versionCode`，转十进制字符串；开发分支使用 `dev_version`；较旧系统分支使用 `999999999` |

本 APK 的正常版本号参数为 `104000023`。条件分支并非所有设备均执行同一个值。证据：`classes2.dex:p6.l.d@0x3b5a48` 与 `p6.l.b@0x3b59a4`；`classes4.dex:r9.a$d.a@0x1ae424`；应用市场与投屏白名单管理也调用同一路径。

请求链：`p6.l / r9.a / market.helper.i` → `l2.a.d/e` → `l2.d.b`。`l2.d.b` 调用 `so.a0$a.c()`，其函数体设置 `GET`；`l2.d.c()` 逐项将 Map 键值加入 URL query。这里已沿混淆后的请求构造器核验 HTTP 方法和参数位置。

响应解析目标为 `com.carwith.common.bean.CloudControlBean`，支持以下成员：

| 字段 | Java 类型 | 含义/边界 |
| --- | --- | --- |
| `uCarAppVersion` | string | 手机端版本相关配置 |
| `carAppVersion` | string | 车端版本相关配置 |
| `appWhiteList` | List | 应用白名单；元素类型见类泛型签名 |
| `appBlackList` | List | 应用黑名单 |
| `carModelBlackList` | List | 车型黑名单 |

`AppWhiteItem` 的实际成员为 `appCategory:int`、`appId:int`、`appMode:int`、`appName:string`、`applicationType:string`、`castType:int`、`packageName:string`、`versionCode:long`。这些类没有显式 `SerializedName`，报告按类成员名列出，不伪造在线响应样本、固定枚举或额外响应外壳。

### 3.2 百度地图车载连接事件

**GET `https://oem.map.baidu.com/agent/incar/event`**，等级 A。证据：`classes2.dex:com.carwith.launcher.map.a.d@0x1b4e44` → 同一 `l2.d.b` GET 构造器。

| Query 参数 | 类型 | 代码中的值或来源 |
| --- | --- | --- |
| `ts` | string | `System.currentTimeMillis()` 的字符串，毫秒 |
| `mb` | string | `Build.MODEL` |
| `os` | string | `Android` 与 `SDK_INT` 拼接 |
| `oaid` | string | OAID 获取函数返回值 |
| `phonebrand` | string | 常量 `xiaomi` |
| `event` | string | 连接分支 `0`，断开分支 `1` |
| `from` | string | 当前缓存的连接类型文本 |

`map.a$a.c` 增补请求头，包含包内固定的 Authorization 相关字符串。完整字面量保留在原始反汇编证据；这里不将其展示成可用凭据或成功调用示例。服务端鉴权结果没有验证。

### 3.3 AI 地址识别

**POST 路径 `https://ai.engine.miui.com/api/aiModel/completionText`**，等级 A。由 `com.carwith.common.aicr.model.aiaddress.b.b@classes.dex:0x4416d0` 构造参数，经 `x1.a.b@0x522898` 调用小米 `securePost` 路径。

| 参数键 | Java 类型 | 代码值 |
| --- | --- | --- |
| `bizCode` | string | `AiAddressRecognitionNavigation` |
| `openAiModel` | string | `tongYiQianWenTurbo` |
| `inputText` | string | 上游输入文本 |

参数以 Map 交给账号/安全请求库。最终加密、签名、Cookie 与 HTTP body 编码未完整复原，不能将上表直接当成普通 JSON POST 的可调用样例。

响应模型 `x1.b<T>` 的明确 JSON 名称为 `code:int`、`message:string`、`traceId:string`、`data:T`；结果模型 `x1.c` 映射 `resultContent:string`。这些名称来自 `SerializedName`，属于等级 B。

### 3.4 混淆后的 Retrofit 定义

包内 HTTP 注解位于 `pr.*`，标准 `retrofit2.http.*` 包名扫描无法发现它们。通过 `mr.r$a.e/g` 的注解解释器确认：`pr.f=GET`、`pr.o=POST`、`pr.a=Body`、`pr.t=Query`、`pr.k=Headers`。证据保存在 `source/dexdump/classes8/mr.r$a.txt`。

| 方法 | 路径 | 参数 | 返回模型 | 证据 |
| --- | --- | --- | --- | --- |
| POST | `/voiceassistant/miotauth/status` | JSON body `cb.b`：`accredit_switch:boolean` | `Single<cb.b>`，同名开关字段 | `classes4.dex:fb.a.a` |
| POST | `tone` | JSON body `cb.f`：`request_id:string`、`vendor_id:string`、`speak:List` | `Single<cb.e>`；data 列表成员存在，无明确 SerializedName | `classes4.dex:fb.b.a` |
| GET | `voiceassistant/privacy/status` | Query `deviceId:string` | `Observable<cb.d>` | `classes4.dex:fb.c.a` |
| POST | `voiceassistant/privacy/status` | JSON body `cb.a`；显式 `content-type:application/json`、`accept:*/*` | `Observable<cb.d>` | `classes4.dex:fb.c.b` |

`cb.a` 请求/数据对象：`watermark:long`、`device_id:string`、`privacy:cb.c`、`status:boolean`。`cb.c`：`address`、`smart_travel`、`simulation`、`contact`、`personalize`、`voice_wakeup`、`continuous_talk`、`schedule`，均为 boolean。`cb.d` 响应：`code:int`、`data:cb.a`、`message:string`。

隐私和米家授权相关客户端有 `nlp.xiaomixiaoai.com`、`nlp-preview.xiaomixiaoai.com`、`nlp-staging.ai.srv` 环境分支。`tone` 的 base URL 从 `th.a.b()` 获取。相对路径、前导 `/` 的解析行为和环境选择必须与调用方一起使用；以上相对路径不直接冒充本设备已经选定的完整 URL。

按上述客户端的正常命名分支，静态构造的完整 URL 为 `https://nlp.xiaomixiaoai.com/voiceassistant/miotauth/status`、`https://nlp.xiaomixiaoai.com/voiceassistant/privacy/status` 和 `https://speech.xiaomixiaoai.com/speech/v1.0/ptts/tone`。第三条来自 `th.a.b@classes7.dex:0x1a154c` 的 base 与 `tone` 相对路径组合；均有 preview/staging 等其它分支，未确认本设备运行时选择。

公共拦截器 `eb.a` 处理 `Authorization`，并识别 `AUTHORIZATION_NON_FLAG`、`i.xiaomixiaoai.com`、`ai-service` 等内部标志；部分 401 分支会重新取 token。这里只恢复头名、标志与代码路径，不声明存在匿名调用方式。

### 3.5 依赖 SDK 和其它候选地址

完整地址及出处见 [urls.csv](inventory/urls.csv) 和 [url_references.csv](inventory/url_references.csv)。它们同时包含 HTTP、WebSocket、Content URI、文档地址、XML namespace 和错误提示中的 URL，不能直接按条目数称为“有效接口数”。

| 地址/路径族 | 包内用途或归属 | 等级 |
| --- | --- | --- |
| `wss://speech.xiaomixiaoai.com/speech/v1.0/longaccess`、同路径 ws 与 preview/tw 变体 | 小爱语音长连接 SDK | B/C；运行时协议与请求样本未验证 |
| `cloudcontrol.xiaomixiaoai.com/aivs/v1.0/config` | 小爱云控 SDK | B/C |
| `speech.xiaomixiaoai.com/speech/v2.0/dump` | 语音 dump 接口族 | B/C |
| `multimodal-access.xiaomixiaoai.com/v1/resource/response` | 多模态资源 SDK | B/C |
| `cacerts.mica.xiaomixiaoai.com/api/certificate/sync` | 小爱证书同步 | B/C |
| `nlp.xiaomixiaoai.com/voiceassistant/privacy/v2` | 小爱隐私 API 的另一条路径；与 Retrofit status 路径分开 | B/C |
| `restsdk.amap.com/v3/iasdkauth`、`/v3/geocode/regeo`、`/v5` | 高德 SDK；存在双栈/HTTP/HTTPS 分支 | B/C |
| `apilocate.amap.com/mobile/binary` | 高德定位 SDK 的二进制接口 | B/C |
| `account.xiaomi.com`、`api.account.xiaomi.com/pass*`、`open.account.xiaomi.com` | 小米账号 SDK | B/C；常见 base 与后缀拼接，附录保存相对路径候选 |
| `openmobile.qq.com`、`wspeed.qq.com/w.cgi` 等 | 腾讯登录、统计等 SDK | B/C |
| `carwith.link.miui.com/static/userProtocol.html`、`supportedCarModels.html`、`privacy.mi.com/CarWith/zh_CN/` | 网页入口 | 已有引用；属于页面资源 |

此外提取了 291 个相对路径字面量候选。里面也会有文件路径与 SDK 路由，详见 [relative_path_candidates.csv](inventory/relative_path_candidates.csv)。

## 4. 原生 CarLink 车机通信

### 4.1 实际封包头

`ca.d.h()` 分配 20 字节头，`ca.k.l()` 拼接 `header[20] + payload`，`ca.l.a()` 将长度设置为 `payload.length+20`，等级 A。多字节整数字段通过 `ca.a` 按大端写入。

| 字节偏移 | 长度 | 字段 | 依据 |
| --- | --- | --- | --- |
| 0 | 4 | 总消息长度（含 20 字节头） | `ca.d.a` / `ca.l.a` |
| 4 | 4 | `seqId` | `ca.d.b` 日志名与序号生成函数 |
| 8 | 4 | `timestamp`，秒 | `currentTimeMillis()/1000` |
| 12 | 1 | 命令标志：来源、格式、消息类型 | `ca.d.o/g/j` 位移和掩码 |
| 13 | 1 | `CmdCategory` | 枚举 `getValue()` |
| 14 | 2 | `serviceId`，写入大端 | `ca.d.o` / `ca.b.d` |
| 16 | 2 | 保留字节，生成时写 0 | `ca.d.h` |
| 18 | 2 | 16 位头校验值 | `ca.c` 对前 18 字节计算，`ca.d.a` 校验 |
| 20 | 可变 | payload | 当前发送路径可直接序列化具体 Protobuf message |

偏移 12 的编码为 `sourceDevice + (dataFormat << 1) + (messageType << 3)`。解码掩码分别为 `0x01`、`0x06 >> 1`、`0x18 >> 3`。来源 `CAR=0`、`PHONE=1`；格式 `RAW=0`、`PB3=1`；类型 `SEND=0`、`REQ=1`、`RES=2`、`SEND_SYNC=3`。

命令分类：`NONE=0`、`CONTROL=1`、`SENSOR=2`、`AUTH=3`、`AUDIO=4`、`VIDEO=5`、`CERT=6`、`ACK=7`、`SHARE=8`。`serviceId` 的读取实现对两个字节直接使用 `aget-byte`，报告保留原代码，不自行修正符号扩展行为。

注意：`ControlChannel.HEADER_LENGTH=12` 确实存在，但上面的实际封包函数使用 20。两条证据须区分。头校验例程已保存，尚未将它命名为未经核验的某一种标准 CRC。

### 4.2 通道默认端口和定时参数

以下来自 `ChannelType.<clinit>@classes4.dex:0x153454` 的构造参数，不是当前已监听端口扫描结果。

| 通道 | 默认端口 |
| --- | --- |
| CUSTOM | 0 |
| UIBC | 4321 |
| RTSP | 7236 |
| RTP | 15550 |
| AUTH | 57209 |
| CONTROL | 57219 |
| MEDIA | 57229 |
| SENSOR | 57239 |
| CERT | 57249 |
| SHARE | 10113 |

`ControlChannel` 常量：心跳间隔 2,000 ms；心跳超时 10,000 ms；ACK 超时 500；重试次数 3；心跳服务号 240。完整常量清单见 [control_constants.csv](inventory/control_constants.csv)。没有据此假定所有连接模式都开启所有端口。

### 4.3 消息编号与 Protobuf 包装边界

包内 `ucar.proto` 定义 `ControlIndex`、`SensorIndex`、`AuthIndex`、`AudioIndex`、`CertIndex` 等索引结构。**Protobuf 字段 tag 和封包头 serviceId 是两种编号，只有沿封包构造代码验证的条目才直接关联。**

例如原生导航出口：

`LauncherDataBusClient.G/F` → `H` → `IDataBusService.sendNavigationInfoToCar` → `DataBusServiceStub.sendNavigationInfoToCar` → `ControlChannel.sendNavigationInfo` → `ca.j.B` → `da.a.w0`。

`ControlChannel.sendNavigationInfo@0x114ed4` 构造 `NotifyNavigationInfo`，`ca.j.B@0x0e0a30` 设置 `CONTROL` 分类和 serviceId 11，序列化的是这个具体 message。这里不能仅凭 `ControlIndex.notify_navigation_info=11` 就额外再包一层 `ControlIndex`。

音乐对应 `ControlChannel.sendMusicInfo@0x114d98` → `ca.j.A@0x0e09ec`，serviceId 10。已从代码恢复的 23 条封包映射详见 [wire_service_ids.csv](inventory/wire_service_ids.csv)。它们不等于全部可能命令。

### 4.4 认证和能力协商字段

`AuthRequest`：`version:int32`、`authPk:bytes`、`authPkHmac:bytes`、`agreementPk:bytes`、`agreementPkSig:bytes`、`random:bytes`、`id:bytes`、`model:string`、`userConfirmed:bool`、可选 `workModes:int32`、可选 `productName:string`。

`AuthResponse`：对应的公钥、HMAC、签名、随机数，以及 `version`、`result`、可选 `workModes`、`dayOrNightMode`、`screenInfo`。`AuthConfirm.cipher:bytes` 的包内注释为用会话密钥加密的手机本地 IP。注释记载 Request 的 id 为 6 字节、model 为 32 字节 UTF-8；不能把注释自动视为已核验的长度检查。

`GetUCarConfigResponse` 的 24 个字段涉及 `carBrMac`、屏幕尺寸、dpi、视频显示尺寸、fps、P2P、SoftAP、传输模式、5G 信道、摄像头、麦克风、低延迟解码、语音唤醒、自定义字段、sdkVersion、workModes、POI 导航、旋转、Home/Back 键、HEVC 与 realDpi。精确类型/tag/optional 见 Protobuf 附录。

这里只恢复消息结构，未取得任何运行时私钥、会话密钥、设备证书或服务器应答。

## 5. 导航、音乐及其它业务字段

### 5.1 原生导航与地图输入

`NotifyNavigationInfo` 的字段为 `isNavigating:bool=1`、`directionIcon:bytes=2`、`distance:string=3`、`distanceUnit:string=4`、`operation:string=5`、`where:string=6`、`title1:string=7`、`title2:string=8`、可选 `id:int32=9`。

地图输入 `UCarMapInfo.fromBundle` 读取以下键，等级 A；实际 Java 成员也已恢复：

| Bundle 键 | 读取类型 | 去向/边界 |
| --- | --- | --- |
| `ucar.map.bundle.DIRECTION_ICON` | Parcelable / Icon | 原生方向图标，也用于混合 HUD |
| `ucar.map.bundle.DISTANCE` | string | 机动提示距离文本 |
| `ucar.map.bundle.DISTANCE_UNIT` | string | 距离单位文本 |
| `ucar.map.bundle.OPERATION` | string | 导航操作文本 |
| `ucar.map.bundle.WHERE` | string | 道路/位置提示文本 |
| `ucar.map.bundle.TITLE_1` | string | 原生导航 title1 |
| `ucar.map.bundle.TITLE_2` | string | 原生导航 title2 |
| `ucar.map.bundle.pkg` | string | 地图包名 |
| `ucar.map.bundle.CROSSING_ICON` | Parcelable / Icon | 本地导航视图字段，已核验的原生 NavigationInfo 出口未复制它 |

还有 `EndType`、`NavType` 常量；状态常量 `STATUS_IN_CRUSE=1`、`STATUS_IN_NAV=2`，拼写按 APK 保存。`title1/title2` 是通用文本，不能只按名称或顺序认定为全程剩余距离、剩余时间或 ETA。

### 5.2 CarLife 混合回调的 HUD

`ICarLifeCastCallback.invokeMethod(Intent)` 出口使用 action `carlife_show_hud_info`。`LauncherDataBusClient.F@classes2.dex:0x17abdc` 构造更新，`D` 构造结束/清理，等级 A。

| Extra 键 | 类型 | 实际代码含义 |
| --- | --- | --- |
| `action` | int | 生命周期；开始/更新分支为 1/2，结束为 3 |
| `navi_turn` | int | 根据图标及地图包名分类的转向值；完整枚举映射尚需对图标分支逐项验证 |
| `remain_distance` | int | 机动提示剩余距离，支持米/公里换算成米 |
| `total_distance` | int | `where` 文本变化时缓存当时的 remain_distance；随后重复发送这个缓存参考值 |
| `road_name` | string | 来自原始 `where` 文本 |
| `turn_icon_data` | byte[] | directionIcon 转换的图像数据 |

`mix_notify_start_navi` 另写 `isNavi:boolean`。**混合回调里的 total_distance 不是独立取得的全程剩余距离。** 当前已核验的 HUD 出口不写 `title1/title2`、剩余秒数、ETA、车道数、推荐车道或车道图；原生 CarLink 出口与此不同。

EasyConn SDK 还定义 `BMapBridge.NavigationInfo.remainDistance/remainTime`、`onLaneInfoUpdate(int,List)`、`ECP_P2C_PHONE_HUDINFO_LANE_GUIDANCE_PICTURE`（`0x20440`）。包内存在这些定义或封装代码，但本次静态索引没有确认 CarWith 主导航业务调用并传出这些数据；`BMapBridgeImpl` 的反射目标不在当前 DEX。它们标为 SDK 能力定义，不作为已接通出口。

2026-11-14另核EasyConn `ECP_P2C_PHONE_HUDINFO`（`0x20110`）：`destinationRemainingDistance:int`
来自`HUDINFO.k`，与`roadRemainingDistance:int`的`HUDINFO.i`分开编码；
未找到目的地距离setter、消息构造或`setHudinfo`的DEX直接调用。
这是专门的目的地剩余距离候选，不能直接用作当前混合HUD字段。
原字节、引用及`TITLE_1/TITLE_2`边界见[全程距离复查](ROUTE_DISTANCE.md)。

### 5.3 音乐、通话、传感器与控制

`NotifyMusicInfo` 的 14 个字段：`artist_name`、`album_name`、`cover_art`、`lyrics`、`playing_times_ms:uint64`、`title`、`author_name`、`writer_name`、`composer_name`、`playing_current_time_ms:int32`、`is_favorite:bool`、`is_playing:bool`、可选 `cover_art_bitmap:bytes`、可选 `id:int32`。两个时间字段的名称明确包含毫秒，但运行时量程没有采样。

混合音乐通道另有 `ICarLifeCastCallback.sendMusicInfo(com.baidu.carlife.mixing.MusicInfo)`、`notifyMusicProgress(long)`、`notifyAudioState(int)`。混淆后的 `MusicInfo` 成员是三项 string、一项 long、两项 int；不能直接假定它等同原生 14 字段模型。

`CallInfo` 定义 `callState`、`number`、`name`、`isIPCall`、`isNeedShowFloatingWindow`、`connectedTime`、`inCallAppId`。`NotifyPhoneState` 定义通话状态、锁屏、微信/QQ 通话、语音助手活跃，以及可选低电量和过热标志。

`SensorIndex` 覆盖 GPS、灯光、陀螺仪、加速度、燃油、挡位、光照、电池；例如 GPS 有 altitude/latitude/longitude、天线状态、PDOP、速度、航向、卫星数、timestamp。输入 Java 模型和 wire schema 的类型可能不同，附录分别列出；单位只采用包内明确注释，不补造坐标/速度缩放规则。

其余结构完整覆盖通知及点击动作、摄像头枚举/预览/拍摄、POI 坐标类型、应用列表/图标/生命周期、显示可见区域、网络分享、文件分享、麦克风与播放器配置、按键和 VR 命令。完整 342 字段与 157 枚举值见 Protobuf 附录。

## 6. Binder、Intent、Content Provider 与 JS 接口

### 6.1 Binder 核心入口

Binder 的 122 个接口包含 Android/MIUI 系统镜像接口与第三方 SDK。CarWith/CarLink/UCar/CarLife/EasyConn 直接相关的接口另标为核心组；完整方法签名和事务号在附录。Binder 方法本身不是 TCP 或 HTTP 接口。

| 接口 | 方法数 | 主要职责 |
| --- | --- | --- |
| `ICarLifeCastManager` | 5 | prepareCast、stopCast、回调和系统音频回调注册、invokeMethod |
| `ICarLifeCastCallback` | 13 | 回调生命周期、音乐信息/进度、音频/按键/触摸监听、invokeMethod |
| `IDataBusService` | 35 | 导航、音乐、电话、状态、应用列表、音视频通道与观察者 |
| `IDataObserver` | 30 | 车端事件与状态回调 |
| `ICarlinkService` | 4 | 连接/投屏框架入口 |
| `IPhoneAudioCast` / `IPhoneAudioCallback` | 16 / 15 | 电话、音乐、麦克风、HFP 等音频控制与回调 |
| `IUCarMapService` / `IUCarMapCallback` | 10 / 5 | 地图导航数据及回调 |
| `IShareService` / `IShareObserver` | 9 / 7 | 文件分享及任务观察 |

`IUCarMapService` 的具体方法：`getValue(int,Bundle):Bundle`、`setValue(int,Bundle)`、`notifyCommuterAddressChanged(boolean,boolean,Bundle)`、`notifyMapUIModeChanged(int,Bundle)`、`notifyNavStatusChanged(boolean,Bundle)`、`notifyStatusChanged(int,Bundle)`、`registerMapCallback(IUCarMapCallback)`、`unregisterMapCallback()`、`removeNavInfo(Bundle)`、`showNavInfo(Bundle,Bundle)`。

仅能从 DEX 恢复方法名、顺序/事务常量与类型；多数参数原名缺失。事务号可通过 `binder_transactions.csv` 与接口所属 `$Stub` 联表，未将未找到的事务号按方法排列猜出。

### 6.2 Intent / Bundle / JSON 键

`key_usage.csv` 列出 2,185 次明确字面量键使用，共 1,137 个不同键，覆盖 Intent、Bundle、JSONObject、Map、SharedPreferences、ContentValues 和 Cursor 列名。每行带方法、指令偏移和实际调用签名。

提取仅追踪直线代码块中的常量寄存器，遇到分支、合流或动态返回时保守清除。因此这是有出处的可恢复集合，不保证所有动态拼接键都已找到；`literal_value` 是静态常量候选，不是运行时数据样本。

其它已核验的混合键：`carlife_dynamic_params` 携带 `carlife_frame:int`；`carlife_music_sample_rate` 返回 `music_sample_rate:int`；部分调用以 `params:string` 传输配置。编码器配置还包含 `level:int`、`i-frame-interval:int`、`profile:int`、`bitrate:int`、`bitrate-mode:int`、`max-fps-to-encoder:float`、`frame-rate:int`、`mode:int`。所有 action 字面量另见 [action_literals.csv](inventory/action_literals.csv)。

### 6.3 Manifest 导出组件和本地 URI

Manifest 共 115 个组件；导出属性与权限按原文件列出：[components.csv](inventory/components.csv)。`exported=true` 仍可能受组件权限、系统签名、绑定逻辑或业务状态限制；`unspecified` 表示未显式声明，未擅自替换成 true/false。

关键入口包括：

- `com.miui.carlink.castfwk.CarlinkService`：显式导出，需要 `miui.carlink.permission.START_CARLINKSERVICE`。
- `com.ucar.map.service.UCarMapService`：action `ucar.service.MAP_SERVICE`，权限 `com.ucar.permission.UCAR_SERVICE`。
- `com.ucar.app.ability.UCarAbilityService`：action `ucar.service.ABILITY_SERVICE`，同上权限。
- `net.easyconn.carman.sdk.DataService`：action `net.easyconn.carman.aidl.remote`，权限 `easyconn.sdk.permission.DATA_SERVICE`。
- `CarlinkInfoDBProvider`：authority `com.miui.carlink.device_list`，权限 `com.miui.carlink.permission.UCAR_SETTINGS_PROVIDER`。
- `DumpLogProvider`：authority `com.miui.carlink.provider.bugreport`，权限 `com.miui.bugreport.permission.DUMP_CACHED_LOG`。

包内还引用百度地图 `content://com.baidu.baidumaps.oemdata.OemContentProvider/common_addr` 与 `/navi_status`、天气、日历、时钟、小爱隐私、网络管理等 Provider URI。URI 字面量能证明引用候选；可用列名、读取权限和真实返回值须结合 Provider 实现或运行时验证。

已提取 7 个 `@JavascriptInterface` 方法，见 [javascript_interfaces.csv](inventory/javascript_interfaces.csv)。这只确认 Java 桥方法定义；注入到网页时使用的 JS 对象名称与实际页面可调用状态未全部确认。

## 7. 配置资源、JNI 和全量清单

### 7.1 JSON、业务类与 SDK 模型

明确的 `SerializedName` 名称共 266 个；883 个混淆后的 Jackson 枚举字段标记没有 JSON 属性名称，单列在 `enum_annotation_markers.csv`，不计入序列化参数。

包内合法 JSON 资源提取 1,128 条去重后的字段路径，保留类型与首个静态值样例。主要有应用市场、应用列表、设备/DPI、语音/VAD/唤醒、快捷指令、设置及通知配置；源文件保存在 `source/assets/`。它们是安装包内配置，不是线上 API 响应。数组使用 `[]` 归一化；同一路径/类型的首个样例不代表全部可能值。

另外提取了 158 个重点业务模型成员及小爱 SDK 的 10,828 个实例模型字段。SDK 模型包含广泛的地图、汽车、媒体、语音和其它业务类型，明确标为“SDK 定义，未确认当前 CarWith 使用”。所有成员仍可在全量字段 CSV 中查到。

### 7.2 原生库和 JNI

25 个原生库覆盖 `libmicastcore.so`、`libgojni.so`、`libECSocksServer.so`、`libtun2socks.so`、`libjadbd.so`、语音库、音频库、Hook/日志与 Android 支持库等。库名、大小、哈希见 `manifest.json.native`。

DEX 中恢复 182 个 native 方法；ARM64 ELF 动态符号表恢复 21,265 条定义的全局/弱导出符号，含大量支持库/C++ 符号，不能将其全部称为业务 API。完整签名与符号地址见 `native_methods.csv`、`native_exports.csv`；`source/*.so.strings.txt` 保存相关可打印字符串。

本轮没有对所有原生函数逐条做 ARM64 反编译，未恢复被去符号、加密或运行时 JNI 注册后才出现的全部语义。ELF 符号地址不是已加载进程地址。

### 7.3 包内嵌套资源

`.rpk` 和 ZIP 嵌套包已列出 321 个内部条目，见 `nested_archive_entries.csv`。本轮未把嵌套 Quick App/二进制资源的全部逻辑当作主 DEX 接口解析。完整顶层目录见 `apk_entries.csv`。

### 7.4 可用性边界与下一步

这份文档可以直接用于字段查找、接口签名核查和后续取证设计。云 API 的线上可用性、设备权限、连接时序、完整账号签名流程、字段量程和运行时枚举仍没有采样。

优先验证点：地图输入的 `TITLE_1/TITLE_2/CROSSING_ICON`；云配置实际应答；车端能力/认证消息；原生导航封包与混合 HUD 同时采样；动态反射实现和 JNI 注册表。获取样本时沿本文的具体方法与偏移定位，避免把“字段存在”误认为“当前通道已经传出”。

复现提取顺序、输出文件和校验结果见 [INVENTORY.md](INVENTORY.md)。原 APK 未修改。
