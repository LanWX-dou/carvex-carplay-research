# 附录：业务模型、序列化名称与配置字段

日期：2026-11-12。这里逐项列出重点业务实例字段、显式序列化名称和 APK JSON 配置路径。类字段属于定义证据；若未同时找到发送/消费代码，不能当作已输出接口。

## 重点业务模型

### com.baidu.carlife.mixing.CastConfig

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | a | int | [] |
| classes.dex | b | int | [] |
| classes.dex | c | int | [] |
| classes.dex | d | android.view.Surface | [] |

### com.baidu.carlife.mixing.MusicInfo

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | a | java.lang.String | [] |
| classes.dex | b | java.lang.String | [] |
| classes.dex | c | java.lang.String | [] |
| classes.dex | d | long | [] |
| classes.dex | e | int | [] |
| classes.dex | f | int | [] |

### com.carwith.common.bean.SettingCategory

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | key | java.lang.String | [] |
| classes.dex | router | java.lang.String | [] |
| classes.dex | spValue | int | [] |
| classes.dex | subTitle | java.lang.String | [] |
| classes.dex | title | java.lang.String | [] |
| classes.dex | type | java.lang.String | [] |
| classes.dex | value | java.util.List | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/List<", "Lcom/carwith/common/bean/SettingCategory;", ">;"]}}] |

### com.carwith.common.bean.a

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | a | android.bluetooth.BluetoothDevice | [] |
| classes.dex | b | int | [] |

### x1.a

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | a | android.content.Context | [] |

### x1.b

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | a | int | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "code"}}] |
| classes.dex | b | java.lang.String | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "message"}}] |
| classes.dex | c | java.lang.String | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "traceId"}}] |
| classes.dex | d | java.lang.Object | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "data"}}, {"type": "Ldalvik/annotation/Signature;", "values": {"value": ["TT;"]}}] |

### x1.c

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | a | java.lang.String | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "resultContent"}}] |

### com.carwith.common.bean.AppBlackItem

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | packageName | java.lang.String | [] |
| classes.dex | versionCodeList | java.util.ArrayList | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/ArrayList<", "Ljava/lang/Long;", ">;"]}}] |

### com.carwith.common.bean.AppWhiteItem

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | appCategory | int | [] |
| classes.dex | appId | int | [] |
| classes.dex | appMode | int | [] |
| classes.dex | appName | java.lang.String | [] |
| classes.dex | applicationType | java.lang.String | [] |
| classes.dex | castType | int | [] |
| classes.dex | packageName | java.lang.String | [] |
| classes.dex | versionCode | long | [] |

### com.carwith.common.bean.CarAppItem

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | carAppMode | int | [] |
| classes.dex | packageName | java.lang.String | [] |

### com.carwith.common.bean.CarModelBlockItem

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | carModelAppTypeList | java.util.List | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/List<", "Lcom/carwith/common/bean/CarAppItem;", ">;"]}}] |
| classes.dex | carModelId | java.lang.String | [] |
| classes.dex | carModelName | java.lang.String | [] |
| classes.dex | carVIN | java.lang.String | [] |
| classes.dex | vehicleManufacturerId | java.lang.String | [] |

### com.carwith.common.bean.CloudControlBean

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | appBlackList | java.util.List | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/List<", "Lcom/carwith/common/bean/AppBlackItem;", ">;"]}}] |
| classes.dex | appWhiteList | java.util.List | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/List<", "Lcom/carwith/common/bean/AppWhiteItem;", ">;"]}}] |
| classes.dex | carAppVersion | java.lang.String | [] |
| classes.dex | carModelBlackList | java.util.List | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/List<", "Lcom/carwith/common/bean/CarModelBlockItem;", ">;"]}}] |
| classes.dex | uCarAppVersion | java.lang.String | [] |

### com.carwith.common.bean.ServerResult

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | code | java.lang.String | [] |
| classes.dex | data | com.carwith.common.bean.CloudControlBean | [] |
| classes.dex | msg | java.lang.String | [] |

### com.carwith.common.bean.SettingsBean$SettingDataBean

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | router | java.lang.String | [] |
| classes.dex | title | java.lang.String | [] |
| classes.dex | type | int | [] |
| classes.dex | value | java.util.List | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/List<", "Lcom/carwith/common/bean/SettingsBean$SettingSecondBean;", ">;"]}}] |

### com.carwith.common.bean.SettingsBean$SettingSecondBean

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | router | java.lang.String | [] |
| classes.dex | subTitle | java.lang.String | [] |
| classes.dex | title | java.lang.String | [] |
| classes.dex | type | int | [] |
| classes.dex | value | java.lang.String | [] |

### com.carwith.common.bean.SettingsBean

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | settingData | java.util.List | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/List<", "Lcom/carwith/common/bean/SettingsBean$SettingDataBean;", ">;"]}}] |

### com.carwith.common.bean.WallpaperResBean$WallpaperCategorysBean$WallpapersBean

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | dark_color | java.lang.String | [] |
| classes.dex | id | java.lang.String | [] |
| classes.dex | light_color | java.lang.String | [] |
| classes.dex | wallpaper_name | java.lang.String | [] |

### com.carwith.common.bean.WallpaperResBean$WallpaperCategorysBean

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | categoryId | java.lang.String | [] |
| classes.dex | categoryNameKey | java.lang.String | [] |
| classes.dex | wallpapers | java.util.List | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/List<", "Lcom/carwith/common/bean/WallpaperResBean$WallpaperCategorysBean$WallpapersBean;", ">;"]}}] |

### com.carwith.common.bean.WallpaperResBean

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes.dex | wallpaperCategorys | java.util.List | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/List<", "Lcom/carwith/common/bean/WallpaperResBean$WallpaperCategorysBean;", ">;"]}}] |

### cb.a

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | long | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "watermark"}}] |
| classes4.dex | b | java.lang.String | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "device_id"}}] |
| classes4.dex | c | cb.c | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "privacy"}}] |
| classes4.dex | d | boolean | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "status"}}] |

### cb.b

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | boolean | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "accredit_switch"}}] |

### cb.c

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | boolean | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "address"}}] |
| classes4.dex | b | boolean | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "smart_travel"}}] |
| classes4.dex | c | boolean | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "simulation"}}] |
| classes4.dex | d | boolean | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "contact"}}] |
| classes4.dex | e | boolean | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "personalize"}}] |
| classes4.dex | f | boolean | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "voice_wakeup"}}] |
| classes4.dex | g | boolean | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "continuous_talk"}}] |
| classes4.dex | h | boolean | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "schedule"}}] |

### cb.d

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | int | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "code"}}] |
| classes4.dex | b | cb.a | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "data"}}] |
| classes4.dex | c | java.lang.String | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "message"}}] |

### cb.e

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | java.util.List | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/List<", "Ljava/lang/String;", ">;"]}}] |

### cb.f

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | java.lang.String | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "request_id"}}] |
| classes4.dex | b | java.lang.String | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "vendor_id"}}] |
| classes4.dex | c | java.util.List | [{"type": "Lcom/google/gson/annotations/SerializedName;", "values": {"value": "speak"}}, {"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/List<", "Ljava/lang/String;", ">;"]}}] |

### com.miui.carlink.databus.p2cdatastructure.MusicInfo

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | java.lang.String | [] |
| classes4.dex | b | java.lang.String | [] |
| classes4.dex | c | java.lang.String | [] |
| classes4.dex | d | java.lang.String | [] |
| classes4.dex | e | long | [] |
| classes4.dex | f | java.lang.String | [] |
| classes4.dex | g | java.lang.String | [] |
| classes4.dex | h | java.lang.String | [] |
| classes4.dex | i | java.lang.String | [] |
| classes4.dex | j | int | [] |
| classes4.dex | k | boolean | [] |
| classes4.dex | l | boolean | [] |
| classes4.dex | m | byte[] | [] |
| classes4.dex | n | int | [] |

### com.miui.carlink.databus.p2cdatastructure.NavigationInfo

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | boolean | [] |
| classes4.dex | b | byte[] | [] |
| classes4.dex | c | java.lang.String | [] |
| classes4.dex | d | java.lang.String | [] |
| classes4.dex | e | java.lang.String | [] |
| classes4.dex | f | java.lang.String | [] |
| classes4.dex | g | java.lang.String | [] |
| classes4.dex | h | java.lang.String | [] |
| classes4.dex | i | int | [] |

### com.miui.carlink.databus.p2cdatastructure.PhoneState

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | com.miui.carlink.databus.proto.UCarProto$CALL_STATE | [] |
| classes4.dex | b | boolean | [] |
| classes4.dex | c | boolean | [] |
| classes4.dex | d | boolean | [] |
| classes4.dex | e | java.util.Optional | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/Optional<", "Ljava/lang/Boolean;", ">;"]}}] |
| classes4.dex | f | java.util.Optional | [{"type": "Ldalvik/annotation/Signature;", "values": {"value": ["Ljava/util/Optional<", "Ljava/lang/Boolean;", ">;"]}}] |

### com.miui.carlink.databus.sensor.AccInfo

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | double | [] |
| classes4.dex | b | double | [] |
| classes4.dex | c | double | [] |
| classes4.dex | d | long | [] |

### com.miui.carlink.databus.sensor.GearInfo

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | com.miui.carlink.databus.proto.UCarProto$GearInfo$GearState | [] |
| classes4.dex | b | int | [] |

### com.miui.carlink.databus.sensor.GpsInfo

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | int | [] |
| classes4.dex | b | int | [] |
| classes4.dex | c | int | [] |
| classes4.dex | d | int | [] |
| classes4.dex | e | int | [] |
| classes4.dex | f | int | [] |
| classes4.dex | g | int | [] |
| classes4.dex | h | int | [] |
| classes4.dex | i | int | [] |
| classes4.dex | j | long | [] |

### com.miui.carlink.databus.sensor.GyroInfo

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | int | [] |
| classes4.dex | b | double | [] |
| classes4.dex | c | double | [] |
| classes4.dex | d | double | [] |
| classes4.dex | e | long | [] |

### com.miui.carlink.databus.sensor.LightSensorInfo

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | double | [] |
| classes4.dex | b | double | [] |
| classes4.dex | c | double | [] |

### com.miui.carlink.databus.sensor.LightsInfo

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | boolean | [] |
| classes4.dex | b | boolean | [] |
| classes4.dex | c | boolean | [] |
| classes4.dex | d | boolean | [] |
| classes4.dex | e | boolean | [] |

### com.miui.carlink.databus.sensor.OilInfo

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes4.dex | a | int | [] |
| classes4.dex | b | int | [] |

### com.ucar.map.UCarMapInfo

| DEX | 成员原名 | 类型 | 注解 |
| --- | --- | --- | --- |
| classes5.dex | crossingIcon | android.graphics.drawable.Icon | [] |
| classes5.dex | directionIcon | android.graphics.drawable.Icon | [] |
| classes5.dex | distance | java.lang.String | [] |
| classes5.dex | distanceUnit | java.lang.String | [] |
| classes5.dex | operation | java.lang.String | [] |
| classes5.dex | pkg | java.lang.String | [] |
| classes5.dex | progress | int | [] |
| classes5.dex | title1 | java.lang.String | [] |
| classes5.dex | title2 | java.lang.String | [] |
| classes5.dex | where | java.lang.String | [] |

## 明确 JSON 名称

共 266 个字段。名称来自 `SerializedName`。另有 883 个无 JSON 名称的枚举字段标记，见机器清单，未纳入本表。

| DEX | 类 | 成员原名 | JSON 名称 | 类型 |
| --- | --- | --- | --- | --- |
| classes.dex | x1.b | a | code | int |
| classes.dex | x1.b | b | message | java.lang.String |
| classes.dex | x1.b | c | traceId | java.lang.String |
| classes.dex | x1.b | d | data | java.lang.Object |
| classes.dex | x1.c | a | resultContent | java.lang.String |
| classes3.dex | com.iccoa.share.transfer.bean.DownloadIntention | a | id | java.lang.String |
| classes3.dex | com.iccoa.share.transfer.bean.DownloadIntention | b | action | long |
| classes3.dex | com.market.sdk.AdsBannerInfo | a | iconUrl | java.lang.String |
| classes3.dex | com.market.sdk.AdsBannerInfo | b | iconUri | android.net.Uri |
| classes3.dex | com.market.sdk.AdsBannerInfo | c | uri | android.net.Uri |
| classes3.dex | com.market.sdk.AppstoreAppInfo | a | appId | java.lang.String |
| classes3.dex | com.market.sdk.AppstoreAppInfo | b | pkgName | java.lang.String |
| classes3.dex | com.market.sdk.AppstoreAppInfo | c | title | java.lang.String |
| classes3.dex | com.market.sdk.AppstoreAppInfo | d | ads | int |
| classes3.dex | com.market.sdk.AppstoreAppInfo | e | digest | java.lang.String |
| classes3.dex | com.market.sdk.AppstoreAppInfo | f | experimentalId | java.lang.String |
| classes3.dex | com.market.sdk.AppstoreAppInfo | g | iconUri | android.net.Uri |
| classes3.dex | com.market.sdk.AppstoreAppInfo | h | iconMask | java.lang.String |
| classes3.dex | com.market.sdk.AppstoreAppInfo | i | appUri | android.net.Uri |
| classes3.dex | com.market.sdk.AppstoreAppInfo | j | mApkBriefDescription | java.lang.String |
| classes3.dex | com.market.sdk.AppstoreAppInfo | k | mApkSize | long |
| classes3.dex | com.market.sdk.AppstoreAppInfo | l | mParameters | java.lang.String |
| classes3.dex | com.market.sdk.AppstoreAppInfo | m | viewMonitorUrls | java.util.List |
| classes3.dex | com.market.sdk.AppstoreAppInfo | n | clickMonitorUrls | java.util.List |
| classes3.dex | com.market.sdk.AppstoreAppInfo | o | impressionMonitorUrls | java.util.List |
| classes3.dex | com.market.sdk.AppstoreAppInfo | p | adInfoPassback | java.lang.String |
| classes3.dex | com.market.sdk.AppstoreAppInfo | q | mFlag | long |
| classes3.dex | com.market.sdk.DesktopRecommendInfo | a | folderId | long |
| classes3.dex | com.market.sdk.DesktopRecommendInfo | b | appInfoList | java.util.List |
| classes3.dex | com.market.sdk.DesktopRecommendInfo | c | bannerList | java.util.List |
| classes3.dex | com.market.sdk.DesktopRecommendInfo | d | backgroundImageUrl | java.lang.String |
| classes3.dex | com.market.sdk.DesktopRecommendInfo | e | description | java.lang.String |
| classes3.dex | com.market.sdk.DesktopRecommendInfo | f | sid | java.lang.String |
| classes3.dex | com.market.sdk.DesktopRecommendInfo | g | cacheTime | long |
| classes4.dex | cb.a | a | watermark | long |
| classes4.dex | cb.a | b | device_id | java.lang.String |
| classes4.dex | cb.a | c | privacy | cb.c |
| classes4.dex | cb.a | d | status | boolean |
| classes4.dex | cb.b | a | accredit_switch | boolean |
| classes4.dex | cb.c | a | address | boolean |
| classes4.dex | cb.c | b | smart_travel | boolean |
| classes4.dex | cb.c | c | simulation | boolean |
| classes4.dex | cb.c | d | contact | boolean |
| classes4.dex | cb.c | e | personalize | boolean |
| classes4.dex | cb.c | f | voice_wakeup | boolean |
| classes4.dex | cb.c | g | continuous_talk | boolean |
| classes4.dex | cb.c | h | schedule | boolean |
| classes4.dex | cb.d | a | code | int |
| classes4.dex | cb.d | b | data | cb.a |
| classes4.dex | cb.d | c | message | java.lang.String |
| classes4.dex | cb.f | a | request_id | java.lang.String |
| classes4.dex | cb.f | b | vendor_id | java.lang.String |
| classes4.dex | cb.f | c | speak | java.util.List |
| classes5.dex | com.ucar.sdk.bean.DeviceInfo | a | id | java.lang.String |
| classes5.dex | com.ucar.sdk.bean.DeviceInfo | b | name | java.lang.String |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | a | id | java.lang.String |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | b | name | java.lang.String |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | c | count | int |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | d | size | long |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | e | thumbUri | java.lang.String |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | f | imageFileCount | int |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | g | videoFileCount | int |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | h | audioFileCount | int |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | i | docFileCount | int |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | j | otherFileCount | int |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | k | imageFileSize | long |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | l | videoFileSize | long |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | m | audioFileSize | long |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | n | docFileSize | long |
| classes5.dex | com.ucar.sdk.bean.TaskInfo | o | otherFileSize | long |
| classes5.dex | com.xiaomi.ai.data.CloudCommonConfig | mDisplayTime | displayTime | int |
| classes5.dex | com.xiaomi.ai.data.CloudCommonConfig | mKeyeventMinTime | keyevent_min_time | int |
| classes5.dex | com.xiaomi.ai.data.CloudCommonConfig | mSimplifyTimeout | simplify_timeout | long |
| classes5.dex | com.xiaomi.ai.data.CloudVadConfig | mCloudVad | cloud_vad | boolean |
| classes5.dex | com.xiaomi.ai.data.FullDuplexConfig | mAecModel | aec_model | java.util.List |
| classes5.dex | com.xiaomi.ai.data.FullDuplexConfig | mBigCardBtTimeout | big_card_bt_timeout | int |
| classes5.dex | com.xiaomi.ai.data.FullDuplexConfig | mBigCardTimeout | big_card_timeout | int |
| classes5.dex | com.xiaomi.ai.data.FullDuplexConfig | mSmallCardBtTimeout | small_card_bt_timeout | int |
| classes5.dex | com.xiaomi.ai.data.FullDuplexConfig | mSmallCardTimeout | small_card_timeout | int |
| classes5.dex | com.xiaomi.ai.data.ModelScore | mModel | model | java.lang.String |
| classes5.dex | com.xiaomi.ai.data.ModelScore | mScore | score | double |
| classes5.dex | com.xiaomi.ai.data.TrainingConfig | mIntroVideo | intro_video | java.lang.String |
| classes5.dex | com.xiaomi.ai.data.VadPrestartConfig | mVadPrestart | vad_prestart | boolean |
| classes5.dex | com.xiaomi.ai.data.VendorTtsConfig | mAsrDetectScore | asr_detect_score | double |
| classes5.dex | com.xiaomi.ai.data.VendorTtsConfig | mModelScores | environment_detect_model_score | java.util.List |
| classes5.dex | com.xiaomi.ai.data.VendorTtsConfig | mTotalFeatureOn | total_feature_on | boolean |
| classes5.dex | com.xiaomi.ai.data.VendorTtsConfig | mVendorTtsModel | vendor_tts_model | java.util.List |
| classes5.dex | com.xiaomi.ai.data.VoiceWaveConfig | mDevices | devices | java.util.List |
| classes5.dex | com.xiaomi.ai.domain.phonecall.common.PhoneCallContent | messageText | message_text | java.lang.String |
| classes5.dex | com.xiaomi.ai.domain.phonecall.common.PhoneCallContent | phoneList | phone_list | java.util.List |
| classes5.dex | com.xiaomi.ai.domain.phonecall.common.PhoneCallContent | toDisplay | to_display | java.lang.String |
| classes5.dex | com.xiaomi.ai.domain.phonecall.common.PhoneCallContent | toSpeak | to_speak | java.lang.String |
| classes5.dex | com.xiaomi.ai.domain.phonecall.contact.PhoneItem | userId | user_id | java.lang.String |
| classes5.dex | kd.a | a | sha1 | java.lang.String |
| classes5.dex | kd.a | b | md5 | java.lang.String |
| classes7.dex | bj.a | a | address | java.lang.String |
| classes7.dex | bj.a | b | lng | double |
| classes7.dex | bj.a | c | city | java.lang.String |
| classes7.dex | bj.a | d | district | java.lang.String |
| classes7.dex | bj.a | e | name | java.lang.String |
| classes7.dex | bj.a | f | lat | double |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AccessibilityInfo | allAppInfo | all_app_info | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AccessibilityInfo | currentPageInfo | current_page_info | com.xiaomi.voiceassistant.fastjson.CurrentPageInfo |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AccessibilityInfo | currentPlayInfo | current_play_info | com.xiaomi.voiceassistant.fastjson.CurrentPlayInfo |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AccessibilityInfo | driveMode | drive_mode | com.xiaomi.voiceassistant.fastjson.DriveMode |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AccessibilityInfo | isLockState | is_lock_state | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AllAppInfoItem | pkgName | pkg_name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AllAppInfoItem | versionCode | version_code | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AllAppInfoItem | versionName | version_name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AppInfo | appInfo | app_info | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AppInfoItem | pkgName | pkg_name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AppVersionsItem | classPatterns | classPatterns | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AppVersionsItem | contentPatterns | contentPatterns | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AppVersionsItem | idPatterns | idPatterns | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AppVersionsItem | textPatterns | textPatterns | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.AppVersionsItem | versionCode | versionCode | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.ClassPatternsItem | className | class_name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.ClassPatternsItem | enabled | enabled | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.ClassPatternsItem | text | text | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | X | x | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | Y | y | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | action | action | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | extra | extra | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | id | id | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | issetBitVector | __isset_bit_vector | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | mClassName | className | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | mIndex | index | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | mPath | path | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | mScrollPath | scrollPath | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | mType | type | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | mWords | words | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | mtoSpeak | toSpeak | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | nodeDesc | nodeDesc | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | packageName | packageName | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | text | text | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Click | waitTime | waitTime | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Client | pageId | pageId | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Client | subType | subType | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Client | toSpeak | toSpeak | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Client | type | type | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.ContentPatternsItem | enabled | enabled | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.ContentPatternsItem | regex | regex | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.CurrentPageInfo | lastSuccessNodeId | last_success_node_id | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.CurrentPageInfo | matchType | match_type | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.CurrentPageInfo | pageId | page_id | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.CurrentPageInfo | pkgName | pkg_name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.CurrentPageInfo | platformVersion | platform_version | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.CurrentPageInfo | versionCode | version_code | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.CurrentPageInfo | versionName | version_name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.CurrentPlayInfo | pkgName | pkg_name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.DeviceConfigInfo | deviceOpen | device_open | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.DeviceConfigInfo | imeiList | imei | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.DriveMode | inDriveMode | in_drive_mode | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.DriveMode | isPassiveMode | is_passive_mode | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.DriveMode | needConfirmEducation | need_confirm_education | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.DriveMode | needFinishEducation | need_finish_education | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.DriveMode | needReplyEducation | need_reply_education | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.DriveMode | promptForBlockedMessageSender | prompt_for_blocked_message_sender | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.DriveMode | reinputButtonClicked | reinput_button_clicked | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.IdPatternsItem | className | class_name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.IdPatternsItem | enabled | enabled | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.IdPatternsItem | text | text | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Intent | type | type | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Intent | uri | uri | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodeExecuteTimeItem | executeTime | execute_time | long |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodeExecuteTimeItem | nodeId | node_id | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodeExecuteTimeItem | waitUserTime | wait_user_time | long |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodeIdInfosItem | appVersions | appVersions | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodeIdInfosItem | pageId | pageId | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodeInfo | nodeInfo | nodeInfo | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodeInfoItem | nodeIdInfos | nodeIdInfos | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodesItem | click | click | com.xiaomi.voiceassistant.fastjson.Click |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodesItem | client | client | com.xiaomi.voiceassistant.fastjson.Client |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodesItem | intent | intent | com.xiaomi.voiceassistant.fastjson.Intent |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodesItem | issetBitVector | __isset_bit_vector | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodesItem | name | name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodesItem | nodeId | nodeId | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.NodesItem | versionCode | versionCode | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | X | x | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | Y | y | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | action | action | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | className | className | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | extra | extra | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | id | id | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | index | index | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | issetBitVector | __isset_bit_vector | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | packageName | packageName | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | path | path | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | text | text | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | type | type | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | waitTime | waitTime | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.Sdk | words | words | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.TextPatternsItem | className | class_name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.TextPatternsItem | enabled | enabled | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.TextPatternsItem | text | text | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.appdownload.Intent | permission | permission | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.appdownload.Intent | pkgName | pkg_name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.appdownload.Intent | type | type | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.appdownload.Intent | uri | uri | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.asrevaluate.AsrEvaluate | result | result | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.asrevaluate.ResultItem | asr | asr | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.asrevaluate.ResultItem | asrFinalTime | asr_final_time | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.asrevaluate.ResultItem | file | file | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.asrevaluate.ResultItem | requestId | request_id | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.asrevaluate.ResultItem | startRequestTime | start_request_time | long |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.asrevaluate.ResultItem | vadEndTime | vad_end_time | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.guide.FirstGuideQueries | autoMic | auto_mic | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.guide.FirstGuideQueries | groupId | group_id | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.guide.FirstGuideQueries | guideTitle | guide_title | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.guide.FirstGuideQueries | queryList | query_list | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.guide.FirstGuideQueries | totalTtsIntroduceEnd | total_tts_introduce_end | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.guide.FirstGuideQueries | totalTtsIntroduceEndError | total_tts_introduce_end_error | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.guide.QueryListItem | matchList | match_list | java.util.List |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.guide.QueryListItem | query | query | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.guide.QueryListItem | queryTts | query_tts | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.guide.QueryListItem | queryTtsWrong | query_tts_wrong | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | albumId | album_id | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | albumName | album_name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | allRate | all_rate | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | artist | artist | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | artistId | artist_id | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | audioId | audio_id | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | copyType | copy_type | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | coverUrl | cover_url | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | cp | cp | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | cpId | cp_id | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | cpSongId | cp_song_id | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | duration | duration | int |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | globalId | global_id | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | id | id | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | isLoadedCover | is_loaded_cover | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | isOriginalSinging | is_original_singing | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | isPayment | payment | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | isVip | is_vip | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | isVisible | is_visible | boolean |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | mid | mid | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | originSong | origin_song | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | refer | refer | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | song | song | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | songRank | song_rank | double |
| classes7.dex | com.xiaomi.voiceassistant.fastjson.music.MusicItem | tags | tags | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.personalInfo.data.loadAddr.ResultItem | a | uid | java.lang.Object |
| classes7.dex | com.xiaomi.voiceassistant.personalInfo.data.loadAddr.ResultItem | b | address | java.lang.Object |
| classes7.dex | com.xiaomi.voiceassistant.personalInfo.data.loadAddr.ResultItem | c | lng | double |
| classes7.dex | com.xiaomi.voiceassistant.personalInfo.data.loadAddr.ResultItem | d | city | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.personalInfo.data.loadAddr.ResultItem | e | district | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.personalInfo.data.loadAddr.ResultItem | f | name | java.lang.String |
| classes7.dex | com.xiaomi.voiceassistant.personalInfo.data.loadAddr.ResultItem | g | lat | double |
| classes7.dex | mj.d | mAiEx | aiEx | java.lang.String |
| classes7.dex | mj.d | mAppRef | appRef | java.lang.String |
| classes7.dex | mj.d | mAppSignature | appSignature | java.lang.String |
| classes7.dex | mj.d | mAutoDownload | autoDownload | boolean |
| classes7.dex | mj.d | mClickMonitorUrls | clickMonitorUrls | java.lang.String[] |
| classes7.dex | mj.d | mEx | ex | java.lang.String |
| classes7.dex | mj.d | mExtChannel | extChannel | java.lang.String |
| classes7.dex | mj.d | mFinishDownloadMonitorUrls | finishDownloadMonitorUrls | java.lang.String[] |
| classes7.dex | mj.d | mFinishInstallMonitorUrls | finishInstallMonitorUrls | java.lang.String[] |
| classes7.dex | mj.d | mIcon | icon | android.graphics.drawable.Drawable |
| classes7.dex | mj.d | mIconUrl | iconUrl | java.lang.String |
| classes7.dex | mj.d | mLabel | label | java.lang.String |
| classes7.dex | mj.d | mLaunchMonitorUrls | launchMonitorUrls | java.lang.String[] |
| classes7.dex | mj.d | mNonce | nonce | java.lang.String |
| classes7.dex | mj.d | mPackageName | packageName | java.lang.String |
| classes7.dex | mj.d | mStartDownloadMonitorUrls | startDownloadMonitorUrls | java.lang.String[] |
| classes7.dex | mj.d | mStartInstallMonitorUrls | startInstallMonitorUrls | java.lang.String[] |
| classes7.dex | mj.d | mViewMonitorUrls | viewMonitorUrls | java.lang.String[] |

## APK 内 JSON 配置字段

共 1,128 条去重路径。类型名为 Python 解析类型：str/string、int/integer、float/number、bool/boolean、NoneType/null、array。静态样例为同路径/类型的第一个值，不代表 API 返回值。

### assets/ReportPrefItem.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.type | int | 0 |
| $.data | str | sdfsdf |
| $.uploadLogContext | bool | True |
| $.requestId | str | sdfsdf |
| $.sessionId | str | sdfsdf |
| $.requestIDSetTime | int | 111111111111111 |
| $.hasUploadCnt | int | 1 |

### assets/ResourceUpdateItem.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.name | str | aaa |
| $.version | int | 1 |
| $.support_app_min_version | int | 1 |
| $.file_size | int | 111111111111111 |
| $.sha1 | str | bf5a8f5c646842fbaf7 |
| $.download_url | str | http://mi.com |

### assets/ai_all_smart_shortcut.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $ | array | — |
| $[].skill_id | str | 216 |
| $[].query | str | 实时肺炎疫情 |
| $[].template | str | — |
| $[].name | str | 实时肺炎疫情 |
| $[].display_name | str | 实时肺炎疫情 |
| $[].brief | str | 最新肺炎疫情实时动态 |
| $[].description | str | 一键查看新型冠状病毒肺炎疫情实时动态  from Tencent |
| $[].icon | str | http://cnbj1.fds.api.xiaomi.com/ai-open-file-service/ai_shortcut/5.0APP/shishifeiyanyiqing.svg |
| $[].icon_border_color | str | #00000000 |
| $[].bg_image | str | — |
| $[].bg_color | str | #f92f2d |
| $[].text_color | str | #ffffff |
| $[].border_color | str | — |
| $[].category | str | 新鲜出炉 |
| $[].speak_enable | bool | True |
| $[].speak_txt_enable | bool | True |
| $[].version | int | 16 |
| $[].minAiVersion | int | 0 |
| $[].autoClose | bool | True |
| $[].ais_min_ver | int | 0 |
| $[].ais_user_type | int | 1 |
| $[].path.node_id | str | 2352 |
| $[].path.params | array | — |
| $[].path.exe_query_template | str | 实时肺炎疫情 |
| $[].path.node_name | str | root |
| $[].path.title_for_sub_nodes | str | — |
| $[].path.sub_nodes | array | — |
| $[].path.sub_nodes[].node_id | str | 2353 |
| $[].path.sub_nodes[].params | array | — |
| $[].path.sub_nodes[].exe_query_template | str | 实时肺炎疫情 |
| $[].path.sub_nodes[].node_name | str | 实时肺炎疫情 |
| $[].path.sub_nodes[].title_for_sub_nodes | str | — |
| $[].path.sub_nodes[].sub_nodes | array | — |
| $[].path.sub_nodes[].always_display | bool | False |
| $[].path.sub_nodes[].intent_uri | str | https://news.qq.com/zt2020/page/feiyan.htm#/area?pool=bj |
| $[].path.sub_nodes[].intent_type | str | activity |
| $[].path.sub_nodes[].package_name | str | com.miui.voiceassist |
| $[].path.sub_nodes[].offline_template_on | bool | False |
| $[].path.sub_nodes[].params[].name | str | nickname |
| $[].path.sub_nodes[].params[].display_name | str | 昵称 |
| $[].path.sub_nodes[].params[].value | str | — |
| $[].path.sub_nodes[].params[].default_value | str | — |
| $[].path.sub_nodes[].params[].sys_var | str | false |
| $[].path.sub_nodes[].params[].widget | str | text |
| $[].path.sub_nodes[].params[].required | str | 0 |
| $[].path.sub_nodes[].ais_code | str | — |
| $[].path.sub_nodes[].sub_nodes[].node_id | str | 2094 |
| $[].path.sub_nodes[].sub_nodes[].params | array | — |
| $[].path.sub_nodes[].sub_nodes[].exe_query_template | str | 我想看央视综合频道 |
| $[].path.sub_nodes[].sub_nodes[].node_name | str | CCTV1 综合 |
| $[].path.sub_nodes[].sub_nodes[].title_for_sub_nodes | str | 123 |
| $[].path.sub_nodes[].sub_nodes[].sub_nodes | array | — |
| $[].path.sub_nodes[].sub_nodes[].always_display | bool | False |
| $[].path.sub_nodes[].sub_nodes[].intent_uri | str | — |
| $[].path.sub_nodes[].sub_nodes[].intent_type | str | — |
| $[].path.sub_nodes[].sub_nodes[].package_name | str | — |
| $[].path.sub_nodes[].sub_nodes[].offline_template_on | bool | False |
| $[].path.params[].name | str | constellation |
| $[].path.params[].display_name | str | 你的星座 |
| $[].path.params[].default_value | str | 白羊座 |
| $[].path.params[].sys_var | str | false |
| $[].path.params[].widget | str | text |
| $[].path.params[].required | str | 1 |
| $[].path.params[].value | str | {"name":"HOME","address":"北京市昌平区霍营街道回龙观东大街240号华龙苑中里","lat":40.084974,"lng":116.37772,"city":"北京城区","district":"昌平区","predicted":false} |

### assets/ai_shortcut.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $ | array | — |
| $[].skill_id | str | 35 |
| $[].name | str | 记个便签 |
| $[].brief | str | 随时记下灵感瞬间 |
| $[].description | str | 一键快速创建新便签，随时记录生活点滴，不错过灵感瞬间 |
| $[].icon | str | — |
| $[].icon_border_color | str | #00000000 |
| $[].bg_image | str | — |
| $[].bg_color | str | #ebad2e |
| $[].text_color | str | #ffffff |
| $[].border_color | str | — |
| $[].speak_enable | bool | False |
| $[].speak_txt_enable | bool | False |
| $[].cover_info.cover_layout_type | int | 0 |
| $[].cover_info.data_type | int | 0 |
| $[].cover_info.cover_data.bg_color | str | #ebad2e |
| $[].cover_info.cover_data.html_text | str | — |
| $[].cover_info.cover_data.icon | str | http://cnbj1.fds.api.xiaomi.com/ai-open-file-service/ai_shortcut/new/bianqian2.png |
| $[].cover_info.cover_data.title | str | 记个便签 |
| $[].cover_info.cover_data.sub_title | str | 随手记录身边事 |
| $[].path.node_id | str | 1946 |
| $[].path.node_name | str | root |
| $[].path.title_for_sub_nodes | str | — |
| $[].path.exe_query_template | str | 新建便签 |
| $[].path.sub_nodes | array | — |
| $[].path.sub_nodes[].exe_query_template | str | 新建便签 |
| $[].path.sub_nodes[].node_name | str | 新建便签 |
| $[].path.sub_nodes[].node_id | str | 1947 |
| $[].path.sub_nodes[].intent_uri | str | intent:#Intent;action=android.intent.action.SEND;type=text/plain;package=com.miui.notes;B.StartActivityWhenLocked=true;S.android.intent.extra.TEXT=;end |
| $[].path.sub_nodes[].intent_type | str | activity |
| $[].path.sub_nodes[].package_name | str | com.miui.notes |
| $[].version | str | 123 |
| $[].path.params | array | — |
| $[].path.params[].name | str | address_home |
| $[].path.params[].display_name | str | 家庭地址 |
| $[].path.params[].value | str | — |
| $[].path.params[].default_value | str | — |
| $[].path.params[].sys_var | bool | True |
| $[].path.params[].widget | str | search_poi |
| $[].path.params[].required | bool | True |
| $[].path.sub_nodes[].params | array | — |
| $[].path.sub_nodes[].params[].name | str | address_company |
| $[].path.sub_nodes[].params[].display_name | str | 公司/学校地址 |
| $[].path.sub_nodes[].params[].value | str | — |
| $[].path.sub_nodes[].params[].default_value | str | — |
| $[].path.sub_nodes[].params[].sys_var | bool | False |
| $[].path.sub_nodes[].params[].widget | str | search_poi |
| $[].path.sub_nodes[].params[].required | bool | True |
| $[].path.sub_nodes[].always_display | bool | True |
| $[].auto_close | bool | False |
| $[].cover_info.layout_type | int | 1 |
| $[].cover_info.expire_time | int | 60 |
| $[].cover_info.cover_data.nodes | array | — |
| $[].cover_info.cover_data.nodes[].title | str | 西瓜味小龙虾 |
| $[].cover_info.cover_data.nodes[].sub_title | str | 5194690热度 |
| $[].cover_info.cover_data.nodes[].name | str | 小米集团 |
| $[].cover_info.cover_data.nodes[].percent | str | -.-% |
| $[].cover_info.cover_data.nodes[].img | str | HK |
| $[].cover_info.cover_data.nodes[].code | str | 01810 |
| $[].cover_info.cover_data.nodes[].value | str | 0.00 |
| $[].path.params[].sys_var | str | false |
| $[].path.params[].widget_config | str | http://test |
| $[].path.params[].required | str | 1 |
| $[].path.params[].defaultValue.code | str | 01810 |
| $[].path.params[].defaultValue.data_type | str | eqty |
| $[].path.params[].defaultValue.market | str | hk |
| $[].path.params[].defaultValue.name | str | 小米集团-W |
| $[].version | int | 18 |
| $[].minAiVersion | int | 0 |
| $[].path.sub_nodes[].params[].sys_var | str | false |
| $[].path.sub_nodes[].params[].required | str | 1 |
| $[].path.sub_nodes[].title_for_sub_nodes | str | — |
| $[].path.sub_nodes[].sub_nodes | array | — |
| $[].path.sub_nodes[].offline_template_on | bool | False |
| $[].cover_info.cover_privacy | bool | True |

### assets/ai_shortcut_headers.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $ | array | — |
| $[].skill_id | str | 32 |
| $[].name | str | 实时天气 |
| $[].brief | str | 当前天气信息，一点即知 |
| $[].description | str | 想知道当前天气情况，就来问小爱“现在天气”吧 |
| $[].icon | str | — |
| $[].icon_border_color | str | #00000000 |
| $[].bg_image | str | — |
| $[].bg_color | str | #33bfd1 |
| $[].text_color | str | #ffffff |
| $[].border_color | str | — |
| $[].speak_enable | bool | False |
| $[].speak_txt_enable | bool | True |
| $[].auto_close | bool | False |
| $[].cover_info.cover_layout_type | int | 0 |
| $[].cover_info.data_type | int | 2 |
| $[].cover_info.cover_data.bg_color | str | #33bfd1 |
| $[].cover_info.cover_data.html_text | str | — |
| $[].cover_info.cover_data.icon | str | http://cnbj1.fds.api.xiaomi.com/ai-open-file-service/ai_shortcut/new/weather/qing.png |
| $[].cover_info.cover_data.title | str | 28<font size='20'>℃</font> |
| $[].cover_info.cover_data.sub_title | str | 空气质量：36 |
| $[].path.node_id | str | 831 |
| $[].path.node_name | str | root |
| $[].path.title_for_sub_nodes | str | — |
| $[].path.exe_query_template | str | 现在天气 |
| $[].path.sub_nodes | array | — |
| $[].path.sub_nodes[].exe_query_template | str | 现在天气 |
| $[].path.sub_nodes[].node_name | str | 现在天气 |
| $[].path.sub_nodes[].node_id | str | 832 |
| $[].version | str | 123 |
| $[].path.sub_nodes[].intent_uri | str | com.miui.hybrid://hybrid.xiaomi.com/app/com.cainiao.guoguoquickapp/?__DSP__=true&__SRC__=%7B%22internal%22%3A%7B%22subScene%22%3A%22aishortcut%22%7D%7D |
| $[].path.sub_nodes[].intent_type | str | activity |
| $[].path.sub_nodes[].package_name | str | com.miui.voiceassist |
| $[].path.sub_nodes[].offline_template_on | int | 1 |

### assets/ai_smart_shortcut.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $ | array | — |
| $[].skill_id | str | 202 |
| $[].query | str | 卡包 |
| $[].template | str | — |
| $[].name | str | 卡包 |
| $[].display_name | str | 卡包 |
| $[].brief | str | 实体卡变身电子卡 |
| $[].description | str | 实体卡变身电子卡 |
| $[].icon | str | http://cnbj1.fds.api.xiaomi.com/ai-open-file-service/ai_shortcut/5.0APP/kabao.svg |
| $[].icon_border_color | str | #00000000 |
| $[].bg_image | str | — |
| $[].bg_color | str | #409af0 |
| $[].text_color | str | #ffffff |
| $[].border_color | str | — |
| $[].category | str | 我的捷径 |
| $[].speak_enable | bool | False |
| $[].speak_txt_enable | bool | False |
| $[].version | int | 9 |
| $[].minAiVersion | int | 0 |
| $[].autoClose | bool | True |
| $[].ais_min_ver | int | 0 |
| $[].ais_user_type | int | 0 |
| $[].path.node_id | str | 2304 |
| $[].path.params | array | — |
| $[].path.exe_query_template | str | 卡包 |
| $[].path.node_name | str | root |
| $[].path.title_for_sub_nodes | str | — |
| $[].path.sub_nodes | array | — |
| $[].path.sub_nodes[].node_id | str | 2305 |
| $[].path.sub_nodes[].params | array | — |
| $[].path.sub_nodes[].exe_query_template | str | 打开门卡 |
| $[].path.sub_nodes[].node_name | str | 门卡 |
| $[].path.sub_nodes[].title_for_sub_nodes | str | — |
| $[].path.sub_nodes[].sub_nodes | array | — |
| $[].path.sub_nodes[].always_display | bool | False |
| $[].path.sub_nodes[].intent_uri | str | intent:#Intent;action=com.miui.intent.action.DOUBLE_CLICK;launchFlags=0x10000000;package=com.miui.tsmclient;i.card_group_id=3;end |
| $[].path.sub_nodes[].intent_type | str | activity |
| $[].path.sub_nodes[].package_name | str | com.miui.tsmclient |
| $[].path.sub_nodes[].offline_template_on | bool | True |
| $[].path.sub_nodes[].ais_code | str | — |

### assets/all_app_info.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.app_info | array | — |
| $.app_info[].pkg_name | str | com.baidu.BaiduMap |

### assets/all_city_info.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.city_info_list | array | — |
| $.city_info_list[].city_name | str | 北京 |
| $.city_info_list[].city_tag | str | 热门 |

### assets/asr_evaluate.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.result | array | — |
| $.result[].file | str | 1.wav |
| $.result[].asr | str | — |
| $.result[].start_request_time | int | 111 |
| $.result[].vad_end_time | str | 111 |
| $.result[].asr_final_time | str | 111 |
| $.result[].request_id | str | 111 |

### assets/camera_intents.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.feature | array | — |
| $.feature[].featureCode | str | take_photo_front_outside_3s |
| $.feature[].name | str | 相机外倒计时3s自拍 |
| $.feature[].intents | array | — |
| $.feature[].intents[] | str | intent:#Intent;action=android.media.action.XIAOAI_CONTROL;package=com.android.camera;component=com.android.camera/.Camera;i.android.intent.extras.CAMERA_MODULE=164;i.android.intent.extras.COUNT_DOWN_TIME=3;i.android.intent.extras.MIUI_CAMERA_FACING=1 |
| $.feature[].intent_type | str | activity |

### assets/circle.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.nodes | array | — |
| $.nodes[].sdk.index | int | 0 |
| $.nodes[].sdk.packageName | str | — |
| $.nodes[].sdk.action | str | openintent |
| $.nodes[].sdk.id | str | — |
| $.nodes[].sdk.type | str | — |
| $.nodes[].sdk.intent | str | — |
| $.nodes[].sdk.className | str | — |
| $.nodes[].sdk.words | str | — |
| $.nodes[].sdk.text | str | — |
| $.nodes[].sdk.path | str | — |
| $.nodes[].sdk.x1 | str | — |
| $.nodes[].sdk.x2 | str | — |
| $.nodes[].sdk.y1 | str | — |
| $.nodes[].sdk.y2 | str | — |
| $.nodes[].sdk.extra | str | — |
| $.nodes[].sdk.waitTime | int | 0 |
| $.nodes[].sdk.__isset_bit_vector | array | — |
| $.nodes[].sdk.__isset_bit_vector[] | int | 1 |
| $.nodes[].client.intent_params.packageName | str | com.tencent.mm |
| $.nodes[].client.intent_params.className | str | com.tencent.mm.ui.tools.ShareToTimeLineUI |
| $.nodes[].client.intent_params.type | str | image/* |
| $.nodes[].client.intent_params.action | str | android.intent.action.SEND_MULTIPLE |
| $.nodes[].client.intent_params.intentType | str | photoPicker |
| $.nodes[].client.intent_params.extraInfo | int | 3 |
| $.nodes[].client.intent_params.extraText | str | 我今天很开心 |
| $.nodes[].toSpeak | str | 在搜索框里输入关键字 |
| $.nodes[].version | str | 6.5.22 |

### assets/cloud_vad_config.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.cloud_vad | bool | True |

### assets/com.qiyi.video.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.nodeInfo | array | — |
| $.nodeInfo[].nodeIdInfos | array | — |
| $.nodeInfo[].nodeIdInfos[].pageId | str | qiyi_have_progress_bar |
| $.nodeInfo[].nodeIdInfos[].appVersions | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].versionCode | str | 146 |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].text | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].text | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].text | str | com.qiyi.video:id/btn_pause |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns[].regex | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns[].enabled | str | — |

### assets/com.tencent.mm.config.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.nodeInfo | array | — |
| $.nodeInfo[].nodeIdInfos | array | — |
| $.nodeInfo[].nodeIdInfos[].pageId | str | weixin_video_chat_answer_or_hangup |
| $.nodeInfo[].nodeIdInfos[].appVersions | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].versionCode | str | 1160 |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].text | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].text | str | 接听 |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].text | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns[].regex | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns[].enabled | str | — |

### assets/com.tencent.mm.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.nodeInfo | array | — |
| $.nodeInfo[].nodeIdInfos | array | — |
| $.nodeInfo[].nodeIdInfos[].pageId | str | weixin_video_chat_answer_or_hangup |
| $.nodeInfo[].nodeIdInfos[].appVersions | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].versionCode | str | 1160 |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].text | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].text | str | 接听 |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].text | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns[].regex | str | 接听 |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns[].enabled | str | — |

### assets/com.tencent.open.config.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.Common_ta_enable | int | 1 |
| $.Common_frequency | int | 24 |

### assets/com.tencent.qqlive.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.nodeInfo | array | — |
| $.nodeInfo[].nodeIdInfos | array | — |
| $.nodeInfo[].nodeIdInfos[].pageId | str | qqlive_have_progress_bar |
| $.nodeInfo[].nodeIdInfos[].appVersions | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].versionCode | str | 146 |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].text | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].text | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].text | str | com.tencent.qqlive:id/b2c |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns[].regex | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns[].enabled | str | — |

### assets/com.youku.phone.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.nodeInfo | array | — |
| $.nodeInfo[].nodeIdInfos | array | — |
| $.nodeInfo[].nodeIdInfos[].pageId | str | youku_have_progress_bar |
| $.nodeInfo[].nodeIdInfos[].appVersions | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].versionCode | str | 146 |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].text | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].classPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].text | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].textPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].text | str | com.youku.phone:id/plugin_small_play_control_btn |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].class_name | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].idPatterns[].enabled | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns | array | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns[].regex | str | — |
| $.nodeInfo[].nodeIdInfos[].appVersions[].contentPatterns[].enabled | str | — |

### assets/context.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.accessibility_info.current_play_info.pkg_name | str | com.miui.player |
| $.accessibility_info.is_lock_state | bool | False |
| $.accessibility_info.open_smart_app | bool | True |
| $.accessibility_info.white_list_user | bool | True |
| $.accessibility_info.current_page_info.pkg_name | str | com.tencent.mm |
| $.accessibility_info.current_page_info.version_code | int | 200 |
| $.accessibility_info.current_page_info.version_name | str | 2.0.0 |
| $.accessibility_info.current_page_info.page_id | str | weixin_1 |
| $.accessibility_info.all_app_info | array | — |
| $.accessibility_info.all_app_info[].pkg_name | str | com.tencent.mm |
| $.accessibility_info.all_app_info[].version_code | int | 200 |
| $.accessibility_info.all_app_info[].version_name | str | 2.0.0 |

### assets/device_config.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.imei | array | — |
| $.imei[] | str | 867305032827284 |
| $.device_open | bool | False |

### assets/ec_dpi.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.29610 | int | 200 |
| $.349 | int | 200 |
| $.44502 | int | 200 |

### assets/first_guide_queries.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.guide_title | str | Hi, 我是小爱，很高兴见到你<br>请试着对我说： |
| $.total_tts_introduce_end | str | 好棒，你已经学会了小爱同学最实用的三个技能，希望以后多和小爱聊聊发现更多新功能。 |
| $.total_tts_introduce_end_error | str | 好像没说对，我知道你已经学会了，希望以后多和我聊聊天，发现更过功能。 |
| $.auto_mic | bool | True |
| $.group_id | str | default |
| $.query_list | array | — |
| $.query_list[].query | str | 最近的假期还有几天 |
| $.query_list[].query_tts | str | 你好，我是小爱同学，你的人工智能助理，想要和我说话，可以先点击左下角的小球，然后对我说最近的假期还有几天 |
| $.query_list[].match_list | array | — |
| $.query_list[].match_list[] | str | 最近的假期还有几天 |
| $.query_list[].query_tts_wrong | str | 好像没说对，不过我们继续吧，那么想第一时间了解天气情况，试试对我说今天天气 |

### assets/full_duplex_config.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.aec_model | array | — |
| $.aec_model[] | str | crux |
| $.small_card_timeout | int | 120 |
| $.big_card_timeout | int | 30 |
| $.small_card_bt_timeout | int | 5 |
| $.big_card_bt_timeout | int | 5 |

### assets/main_ai.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.status.code | int | 200 |
| $.status.error_type | str | OK |
| $.data | array | — |
| $.data[].unitId | str | 669629119620715520 |
| $.data[].unitType | str | scene |
| $.data[].name | str | 场景-春天 |
| $.data[].isWhiteList | int | -1 |
| $.data[].scene.bubbleText | array | — |
| $.data[].scene.bubbleText[] | str | 宝贝，春天来了哦😊 |
| $.data[].scene.cards | array | — |
| $.data[].scene.cards[].cardId | str | 669617643514234880 |
| $.data[].scene.cards[].cardType | str | singleBig |
| $.data[].scene.cards[].template | str | skill |
| $.data[].scene.cards[].title | str | 春天吃什么养生 |
| $.data[].scene.cards[].subtitle | str | 健康 |
| $.data[].scene.cards[].describe | str | 有41万人在说 |
| $.data[].scene.cards[].img | str | https://file.xiaomixiaoai.com/cache/anonymous/file/8f1fc3f4ac01800f3b5ece7c |
| $.data[].scene.cards[].bgColorStart | str | — |
| $.data[].scene.cards[].bgColorEnd | str | — |
| $.data[].scene.cards[].clickEvent.event | str | query |
| $.data[].scene.cards[].clickEvent.query | str | 春天吃什么养生 |
| $.data[].scene.cards[].clickEvent.isAutoPlay | bool | False |
| $.data[].scene.cards[].icon | str | http://cnbj1.fds.api.xiaomi.com/ai-open-file-service/ai_shortcut/5.0APP/widget/huangli1.png |
| $.data[].scene.cards[].bgImg | str | http://cnbj1.fds.api.xiaomi.com/ai-open-file-service/ai_shortcut/5.0APP/widget/huangli1.png |
| $.data[].scene.cards[].widgetInfo.calendar.chineseCalendarDate | str | 四月十三 |
| $.data[].scene.cards[].widgetInfo.calendar.calendarDate | int | 24 |
| $.data[].scene.cards[].widgetInfo.calendar.good | str | 沐浴 扫舍 余事勿取 |
| $.data[].scene.cards[].widgetInfo.calendar.bad | str | 斋醮 开市 嫁娶 作灶 |
| $.data[].scene.cards[].widgetInfo.holiday.date | str | 6月14日 |
| $.data[].scene.cards[].widgetInfo.holiday.days | str | 26 |
| $.data[].scene.cards[].widgetInfo.holiday.holidayName | str | 端午节 |
| $.data[].scene.cards[].foldCard.delay | int | 4000 |
| $.data[].scene.cards[].foldCard.cp | str | 知乎 |
| $.data[].scene.cards[].foldCard.cardList | array | — |
| $.data[].scene.cards[].foldCard.cardList[].cardId | str | BrXwcE |
| $.data[].scene.cards[].foldCard.cardList[].title | str | 0.考研一定要去图书馆或者考研教室吗？ |
| $.data[].scene.cards[].foldCard.cardList[].subtitle | str | 知乎问答 |
| $.data[].scene.cards[].foldCard.cardList[].hitCount | int | 660000 |
| $.data[].scene.cards[].foldCard.cardList[].cpName | str | zhihu |
| $.data[].scene.cards[].foldCard.cardList[].cpLogo | str | https://cdn.cnbj1.fds.api.mi-img.com/ai-hot-list/square_zhihu.png |
| $.data[].scene.cards[].foldCard.cardList[].img | str | https://pic3.zhimg.com/50/v2-168c1bc4a584d01a05aebdc66ed52682_b.jpg |
| $.data[].scene.cards[].foldCard.cardList[].icon | NoneType | None |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.event | str | deepLink |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.deepLink.webUrl | str | https://www.zhihu.com/question/314239506?utm_medium=partner&utm_source=xiaomi_search |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.deepLink.packageName | str | com.zhihu.android |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.deepLink.deepLinkUri | str | zhihu://question/314239506?utm_medium=partner&utm_source=xiaomi_search |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.isAutoPlay | bool | False |
| $.data[].scene.cards[].foldCard.cardList[].isEntrance | bool | True |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.intent | str | intent://i.xiaomixiaoai.com/h5/ai-ak-fe/#/hotspots?cp=zhihu&from=foldCard/#Intent;scheme=https;launchFlags=0x10000000;component=com.miui.voiceassist/com.xiaomi.voiceassistant.webview.AiWebActivity;S.webFullScreen=true;end |
| $.data[].dialog.question.questionId | str | 650750447228815360 |
| $.data[].dialog.question.questionType | str | nickname |
| $.data[].dialog.question.questionName | str | 昵称 |
| $.data[].dialog.question.text | array | — |
| $.data[].dialog.question.text[] | str | 想知道...我要怎么称呼你呀？ |
| $.data[].dialog.answer | array | — |
| $.data[].dialog.answer[].inputType | str | TEXT_INPUT |
| $.data[].dialog.answer[].label | str | 我叫 |
| $.data[].scene.cards[].clickEvent.instruction | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].header.namespace | str | Template |
| $.data[].scene.cards[].clickEvent.instruction[].header.name | str | Music |
| $.data[].scene.cards[].clickEvent.instruction[].header.id | str | f4c354387f7140f8a385d70602de8b63 |
| $.data[].scene.cards[].clickEvent.instruction[].header.dialog_id | str | 73ebaf6b3d6e4f36966fb709e618a8b7 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].provider.name | str | miui |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].provider.logo.description | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].provider.logo.sources | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].provider.logo.sources[].url | str | http://t2.a.market.xiaomi.com/download/AppStore/AppStore/04a825e922614e3efeba487f86c77bb97cc4339c9 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].auto_play_len | int | 0 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].audio_items | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].audio_items[].audio_id | str | 45295693 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].audio_items[].audio_name | str | 雨爱 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].audio_items[].artist_name | str | 杨丞琳 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].audio_items[].artist_id | int | 0 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].audio_items[].album_name | str | 雨爱 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].audio_items[].album_id | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].audio_items[].cover.description | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].audio_items[].cover.sources | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].audio_items[].cover.sources[].url | str | http://t10.market.xiaomi.com/thumbnail/webp/w0/MusicServer/0d1e8a5f41f5946860f973295dbd557fac2a79646/webp.webp |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].audio_items[].controls | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].app.app.name | str | 音乐 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].app.app.pkg_name | str | com.miui.player |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].app.app.slogan | str | 海量曲库众星云集，你爱听的这都有 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].app.app.tag | str | 影音视听 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].app.app.icon.description | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].app.app.icon.sources | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].app.app.icon.sources[].url | str | http://t2.a.market.xiaomi.com/download/AppStore/AppStore/04a825e922614e3efeba487f86c77bb97cc4339c9 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].app.app.rating_score | float | 1.7999999523162842 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].app.control.type | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].app.control.name | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].skill_icon.description | str | 音乐 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].skill_icon.sources | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.group[].skill_icon.sources[].url | str | http://t2.a.market.xiaomi.com/download/AppStore/AppStore/04a825e922614e3efeba487f86c77bb97cc4339c9 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.loop_mode | str | LIST |
| $.data[].scene.cards[].clickEvent.instruction[].payload.title.main_title | str | 为您播放 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.title.sub_title | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.query_type | str | SONG_SEARCH |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.type | str | ACTIVITY |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.pkg_name | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.uri | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.grade | str | BEST |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.cp_enter_intent | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.cp_enter_intent[] | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.cp_enter_intent[][].cp_name | str | miui |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.cp_enter_intent[][].intent | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.cp_enter_intent[][].pkg | str | com.miui.player |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.common_func | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.common_func[] | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.common_func[][] | bool | False |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.with_best_version | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.with_best_version[] | bool | False |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.min_fold | int | 3 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.fold_num | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.fold_num[] | int | 3 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.full_screen.task | str | 73ebaf6b3d6e4f36966fb709e618a8b7 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.display.display_mode | str | SMALL |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items[].audio_id | str | 45295693 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items[].audio_name | str | 雨爱 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items[].artist_name | str | 杨丞琳 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items[].artist_id | str | 0 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items[].album_name | str | 雨爱 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items[].album_id | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.name | str | 音乐 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.pkg_name | str | com.miui.player |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.slogan | str | 海量曲库众星云集，你爱听的这都有 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.tag | str | 影音视听 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.icon.description | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.icon.sources | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.icon.sources[].url | str | http://t2.a.market.xiaomi.com/download/AppStore/AppStore/04a825e922614e3efeba487f86c77bb97cc4339c9 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.rating_score | float | 1.7999999523162842 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.play_length | int | 1 |
| $.data[].scene.cards[].widgetInfo.musicRecommendation.coverImage | array | — |
| $.data[].scene.cards[].widgetInfo.musicRecommendation.coverImage[] | str | http://y.gtimg.cn/music/photo_new/T002R500x500M000001tTNk21VYQji_1.jpg |
| $.data[].dialog.answer[].intentLink | str | intent://i.xiaomixiaoai.com/h5/ai-personal-info-fe/#/setAnniversary?mode=add/#Intent;scheme=https;launchFlags=0x10000000;component=com.miui.voiceassist/com.xiaomi.voiceassistant.webview.AiWebActivity;S.webFullScreen=true;end |
| $.data[].scene.cards[].clickEvent.intent | str | intent:#Intent;action=com.miui.voiceassist.ACTION_CHECK_LOGIN;launchFlags=0x10000000;component=com.miui.voiceassist/com.xiaomi.voiceassistant.personalInfo.CheckLoginActivity;S.intentUri=intent%3a%2f%2faiweb%3furl%3dhttps%253a%252f%252fi-preview.xiaom |
| $.data[].scene.cards[].widgetInfo.constellation.rate | int | 4 |
| $.data[].scene.cards[].widgetInfo.constellation.desc | str | 点击先设置一下你的生日吧！让小爱更了解你哦～ |
| $.data[].scene.cards[].widgetInfo.constellation.isDefault | bool | True |
| $.data[].scene.cards[].widgetInfo.weather.temperature | str | 20 |
| $.data[].scene.cards[].widgetInfo.weather.quality | str | 优 |
| $.data[].scene.cards[].foldCard.cardList[].song.artist | str | 杨丞琳 |
| $.data[].scene.cards[].foldCard.cardList[].song.songName | str | 雨爱 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].header.namespace | str | Template |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].header.name | str | Music |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].header.id | str | f31be5e176964be89fe9e28de599ddce |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].header.dialog_id | str | 6e9264a942514039afeae151743999fe |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].provider.name | str | miui |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].provider.logo.description | str | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].provider.logo.sources | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].provider.logo.sources[].url | str | http://t2.a.market.xiaomi.com/download/AppStore/AppStore/04a825e922614e3efeba487f86c77bb97cc4339c9 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].auto_play_len | int | 0 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].audio_items | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].audio_items[].audio_id | str | 45295693 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].audio_items[].audio_name | str | 雨爱 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].audio_items[].artist_name | str | 杨丞琳 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].audio_items[].artist_id | int | 0 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].audio_items[].album_name | str | 雨爱 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].audio_items[].album_id | str | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].audio_items[].cover.description | str | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].audio_items[].cover.sources | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].audio_items[].cover.sources[].url | str | http://t10.market.xiaomi.com/thumbnail/webp/w0/MusicServer/0d1e8a5f41f5946860f973295dbd557fac2a79646/webp.webp |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].audio_items[].controls | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].app.app.name | str | 音乐 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].app.app.pkg_name | str | com.miui.player |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].app.app.slogan | str | 海量曲库众星云集，你爱听的这都有 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].app.app.tag | str | 影音视听 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].app.app.icon.description | str | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].app.app.icon.sources | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].app.app.icon.sources[].url | str | http://t2.a.market.xiaomi.com/download/AppStore/AppStore/04a825e922614e3efeba487f86c77bb97cc4339c9 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].app.app.rating_score | float | 1.7999999523162842 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].app.control.type | str | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].app.control.name | str | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].skill_icon.description | str | 音乐 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].skill_icon.sources | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.group[].skill_icon.sources[].url | str | http://t2.a.market.xiaomi.com/download/AppStore/AppStore/04a825e922614e3efeba487f86c77bb97cc4339c9 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.loop_mode | str | LIST |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.title.main_title | str | 为您播放 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.title.sub_title | str | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.query_type | str | SONG_SEARCH |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.type | str | ACTIVITY |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.pkg_name | str | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.uri | str | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.grade | str | BEST |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.cp_enter_intent | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.cp_enter_intent[] | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.cp_enter_intent[][].cp_name | str | miui |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.cp_enter_intent[][].intent | str | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.cp_enter_intent[][].pkg | str | com.miui.player |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.common_func | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.common_func[] | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.common_func[][] | bool | False |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.with_best_version | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.with_best_version[] | bool | False |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.min_fold | int | 3 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.fold_num | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.action.intent.params.fold_num[] | int | 3 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.full_screen.task | str | 6e9264a942514039afeae151743999fe |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.display.display_mode | str | SMALL |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.audio_items | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.audio_items[].audio_id | str | 45295693 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.audio_items[].audio_name | str | 雨爱 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.audio_items[].artist_name | str | 杨丞琳 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.audio_items[].artist_id | str | 0 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.audio_items[].album_name | str | 雨爱 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.audio_items[].album_id | str | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.app.name | str | 音乐 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.app.pkg_name | str | com.miui.player |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.app.slogan | str | 海量曲库众星云集，你爱听的这都有 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.app.tag | str | 影音视听 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.app.icon.description | str | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.app.icon.sources | array | — |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.app.icon.sources[].url | str | http://t2.a.market.xiaomi.com/download/AppStore/AppStore/04a825e922614e3efeba487f86c77bb97cc4339c9 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.app.rating_score | float | 1.7999999523162842 |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.instruction[].payload.play_length | int | 1 |
| $.data[].scene.cards[].foldCard.cardList[].icon | str | https://cdn.cnbj1.fds.api.mi-img.com/function-guide-icons/boiling.png |
| $.data[].scene.cards[].foldCard.cardList[].clickEvent.query | str | 放假还有多少天 |
| $.timeStamp | int | 1618487519027 |
| $.requestId | str | 847ce28686a748368800329818eadcd1 |

### assets/market.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $ | array | — |
| $[].mAuthor | str | 咪咕音乐有限公司 |
| $[].mDeepLink | str | mimarket://details?startDownload=true&detailStyle=5&sign=DuWGnRaiJXDmgHnikuKY5XPvIanU4OZSKsVJgUtjlNTjsWGz0dOf%2BYqiptXwQItrAvxk3uW%2BWl63%0D%0AZKiZIkJvMPxAEQpVy1DfzSiTUQz3qUpX0OmwaKBjetctAaZ%2FpZ9RYjjG6g0z7aNMPixkboAL9YsT%0D%0A6ZvqeabU%2BIwtImi3mII%3 |
| $[].mIcon | str | http://fgb0.market.xiaomi.com/download/AppStore/0767a6f4350ef48cdb9af14b8fe0978b4dc702cb1 |
| $[].mId | str | cmccwm.mobilemusic |
| $[].mIntroduce.briefShow | str | 千万正版曲库，5G至臻音质 |
| $[].mIntroduce.changeLog | str | 优化多项细节，体验更流畅。 |
| $[].mIntroduce.introduction | str | 【千万曲库】新歌实时发布，原创新歌、影视新碟、综艺新歌应有尽有，给你畅听体验！<br>【臻3D】至臻3D立体环绕，给你超凡听歌新体验，好听不止于此！<br>【极光音效】独享「HiFi房间」「纯净ACG」「动感电音」等音效，为您带来更出色的音乐体验，沉浸“响”受音乐～<br>【音乐电台】YOU乐电台，发掘惊喜之声。一样的音乐，不一样的玩法，更多精彩不容错过！<br>【个性推荐】“我的”瀑布流式个性化推荐，下拉看见更多精彩，大数据智能推荐，量身定制专属于你的私人音乐！ <br>【视频彩铃】热门影视片段、爱豆全新MV，让通话等待“ |
| $[].mIntroduce.publisherName | str | 咪咕音乐有限公司 |
| $[].mIntroduce.updateTime | int | 1717659481617 |
| $[].mIntroduce.versionName | str | 7.41.11 |
| $[].mName | str | 咪咕音乐-让音乐更有趣 |
| $[].mPermissionUrl | str | https://app.market.xiaomi.com/hd/apm-h5-cdn/cdn-app-permission.html?urlKey=app_permission_h5_cdn&packageName=cmccwm.mobilemusic |
| $[].mPrivacyUrl | str | https://passport.migu.cn/portal/privacy/appprotocol?sourceid=220024 |
| $[].mVersion | str | 7.41.11 |

### assets/notification_test.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.msgType | str | IOT_REMINDER |
| $.msgSubType | str | SUB_IOT_TEMPERATURE |
| $.icon | str | https://cdn.cnbj1.fds.api.mi-img.com/xiaoailite-ios/XiaoAiSuggestion/env.png |
| $.isGeneralLayout | bool | False |
| $.msgSendTimestamp | int | 1591181058303 |
| $.msgReadTimestamp | int | 0 |
| $.msgExpectSendTimestamp | int | 0 |
| $.msgExpirationSecond | int | 1800 |
| $.msgId | str | 24c57098e2fe44b3881c66606f26600b |
| $.payload | array | — |
| $.payload[].iotCard.iotType | str | TEMPERATURE_HIGH |
| $.payload[].iotCard.title | str | 外面34°C，开制冷吧？ |
| $.payload[].iotCard.devices | array | — |
| $.payload[].iotCard.devices[].deviceIcon | str | https://file.xiaomixiaoai.com/anonymous/file/816fe2d63800400f92e40fc5 |
| $.payload[].iotCard.devices[].deviceName | str | 卧室空调 |
| $.payload[].iotCard.devices[].room | str | 卧室 |
| $.payload[].iotCard.devices[].totalDeviceCount | int | 1 |
| $.payload[].iotCard.devices[].description | str | 卧室 |
| $.payload[].iotCard.devices[].openButton.text | str | 打开设备 |
| $.payload[].iotCard.devices[].openButton.type | str | URL |
| $.payload[].iotCard.devices[].openButton.action | str | NONE |
| $.payload[].iotCard.devices[].openButton.value | str | https://preview4test-api.ai.xiaomi.com/ext/setproperty |
| $.payload[].iotCard.devices[].openButton.icon | str | — |
| $.payload[].iotCard.devices[].openButton.params.control_data | str | [{"setdata":{"properties":[{"pid":"urn:miot-spec-v2:device:air-conditioner:0000A004:lumi-v2:1.2.1","value":true},{"pid":"urn:miot-spec-v2:device:air-conditioner:0000A004:lumi-v2:1.2.1","value":true}],"sort":{}},"devtypenames":[],"userinfo":{"id":"120 |
| $.payload[].iotCard.devices[].openButton.params.method | str | POST |
| $.payload[].iotCard.cardButton.text | str | — |
| $.payload[].iotCard.cardButton.type | str | INTENT |
| $.payload[].iotCard.cardButton.action | str | NONE |
| $.payload[].iotCard.cardButton.value | str | intent://home.mi.com/device/lumi.acpartner.v3/?did=83812480#Intent;scheme=mihome;end |
| $.payload[].iotCard.cardButton.icon | str | https://cdn.cnbj1.fds.api.mi-img.com/xiaoailite-ios/XiaoAiSuggestion/env.png |
| $.payload[].iotCard.cardButton.params.intentType | str | ACTIVITY |
| $.payload[].iotCard.cardButton.params.minVersion | str | 305011000 |
| $.payload[].iotCard.cardButton.params.pkgName | str | com.xiaomi.smarthome |
| $.debugInfo | str | — |
| $.notify.title | str | 外面34°C，开制冷吧？ |
| $.notify.desc | str | — |
| $.notify.body | str | 卧室空调 \| 卧室 |

### assets/offline_recommend_conf.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.guide_queries | array | — |
| $.guide_queries[].exe_pkg_name | str | — |
| $.guide_queries[].min_version | int | 0 |
| $.guide_queries[].network_status | str | wifi_or_mobile_network |
| $.guide_queries[].query | str | 最新电影 |
| $.guide_queries[].scenes | array | — |
| $.guide_queries[].scenes[] | str | com.miui.home |
| $.guide_queries[].send_query | str | 最新电影 |
| $.guide_queries[].time | array | — |
| $.guide_queries[].time[] | str | 00-23 |
| $.guide_queries[].weekday | array | — |
| $.guide_queries[].weekday[] | str | 1-7 |
| $.max_wait_time | int | 300 |

### assets/operation_guide.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.oneDayLimit | int | 1 |
| $.guide | array | — |
| $.guide[].event | str | slidingUp |
| $.guide[].showCount | int | 2 |
| $.guide[].allLimit | int | 2 |
| $.guide[].activeDisappear | int | 7 |
| $.guide[].passiveDisappear | int | 30 |
| $.guide[].toast | str | 向上轻推，小爱同学都在这里 |

### assets/preload_offline_ai.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.status.code | int | 200 |
| $.status.error_type | str | OK |
| $.data | array | — |
| $.data[].unitId | str | 703558010613535744 |
| $.data[].unitType | str | scene |
| $.data[].name | str | 兜底抽屉1 |
| $.data[].isWhiteList | int | 1 |
| $.data[].scene.bubbleText | array | — |
| $.data[].scene.bubbleText[] | str | 说来，我会的东西可多了，来试试 |
| $.data[].scene.cards | array | — |
| $.data[].scene.cards[].cardId | str | 645590220040837120 |
| $.data[].scene.cards[].cardType | str | singleBig |
| $.data[].scene.cards[].template | str | skill |
| $.data[].scene.cards[].title | str | 历史上的今天 |
| $.data[].scene.cards[].subtitle | str | 百科 |
| $.data[].scene.cards[].describe | str | 有42万人在说 |
| $.data[].scene.cards[].img | str | https://file.xiaomixiaoai.com/cache/anonymous/file/9591a6a5b001c00f2b192516 |
| $.data[].scene.cards[].bgColorStart | str | — |
| $.data[].scene.cards[].bgColorEnd | str | — |
| $.data[].scene.cards[].clickEvent.event | str | query |
| $.data[].scene.cards[].clickEvent.query | str | 历史上的今天 |
| $.data[].scene.cards[].clickEvent.isAutoPlay | bool | False |
| $.data[].scene.cards[].bgImg | str | https://file.xiaomixiaoai.com/cache/anonymous/file/9742bb7aa401400f87db3914 |
| $.timeStamp | int | 1618487519027 |
| $.requestId | str | 847ce28686a748368800329818eadcd1 |

### assets/record_audio_upload_config.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.record_audio_upload | bool | False |

### assets/redpacket.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.nodes | array | — |
| $.nodes[].click.index | int | 0 |
| $.nodes[].click.packageName | str | com.tencent.mm |
| $.nodes[].click.action | str | openintent |
| $.nodes[].click.id | str | — |
| $.nodes[].click.type | str | — |
| $.nodes[].click.className | str | com.tencent.mm.ui.LauncherUI |
| $.nodes[].click.words | str | — |
| $.nodes[].click.text | str | — |
| $.nodes[].click.path | str | — |
| $.nodes[].click.scrollPath | str | — |
| $.nodes[].click.x | str | — |
| $.nodes[].click.y | str | — |
| $.nodes[].click.waitTime | int | 0 |
| $.nodes[].click.extra | str | — |
| $.nodes[].click.toSpeak | str | 我小爱已用尽洪荒之力 |
| $.nodes[].client.type | str | — |
| $.nodes[].client.subType | str | — |
| $.nodes[].client.pageId | str | — |
| $.nodes[].client.toSpeak | str | — |
| $.nodes[].intent.type | str | — |
| $.nodes[].intent.uri | str | — |
| $.nodes[].name | str | 打开微信 |
| $.nodes[].nodeId | int | 1 |
| $.nodes[].versionCode | int | 1160 |
| $.to_speak | str | 我搞定啦 |
| $.open_mic | bool | True |

### assets/settings.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.settingData | array | — |
| $.settingData[].id | int | 1 |
| $.settingData[].type | int | 1 |
| $.settingData[].router | str | Navigation |
| $.settingData[].title | str | 导航设置 |

### assets/settings_config.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $ | array | — |
| $[].type | str | normal |
| $[].title | str | 导航设置 |
| $[].key | str | nav_setting |
| $[].value | array | — |
| $[].value[].type | str | switch |
| $[].value[].title | str | POI信息流转 |
| $[].value[].key | str | prefer_auto_poi |
| $[].router | str | Navigation |
| $[].value[].value | array | — |
| $[].value[].value[].type | str | radioButton |
| $[].value[].value[].title | str | 车机蓝牙 |
| $[].value[].value[].key | str | prefer_auto_bt_play |
| $[].value[].subTitle | str | 开启后提升部分车型媒体音质，如异常请关闭该设置 |
| $[].value[].router | str | Audio |
| $[].value[].value[].subTitle | str | 1920 x 1080 |
| $[].value[].value[].value | array | — |
| $[].value[].value[].value[].type | str | title |
| $[].value[].value[].value[].title | str | 标准屏幕（16:9） |
| $[].value[].value[].value[].key | str | user_setting_resolution |
| $[].value[].value[].value[].subTitle | str | 1920 x 1080 |
| $[].value[].value[].value[].router | str | custom_resolution |
| $[].value[].value[].router | str | Resolution |

### assets/test_main_ai_nickname.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.status.code | int | 200 |
| $.status.error_type | str | OK |
| $.data | array | — |
| $.data[].unitId | str | 669629119620715520 |
| $.data[].unitType | str | scene |
| $.data[].name | str | 场景-春天 |
| $.data[].isWhiteList | int | -1 |
| $.data[].scene.bubbleText | array | — |
| $.data[].scene.bubbleText[] | str | 春天到了，想推荐你看看👇 |
| $.data[].scene.cards | array | — |
| $.data[].scene.cards[].cardId | str | 643893673779534848 |
| $.data[].scene.cards[].cardType | str | widget |
| $.data[].scene.cards[].template | str | weather |
| $.data[].scene.cards[].title | str | 今天天气怎么样 |
| $.data[].scene.cards[].bgImg | str | https://file.xiaomixiaoai.com/anonymous/file/4f7978612c01400f9947d33d |
| $.data[].scene.cards[].bgColorStart | str | — |
| $.data[].scene.cards[].bgColorEnd | str | — |
| $.data[].scene.cards[].clickEvent.event | str | query |
| $.data[].scene.cards[].clickEvent.query | str | 今天天气怎么样 |
| $.data[].scene.cards[].widgetInfo.weather.temperature | str | 20 |
| $.data[].scene.cards[].widgetInfo.weather.quality | str | 优 |
| $.data[].scene.cards[].img | str | https://file.xiaomixiaoai.com/cache/anonymous/file/8f9c0b8f9c01800f42186251 |
| $.data[].scene.cards[].clickEvent.isAutoPlay | bool | False |
| $.data[].dialog.question.questionId | str | 650750447228815360 |
| $.data[].dialog.question.questionType | str | nickname |
| $.data[].dialog.question.questionName | str | 昵称 |
| $.data[].dialog.question.text | array | — |
| $.data[].dialog.question.text[] | str | 你想我怎么叫你呢？😊 |
| $.data[].dialog.answer | array | — |
| $.data[].dialog.answer[].inputType | str | COMMON_TYPE |
| $.data[].dialog.answer[].label | str | 宝贝 |
| $.data[].scene.cards[].widgetInfo.calendar.chineseCalendarDate | str | 七月初二 |
| $.data[].scene.cards[].widgetInfo.calendar.calendarDate | str | 20 |
| $.data[].scene.cards[].widgetInfo.calendar.good | str | 真心 |
| $.data[].scene.cards[].widgetInfo.calendar.bad | str | 虚伪 |
| $.data[].scene.cards[].icon | str | xxx |
| $.data[].scene.cards[].clickEvent.intent | str | intent:#Intent;action=com.miui.voiceassist.ACTION_CHECK_LOGIN;launchFlags=0x10000000;component=com.miui.voiceassist/com.xiaomi.voiceassistant.personalInfo.CheckLoginActivity;S.intentUri=intent%3a%2f%2faiweb%3furl%3dhttps%253a%252f%252fi-preview.xiaom |
| $.data[].scene.cards[].widgetInfo.constellation.rate | int | 4 |
| $.data[].scene.cards[].widgetInfo.constellation.desc | str | 点击先设置一下你的生日吧！让小爱更了解你哦～ |
| $.data[].scene.cards[].widgetInfo.constellation.isDefault | bool | True |
| $.data[].scene.cards[].widgetInfo.holiday.holidayName | str | 国庆 |
| $.data[].scene.cards[].widgetInfo.holiday.date | str | 10月01日 |
| $.data[].scene.cards[].widgetInfo.holiday.days | int | 35 |
| $.data[].scene.cards[].subtitle | str | 应用直达 |
| $.data[].scene.cards[].describe | str | 有33万人在说 |
| $.data[].scene.cards[].clickEvent.instruction | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].header.name | str | PlayApp |
| $.data[].scene.cards[].clickEvent.instruction[].header.namespace | str | AudioPlayer |
| $.data[].scene.cards[].clickEvent.instruction[].header.dependence.id | str | 9e02992463594cb3b8252e131a304970 |
| $.data[].scene.cards[].clickEvent.instruction[].header.dependence.predicate | str | true |
| $.data[].scene.cards[].clickEvent.instruction[].header.dialog_id | str | 9b1785dc03084054910fffcccc638c10 |
| $.data[].scene.cards[].clickEvent.instruction[].header.id | str | 20bce96362af481c8d8bb2119bcb4de8 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.apk_size | int | 30700000 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.icon.description | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.icon.sources | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.icon.sources[].url | str | http://t2.a.market.xiaomi.com/download/AppStore/AppStore/04a825e922614e3efeba487f86c77bb97cc4339c9 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.name | str | 音乐 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.pkg_name | str | com.miui.player |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.rating_score | float | 1.8 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.slogan | str | 海量曲库众星云集，你爱听的这都有 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.tag | str | 影音视听 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.version.latest | int | 11331 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.app.version.min | int | 97 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items | array | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items[].album_id | str | 4437774714139529694 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items[].album_name | str | — |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items[].artist_id | str | 0 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items[].artist_name | str | 聂枫 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items[].audio_id | str | 27665343 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.audio_items[].audio_name | str | 草原夜色美 |
| $.data[].scene.cards[].clickEvent.instruction[].payload.play_length | int | 10 |
| $.data[].scene.cards[].widgetInfo.musicRecommendation.coverImage | array | — |
| $.data[].scene.cards[].widgetInfo.musicRecommendation.coverImage[] | str | http://y.gtimg.cn/music/photo_new/T002R500x500M000001tTNk21VYQji_1.jpg |
| $.timeStamp | int | 1618651624170 |
| $.requestId | str | 7c13a5d3f71140e4a7068e48af96e9ed |

### assets/track.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.request_id | str | sdfsdf |
| $.domain | str | sdfsdf |
| $.timestamp | str | 123345 |
| $.context | str | sdfsdf |
| $.content | str | sdfsdf |
| $.error_node_json | str | sdfsdf |
| $.error_type | str | sdfsdf |
| $.pkg_name | str | sdfsdf |
| $.version_code | int | 4 |
| $.version_name | str | sdfsdf |
| $.query | str | sdfsdf |
| $.node_version_code | int | 4 |
| $.node_version_name | str | sdfsdf |
| $.error_node_id | int | 4 |
| $.all_execute_time | int | 234444444444 |
| $.node_execute_time | array | — |
| $.node_execute_time[].node_id | int | 4 |
| $.node_execute_time[].execute_time | int | 234444444444 |
| $.node_execute_time[].wait_user_time | int | 234444444444 |
| $.sdk_access_node_info | str | sdfsdf |
| $.uploadLogContext | bool | True |
| $.AccessibilityServiceState | str | sdfsf |
| $.useragent | str | sdfsdf |
| $.event_category | str | sdfsfd |
| $.event_type | str | sdfsfd |
| $.event_value | str | sdfsfd |
| $.event_params | str | sdfsdf |

### assets/training_config.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.intro_video | str | https://cdn.cnbj1.fds.api.mi-img.com/xiaoailite/test/%E4%B8%80%E5%8F%A5%E8%AF%9D%E6%8E%A7%E5%88%B6%E5%A4%9A%E4%B8%AA%E8%AE%BE%E5%A4%87_%5BAVC_%E9%AB%98%E8%B4%A8%E9%87%8F%E5%92%8C%E5%A4%A7%E5%B0%8F%5D.mp4 |

### assets/vad_prestart_switch_config.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.vad_prestart | bool | False |

### assets/vendor_tts_config.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.vendor_tts_model | array | — |
| $.vendor_tts_model[] | str | cmi |
| $.asr_detect_score | float | 0.4 |
| $.total_feature_on | bool | False |

### assets/voice_wave_config.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.devices | array | — |
| $.devices[] | str | cas |

### assets/wallpaperjson.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.wallpaperCategorys | array | — |
| $.wallpaperCategorys[].categoryId | str | 柔光 |
| $.wallpaperCategorys[].categoryNameKey | str | phone_settings_wallpaper_soft_light |
| $.wallpaperCategorys[].wallpapers | array | — |
| $.wallpaperCategorys[].wallpapers[].id | str | 19 |
| $.wallpaperCategorys[].wallpapers[].wallpaper_name | str | wallpaper_19 |
| $.wallpaperCategorys[].wallpapers[].light_color | str | #DEDFE0 |
| $.wallpaperCategorys[].wallpapers[].dark_color | str | #5A5B5B |

### assets/weixin_contact_for_localnlp.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.weixin_contact_for_localnlp | array | — |
| $.weixin_contact_for_localnlp[].name | str | adb |
| $.weixin_contact_for_localnlp[].category | str | category |

### assets/whitelist.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.white_list_model | array | — |
| $.white_list_model[].model_name | str | MIX 2 |
| $.white_list_model[].device_name | str | chiron |

### debug.conf.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.debug_tool | str | com.xiaomi.ai.nlp.factoid.utils.debug.SystemOutDebugTool |

### nlp_edge_config.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.phonecall_asr_threshold_not_waiting_online | float | 0.67 |

### parser.conf.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.parsers | array | — |
| $.parsers[].parser | str | NumberParser |
| $.parsers[].deps | array | — |
| $.parsers[].deps[] | str | NumberParser |

### res/-Im.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.v | str | 5.12.2 |
| $.fr | int | 60 |
| $.ip | int | 0 |
| $.op | int | 170 |
| $.w | int | 1008 |
| $.h | int | 480 |
| $.nm | str | 通过CarWith连接 |
| $.ddd | int | 0 |
| $.assets | array | — |
| $.assets[].id | str | image_0 |
| $.assets[].w | int | 26 |
| $.assets[].h | int | 35 |
| $.assets[].u | str | — |
| $.assets[].p | str | data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAjCAYAAACKPxqrAAACmklEQVR4Ab3BMWtbVxiA4ff7pO73J5ykV9w1SxdPDaFo0dBAumRKoAkcgUEZ4qEuhECipaMgF6rBnjx17iakqUuGZr2t256fcH+AdL7IRoNq7rmSY+Pnkf5owF1Q7kiXHSomWYfO94YcGPadIJlAZlCDBLCPYGc9hgtaSH80oEnFJOvQHRq8 |
| $.assets[].e | int | 1 |
| $.layers | array | — |
| $.layers[].ddd | int | 0 |
| $.layers[].ind | int | 4 |
| $.layers[].ty | int | 2 |
| $.layers[].nm | str | 定位置.png |
| $.layers[].cl | str | png |
| $.layers[].refId | str | image_0 |
| $.layers[].sr | int | 1 |
| $.layers[].ks.o.a | int | 0 |
| $.layers[].ks.o.k | int | 100 |
| $.layers[].ks.o.ix | int | 11 |
| $.layers[].ks.r.a | int | 0 |
| $.layers[].ks.r.k | int | 0 |
| $.layers[].ks.r.ix | int | 10 |
| $.layers[].ks.p.a | int | 1 |
| $.layers[].ks.p.k | array | — |
| $.layers[].ks.p.k[].i.x | float | 0.16 |
| $.layers[].ks.p.k[].i.y | int | 1 |
| $.layers[].ks.p.k[].o.x | float | 0.167 |
| $.layers[].ks.p.k[].o.y | float | 0.167 |
| $.layers[].ks.p.k[].t | int | 115 |
| $.layers[].ks.p.k[].s | array | — |
| $.layers[].ks.p.k[].s[] | int | 488 |
| $.layers[].ks.p.k[].s[] | float | 179.059 |
| $.layers[].ks.p.k[].to | array | — |
| $.layers[].ks.p.k[].to[] | float | 3.691 |
| $.layers[].ks.p.k[].to[] | int | 0 |
| $.layers[].ks.p.k[].ti | array | — |
| $.layers[].ks.p.k[].ti[] | float | -3.691 |
| $.layers[].ks.p.k[].ti[] | int | 0 |
| $.layers[].ks.p.ix | int | 2 |
| $.layers[].ks.p.l | int | 2 |
| $.layers[].ks.a.a | int | 0 |
| $.layers[].ks.a.k | array | — |
| $.layers[].ks.a.k[] | int | 13 |
| $.layers[].ks.a.k[] | float | 17.5 |
| $.layers[].ks.a.ix | int | 1 |
| $.layers[].ks.a.l | int | 2 |
| $.layers[].ks.s.a | int | 1 |
| $.layers[].ks.s.k | array | — |
| $.layers[].ks.s.k[].i.x | array | — |
| $.layers[].ks.s.k[].i.x[] | float | 0.16 |
| $.layers[].ks.s.k[].i.y | array | — |
| $.layers[].ks.s.k[].i.y[] | int | 1 |
| $.layers[].ks.s.k[].o.x | array | — |
| $.layers[].ks.s.k[].o.x[] | float | 0.167 |
| $.layers[].ks.s.k[].o.y | array | — |
| $.layers[].ks.s.k[].o.y[] | float | 0.167 |
| $.layers[].ks.s.k[].o.y[] | int | 0 |
| $.layers[].ks.s.k[].t | int | 115 |
| $.layers[].ks.s.k[].s | array | — |
| $.layers[].ks.s.k[].s[] | int | 90 |
| $.layers[].ks.s.ix | int | 6 |
| $.layers[].ks.s.l | int | 2 |
| $.layers[].ao | int | 0 |
| $.layers[].ip | int | 115 |
| $.layers[].op | int | 293 |
| $.layers[].st | int | 0 |
| $.layers[].bm | int | 0 |
| $.layers[].parent | int | 6 |
| $.layers[].ks.p.k[] | float | 113.051 |
| $.layers[].ks.p.k[] | int | 0 |
| $.layers[].ks.s.k[] | int | 90 |
| $.layers[].ks.o.k | array | — |
| $.layers[].ks.o.k[].i.x | array | — |
| $.layers[].ks.o.k[].i.x[] | float | 0.833 |
| $.layers[].ks.o.k[].i.y | array | — |
| $.layers[].ks.o.k[].i.y[] | float | 0.833 |
| $.layers[].ks.o.k[].o.x | array | — |
| $.layers[].ks.o.k[].o.x[] | float | 0.167 |
| $.layers[].ks.o.k[].o.y | array | — |
| $.layers[].ks.o.k[].o.y[] | float | 0.167 |
| $.layers[].ks.o.k[].t | int | 105 |
| $.layers[].ks.o.k[].s | array | — |
| $.layers[].ks.o.k[].s[] | int | 100 |
| $.layers[].ks.r.k | array | — |
| $.layers[].ks.r.k[].i.x | array | — |
| $.layers[].ks.r.k[].i.x[] | float | 0.667 |
| $.layers[].ks.r.k[].i.y | array | — |
| $.layers[].ks.r.k[].i.y[] | int | 1 |
| $.layers[].ks.r.k[].o.x | array | — |
| $.layers[].ks.r.k[].o.x[] | float | 0.333 |
| $.layers[].ks.r.k[].o.y | array | — |
| $.layers[].ks.r.k[].o.y[] | int | 0 |
| $.layers[].ks.r.k[].t | int | 25 |
| $.layers[].ks.r.k[].s | array | — |
| $.layers[].ks.r.k[].s[] | int | 0 |
| $.layers[].ks.o.k[].i.y[] | int | 1 |
| $.layers[].ks.o.k[].o.y[] | int | 0 |
| $.layers[].sw | int | 1008 |
| $.layers[].sh | int | 480 |
| $.layers[].sc | str | #ffffff |
| $.markers | array | — |

### res/5Vo.json

| 字段路径 | 类型 | 包内静态样例 |
| --- | --- | --- |
| $.v | str | 5.12.2 |
| $.fr | int | 60 |
| $.ip | int | 0 |
| $.op | int | 170 |
| $.w | int | 1008 |
| $.h | int | 480 |
| $.nm | str | 通过CarWith连接 |
| $.ddd | int | 0 |
| $.assets | array | — |
| $.assets[].id | str | image_0 |
| $.assets[].w | int | 26 |
| $.assets[].h | int | 35 |
| $.assets[].u | str | — |
| $.assets[].p | str | data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAjCAYAAACKPxqrAAACkklEQVR4Ab3BQW4TZxiA4ff77O7nAkg/0lizqoS6rxTYeGMkcgBa0pUnVsBcADwnaI0F8YpEzQW4gacnaFBXo0Tqf4Q5gD0fTuSFieYfT0iU55H+eMBDUB5Ilx0KZlGHzgtDngG/ApFAZFCCeLD/kOpzz0Y5DaQ/HlCnYBZ16I4N3ghE7GDg |
| $.assets[].e | int | 1 |
| $.layers | array | — |
| $.layers[].ddd | int | 0 |
| $.layers[].ind | int | 4 |
| $.layers[].ty | int | 2 |
| $.layers[].nm | str | 定位置.png |
| $.layers[].cl | str | png |
| $.layers[].refId | str | image_0 |
| $.layers[].sr | int | 1 |
| $.layers[].ks.o.a | int | 0 |
| $.layers[].ks.o.k | int | 100 |
| $.layers[].ks.o.ix | int | 11 |
| $.layers[].ks.r.a | int | 0 |
| $.layers[].ks.r.k | int | 0 |
| $.layers[].ks.r.ix | int | 10 |
| $.layers[].ks.p.a | int | 1 |
| $.layers[].ks.p.k | array | — |
| $.layers[].ks.p.k[].i.x | float | 0.16 |
| $.layers[].ks.p.k[].i.y | int | 1 |
| $.layers[].ks.p.k[].o.x | float | 0.167 |
| $.layers[].ks.p.k[].o.y | float | 0.167 |
| $.layers[].ks.p.k[].t | int | 115 |
| $.layers[].ks.p.k[].s | array | — |
| $.layers[].ks.p.k[].s[] | int | 488 |
| $.layers[].ks.p.k[].s[] | float | 179.059 |
| $.layers[].ks.p.k[].to | array | — |
| $.layers[].ks.p.k[].to[] | float | 2.667 |
| $.layers[].ks.p.k[].to[] | int | 0 |
| $.layers[].ks.p.k[].ti | array | — |
| $.layers[].ks.p.k[].ti[] | float | -2.667 |
| $.layers[].ks.p.k[].ti[] | int | 0 |
| $.layers[].ks.p.ix | int | 2 |
| $.layers[].ks.p.l | int | 2 |
| $.layers[].ks.a.a | int | 0 |
| $.layers[].ks.a.k | array | — |
| $.layers[].ks.a.k[] | int | 13 |
| $.layers[].ks.a.k[] | float | 17.5 |
| $.layers[].ks.a.ix | int | 1 |
| $.layers[].ks.a.l | int | 2 |
| $.layers[].ks.s.a | int | 1 |
| $.layers[].ks.s.k | array | — |
| $.layers[].ks.s.k[].i.x | array | — |
| $.layers[].ks.s.k[].i.x[] | float | 0.16 |
| $.layers[].ks.s.k[].i.y | array | — |
| $.layers[].ks.s.k[].i.y[] | int | 1 |
| $.layers[].ks.s.k[].o.x | array | — |
| $.layers[].ks.s.k[].o.x[] | float | 0.167 |
| $.layers[].ks.s.k[].o.y | array | — |
| $.layers[].ks.s.k[].o.y[] | float | 0.167 |
| $.layers[].ks.s.k[].o.y[] | int | 0 |
| $.layers[].ks.s.k[].t | int | 115 |
| $.layers[].ks.s.k[].s | array | — |
| $.layers[].ks.s.k[].s[] | int | 90 |
| $.layers[].ks.s.ix | int | 6 |
| $.layers[].ks.s.l | int | 2 |
| $.layers[].ao | int | 0 |
| $.layers[].ip | int | 115 |
| $.layers[].op | int | 293 |
| $.layers[].st | int | 0 |
| $.layers[].bm | int | 0 |
| $.layers[].parent | int | 6 |
| $.layers[].ks.p.k[] | float | 113.051 |
| $.layers[].ks.p.k[] | int | 0 |
| $.layers[].ks.s.k[] | int | 90 |
| $.layers[].ks.o.k | array | — |
| $.layers[].ks.o.k[].i.x | array | — |
| $.layers[].ks.o.k[].i.x[] | float | 0.833 |
| $.layers[].ks.o.k[].i.y | array | — |
| $.layers[].ks.o.k[].i.y[] | float | 0.833 |
| $.layers[].ks.o.k[].o.x | array | — |
| $.layers[].ks.o.k[].o.x[] | float | 0.167 |
| $.layers[].ks.o.k[].o.y | array | — |
| $.layers[].ks.o.k[].o.y[] | float | 0.167 |
| $.layers[].ks.o.k[].t | int | 105 |
| $.layers[].ks.o.k[].s | array | — |
| $.layers[].ks.o.k[].s[] | int | 100 |
| $.layers[].ks.r.k | array | — |
| $.layers[].ks.r.k[].i.x | array | — |
| $.layers[].ks.r.k[].i.x[] | float | 0.667 |
| $.layers[].ks.r.k[].i.y | array | — |
| $.layers[].ks.r.k[].i.y[] | int | 1 |
| $.layers[].ks.r.k[].o.x | array | — |
| $.layers[].ks.r.k[].o.x[] | float | 0.333 |
| $.layers[].ks.r.k[].o.y | array | — |
| $.layers[].ks.r.k[].o.y[] | int | 0 |
| $.layers[].ks.r.k[].t | int | 25 |
| $.layers[].ks.r.k[].s | array | — |
| $.layers[].ks.r.k[].s[] | int | 0 |
| $.layers[].ks.o.k[].i.y[] | int | 1 |
| $.layers[].ks.o.k[].o.y[] | int | 0 |
| $.markers | array | — |

