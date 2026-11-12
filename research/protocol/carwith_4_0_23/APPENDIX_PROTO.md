# 附录：完整 Protobuf 字段与枚举

日期：2026-11-12。字段直接取自 APK 内的 `ucar.proto`、`share.proto`；字段 tag 与编译类 `*_FIELD_NUMBER` 逐项核对。

300 个 ucar.proto 字段与编译类匹配；42 个 share.proto 字段只有包内 schema 证据，没有对应的 ShareProto 编译类匹配。后者仍保留为定义，不能声明其当前通道已启用。

`singular` 表示未显式 optional/repeated 的声明，不等于已经确认业务必填。消息字段编号不是封包头 serviceId。

## ucar.proto

原始文件：[source/ucar.proto](source/ucar.proto)。

### Gps

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | altitude | double | singular | 9 | 匹配 | — |
| 2 | latitude | double | singular | 10 | 匹配 | — |
| 3 | longitude | double | singular | 11 | 匹配 | — |
| 4 | antenna_state | uint32 | singular | 12 | 匹配 | — |
| 5 | pdop | uint32 | singular | 13 | 匹配 | — |
| 6 | speed | uint32 | singular | 14 | 匹配 | — |
| 7 | heading | uint32 | singular | 15 | 匹配 | — |
| 8 | sats_used | uint32 | singular | 16 | 匹配 | — |
| 9 | sats_visible | uint32 | singular | 17 | 匹配 | — |
| 10 | timestamp | uint64 | singular | 18 | 匹配 | — |

### Lights

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | low_beam_on | bool | singular | 22 | 匹配 | — |
| 2 | high_beam_on | bool | singular | 23 | 匹配 | — |
| 3 | clearance_lamp_on | bool | singular | 24 | 匹配 | — |
| 4 | backup_lamp_on | bool | singular | 25 | 匹配 | — |
| 5 | stop_lamp_on | bool | singular | 26 | 匹配 | — |

### GyroScope

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | gyro_type | int32 | singular | 36 | 匹配 | — |
| 2 | legyro_x | double | singular | 37 | 匹配 | — |
| 3 | legyro_y | double | singular | 38 | 匹配 | — |
| 4 | legyro_z | double | singular | 39 | 匹配 | — |
| 5 | timestamp | uint64 | singular | 40 | 匹配 | — |

### Acceleration

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | acc_x | double | singular | 44 | 匹配 | — |
| 2 | acc_y | double | singular | 45 | 匹配 | — |
| 3 | acc_z | double | singular | 46 | 匹配 | — |
| 4 | timestamp | uint64 | singular | 47 | 匹配 | — |

### Oil

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | max_fuel | uint32 | singular | 51 | 匹配 | 0.1L |
| 2 | current_fuel | uint32 | singular | 52 | 匹配 | — |
| 3 | is_low_fuel | bool | optional | 53 | 匹配 | — |

### Battery

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | max_power | uint32 | singular | 57 | 匹配 | 0.1kwH |
| 2 | current_power | uint32 | singular | 58 | 匹配 | — |
| 3 | is_low_power | bool | singular | 59 | 匹配 | — |

### GearInfo

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | gear | GearState | singular | 71 | 匹配 | — |
| 2 | speed | uint32 | singular | 72 | 匹配 | — |

### LightSensorInfo

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | max_lux | double | singular | 76 | 匹配 | — |
| 2 | min_lux | double | singular | 77 | 匹配 | — |
| 3 | current_lux | double | singular | 78 | 匹配 | — |

### SensorIndex

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | gps | Gps | singular | 82 | 匹配 | — |
| 2 | lights | Lights | singular | 83 | 匹配 | — |
| 3 | gyro_scope | GyroScope | singular | 84 | 匹配 | — |
| 4 | acceleration | Acceleration | singular | 85 | 匹配 | — |
| 5 | oil | Oil | singular | 86 | 匹配 | — |
| 6 | gear_info | GearInfo | singular | 87 | 匹配 | — |
| 7 | light_sensor_info | LightSensorInfo | singular | 88 | 匹配 | — |
| 8 | battery | Battery | singular | 89 | 匹配 | — |

### Heartbeat

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | timestamp | uint64 | singular | 94 | 匹配 | — |

### GetPortRequest

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | type | ServerType | singular | 105 | 匹配 | — |

### GetPortResponse

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | result | Result | singular | 115 | 匹配 | — |
| 2 | port | int32 | singular | 116 | 匹配 | — |

### NotifyCarToForeground

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | timestamp | uint64 | singular | 120 | 匹配 | — |

### NotifyCarToBackground

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | timestamp | uint64 | singular | 124 | 匹配 | — |

### NotifyCarToForegroundCapsule

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | timestamp | uint64 | singular | 128 | 匹配 | — |

### NotifyCarToBackgroundCapsule

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | timestamp | uint64 | singular | 132 | 匹配 | — |

### PauseCast

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | timestamp | uint64 | singular | 136 | 匹配 | — |

### NotifyMicrophoneState

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | state | bool | singular | 140 | 匹配 | — |
| 2 | sample_rate | SampleRate | singular | 141 | 匹配 | — |
| 3 | channel_mask | ChannelMask | singular | 142 | 匹配 | — |
| 4 | encoding_format | EncodingFormat | singular | 143 | 匹配 | — |

### NotifyMirrorState

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mirror_state | MirrorState | singular | 184 | 匹配 | — |

### NotifyAudioPlayerState

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | type | AudioType | singular | 196 | 匹配 | — |
| 2 | state | AudioPlayerState | singular | 197 | 匹配 | — |
| 3 | sample_rate | SampleRate | singular | 198 | 匹配 | — |
| 4 | channel_mask | ChannelMask | singular | 199 | 匹配 | — |
| 5 | encoding_format | EncodingFormat | singular | 200 | 匹配 | — |
| 6 | mime_type | string | optional | 201 | 匹配 | — |

### NotifyPhoneState

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | cs | CALL_STATE | singular | 231 | 匹配 | — |
| 2 | is_screen_locked | bool | singular | 232 | 匹配 | 是否锁屏 |
| 3 | is_wechat_qq_call | bool | singular | 233 | 匹配 | 是否为qq或微信语音通话 |
| 4 | is_voice_assistant_active | bool | singular | 234 | 匹配 | 手机端语音助手是否唤醒 |
| 5 | is_low_power | bool | optional | 235 | 匹配 | 手机端是否低电压，具体低电压阀值，由手机端决定 |
| 6 | is_overheat | bool | optional | 236 | 匹配 | 手机端温度是否过高，具体高温阀值，由手机端决定 |

### NotifyMusicInfo

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | artist_name | string | singular | 241 | 匹配 | — |
| 2 | album_name | string | singular | 242 | 匹配 | — |
| 3 | cover_art | string | singular | 243 | 匹配 | — |
| 4 | lyrics | string | singular | 244 | 匹配 | — |
| 5 | playing_times_ms | uint64 | singular | 245 | 匹配 | — |
| 6 | title | string | singular | 246 | 匹配 | — |
| 7 | author_name | string | singular | 247 | 匹配 | — |
| 8 | writer_name | string | singular | 248 | 匹配 | — |
| 9 | composer_name | string | singular | 249 | 匹配 | — |
| 10 | playing_current_time_ms | int32 | singular | 250 | 匹配 | — |
| 11 | is_favorite | bool | singular | 251 | 匹配 | — |
| 12 | is_playing | bool | singular | 252 | 匹配 | — |
| 13 | cover_art_bitmap | bytes | optional | 253 | 匹配 | 建议在每首歌切换的时候提供一次 |
| 14 | id | int32 | optional | 254 | 匹配 | 应用融合、小窗投屏可以根据id获取应用名称，图标，-1表示session已销毁，非上车应用，全屏投屏时均为0 |

### NotifyNavigationInfo

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | isNavigating | bool | singular | 258 | 匹配 | — |
| 2 | directionIcon | bytes | singular | 259 | 匹配 | — |
| 3 | distance | string | singular | 260 | 匹配 | — |
| 4 | distanceUnit | string | singular | 261 | 匹配 | — |
| 5 | operation | string | singular | 262 | 匹配 | — |
| 6 | where | string | singular | 263 | 匹配 | — |
| 7 | title1 | string | singular | 264 | 匹配 | — |
| 8 | title2 | string | singular | 265 | 匹配 | — |
| 9 | id | int32 | optional | 266 | 匹配 | 应用融合、小窗投屏可以根据id获取应用名称，图标， |

### CustomKeyEvent

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | action | int32 | singular | 285 | 匹配 | — |
| 2 | keycode | KeyCode | singular | 286 | 匹配 | — |
| 3 | meta_state | int32 | singular | 287 | 匹配 | — |
| 4 | timestamp | uint64 | singular | 288 | 匹配 | — |

### VRCmdToPhone

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | cmd | VRCmd | singular | 310 | 匹配 | — |
| 2 | source | string | singular | 311 | 匹配 | — |

### NotifyCallHungUp

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | timestamp | uint64 | singular | 315 | 匹配 | — |

### NotifySwitchDayOrNight

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mode | Mode | singular | 324 | 匹配 | — |

### AwakenVoiceAssistant

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | pcm_data | bytes | singular | 328 | 匹配 | — |
| 2 | sample_rate | SampleRate | singular | 329 | 匹配 | — |
| 3 | channel_mask | ChannelMask | singular | 330 | 匹配 | — |
| 4 | encoding_format | EncodingFormat | singular | 331 | 匹配 | — |
| 5 | timestamp | uint64 | singular | 332 | 匹配 | — |
| 6 | source | string | singular | 333 | 匹配 | — |

### AudioPlayerControl

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | audio_type | AudioType | singular | 341 | 匹配 | — |
| 2 | buffering_count | int32 | singular | 344 | 匹配 | — |
| 3 | speed_adjust_step | int32 | singular | 347 | 匹配 | — |

### BluetoothMacInfo

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | op_type | OPType | singular | 356 | 匹配 | — |
| 2 | bluetooth_mac | string | singular | 357 | 匹配 | — |

### Disconnect

空 message；不添加字段。

### GetUCarConfigRequest

空 message；不添加字段。

### GetUCarConfigResponse

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | carBrMac | bytes | singular | 369 | 匹配 | — |
| 2 | screenWidth | int32 | singular | 370 | 匹配 | — |
| 3 | screenHeight | int32 | singular | 371 | 匹配 | — |
| 4 | dpi | int32 | singular | 372 | 匹配 | — |
| 5 | videoDisplayWidth | int32 | singular | 373 | 匹配 | — |
| 6 | videoDisplayHeight | int32 | singular | 374 | 匹配 | — |
| 7 | fps | int32 | singular | 375 | 匹配 | — |
| 8 | isSupportP2P | bool | singular | 376 | 匹配 | — |
| 9 | isSupportSoftAP | bool | singular | 377 | 匹配 | — |
| 10 | isDataTransMode | bool | singular | 378 | 匹配 | — |
| 11 | default5gChannel | int32 | singular | 379 | 匹配 | — |
| 12 | isSupportCamera | bool | singular | 380 | 匹配 | — |
| 13 | isSupportMic | bool | singular | 381 | 匹配 | — |
| 14 | isSupportLowLatencyDecodingMode | bool | singular | 382 | 匹配 | — |
| 15 | isSupportVoiceWaken | bool | singular | 383 | 匹配 | — |
| 16 | carCustomField | bytes | singular | 384 | 匹配 | — |
| 17 | sdkVersion | string | singular | 385 | 匹配 | — |
| 18 | workModes | int32 | optional | 386 | 匹配 | — |
| 19 | isSupportPOINav | bool | optional | 387 | 匹配 | — |
| 20 | isSupportRotation | bool | optional | 388 | 匹配 | — |
| 21 | isSupportHomeKey | bool | optional | 389 | 匹配 | — |
| 22 | isSupportBackKey | bool | optional | 390 | 匹配 | — |
| 23 | isSupportHevc | bool | optional | 391 | 匹配 | — |
| 24 | realDpi | int32 | optional | 392 | 匹配 | — |

### GetAppListRequest

空 message；不添加字段。

### AppGeneralInfoMessage

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | int32 | singular | 420 | 匹配 | — |
| 2 | label | string | singular | 421 | 匹配 | — |
| 3 | category | AppCategory | singular | 422 | 匹配 | — |

### GetAppListResponse

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | total | int32 | singular | 426 | 匹配 | — |
| 2 | appInfo | AppGeneralInfoMessage | repeated | 427 | 匹配 | — |

### GetAppDetailInfoRequest

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | total | int32 | singular | 431 | 匹配 | — |
| 2 | id | int32 | repeated | 432 | 匹配 | — |

### AppDetailInfoMessage

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | int32 | singular | 436 | 匹配 | — |
| 2 | label | string | singular | 437 | 匹配 | — |
| 3 | category | AppCategory | singular | 438 | 匹配 | — |
| 4 | packageName | string | singular | 439 | 匹配 | — |
| 5 | icon | bytes | singular | 440 | 匹配 | — |
| 6 | isSupportLandscape | bool | optional | 441 | 匹配 | — |
| 7 | isSupportPortrait | bool | optional | 442 | 匹配 | — |

### GetAppDetailInfoResponse

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | total | int32 | singular | 446 | 匹配 | — |
| 2 | appDetailInfo | AppDetailInfoMessage | repeated | 447 | 匹配 | — |

### InvokeApp

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | int32 | singular | 467 | 匹配 | — |
| 2 | packageName | string | singular | 468 | 匹配 | — |
| 3 | invokeState | AppInvokeCategory | singular | 469 | 匹配 | — |
| 4 | displayMode | int32 | singular | 470 | 匹配 | — |

### DisplayVisibleRegion

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mode | int32 | singular | 474 | 匹配 | — |
| 2 | originWidth | int32 | singular | 475 | 匹配 | — |
| 3 | originHeight | int32 | singular | 476 | 匹配 | — |
| 4 | left | int32 | singular | 477 | 匹配 | — |
| 5 | top | int32 | singular | 478 | 匹配 | — |
| 6 | right | int32 | singular | 479 | 匹配 | — |
| 7 | bottom | int32 | singular | 480 | 匹配 | — |

### AppStateChanged

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | int32 | singular | 484 | 匹配 | — |
| 2 | isNeedShow | bool | singular | 485 | 匹配 | — |
| 3 | displayRotation | int32 | singular | 486 | 匹配 | — |
| 4 | state | AppStateCategory | singular | 487 | 匹配 | — |
| 5 | timestamp | uint64 | singular | 488 | 匹配 | — |
| 6 | visibleRegion | DisplayVisibleRegion | optional | 489 | 匹配 | — |
| 7 | isAllowedSwitchMode | bool | optional | 490 | 匹配 | — |

### AppListChanged

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | int32 | repeated | 499 | 匹配 | — |
| 2 | state | AppListState | singular | 500 | 匹配 | — |

### TouchPadVibrator

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | vibrator | bool | singular | 504 | 匹配 | — |

### ShareNetwork

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | action | ShareNetworkAction | singular | 515 | 匹配 | — |

### NetWorkState

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | isNetworkAvailable | bool | singular | 520 | 匹配 | — |

### NetWorkNotification

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | state | NetWorkState | optional | 524 | 匹配 | — |

### ControlIndex

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | heartbeat | Heartbeat | singular | 528 | 匹配 | — |
| 2 | get_port_request | GetPortRequest | singular | 529 | 匹配 | — |
| 3 | get_port_response | GetPortResponse | singular | 530 | 匹配 | — |
| 4 | notify_car_to_foreground | NotifyCarToForeground | singular | 531 | 匹配 | — |
| 5 | notify_car_to_background | NotifyCarToBackground | singular | 532 | 匹配 | — |
| 6 | notify_microphone_state | NotifyMicrophoneState | singular | 533 | 匹配 | — |
| 7 | notify_mirror_state | NotifyMirrorState | singular | 534 | 匹配 | — |
| 8 | notify_audio_player_state | NotifyAudioPlayerState | singular | 535 | 匹配 | — |
| 9 | notify_phone_state | NotifyPhoneState | singular | 536 | 匹配 | — |
| 10 | notify_music_info | NotifyMusicInfo | singular | 537 | 匹配 | — |
| 11 | notify_navigation_info | NotifyNavigationInfo | singular | 538 | 匹配 | — |
| 12 | custom_key_event | CustomKeyEvent | singular | 539 | 匹配 | — |
| 13 | vr_cmd_to_phone | VRCmdToPhone | singular | 540 | 匹配 | — |
| 14 | notify_call_hung_up | NotifyCallHungUp | singular | 541 | 匹配 | — |
| 15 | notify_switch_day_or_night | NotifySwitchDayOrNight | singular | 542 | 匹配 | — |
| 16 | awaken_voice_assistant | AwakenVoiceAssistant | singular | 543 | 匹配 | — |
| 17 | audio_player_control | AudioPlayerControl | singular | 544 | 匹配 | — |
| 18 | notify_add_camera | NotifyAddCamera | singular | 545 | 匹配 | — |
| 19 | notify_remove_camera | NotifyRemoveCamera | singular | 546 | 匹配 | — |
| 20 | set_camera_state | SetCameraState | singular | 547 | 匹配 | — |
| 21 | camera_state | NotifyCameraStateChanged | singular | 548 | 匹配 | — |
| 22 | bluetooth_mac | BluetoothMacInfo | singular | 549 | 匹配 | — |
| 23 | disconnect | Disconnect | singular | 550 | 匹配 | — |
| 24 | get_ucar_config_request | GetUCarConfigRequest | singular | 551 | 匹配 | — |
| 25 | get_ucar_config_response | GetUCarConfigResponse | singular | 552 | 匹配 | — |
| 26 | get_app_list_request | GetAppListRequest | singular | 553 | 匹配 | — |
| 27 | get_app_list_response | GetAppListResponse | singular | 554 | 匹配 | — |
| 28 | get_app_detail_info_request | GetAppDetailInfoRequest | singular | 555 | 匹配 | — |
| 29 | get_app_detail_info_response | GetAppDetailInfoResponse | singular | 556 | 匹配 | — |
| 30 | invoke_app | InvokeApp | singular | 557 | 匹配 | — |
| 31 | app_state_changed | AppStateChanged | singular | 558 | 匹配 | — |
| 32 | app_list_changed | AppListChanged | singular | 559 | 匹配 | — |
| 33 | poi_address | POIAddress | singular | 560 | 匹配 | — |
| 34 | call_info | CallInfo | singular | 561 | 匹配 | — |
| 35 | pick_up_call | PickUpCall | singular | 562 | 匹配 | — |
| 36 | add_notification | AddNotification | singular | 563 | 匹配 | — |
| 37 | click_notification | ClickNotification | singular | 564 | 匹配 | — |
| 38 | delete_notification | DeleteNotification | singular | 565 | 匹配 | — |
| 39 | touch_pad_vibrator | TouchPadVibrator | singular | 566 | 匹配 | — |
| 40 | notify_car_vr_state | NotifyCarVrState | singular | 567 | 匹配 | — |
| 41 | pause_cast | PauseCast | singular | 568 | 匹配 | — |
| 42 | share_network | ShareNetwork | singular | 569 | 匹配 | — |
| 10001 | notify_car_to_foreground_capsule | NotifyCarToForegroundCapsule | singular | 570 | 匹配 | — |
| 10002 | notify_car_to_background_capsule | NotifyCarToBackgroundCapsule | singular | 571 | 匹配 | — |
| 57 | network_notification | NetWorkNotification | singular | 572 | 匹配 | — |

### CallInfo

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | callState | CALL_STATE | singular | 576 | 匹配 | — |
| 2 | number | string | singular | 577 | 匹配 | — |
| 3 | name | string | singular | 578 | 匹配 | — |
| 4 | isIPCall | bool | singular | 579 | 匹配 | — |
| 5 | isNeedShowFloatingWindow | bool | singular | 580 | 匹配 | — |
| 6 | connectedTime | int32 | singular | 581 | 匹配 | — |
| 7 | inCallAppId | int32 | singular | 582 | 匹配 | — |

### PickUpCall

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | timestamp | uint64 | singular | 586 | 匹配 | — |

### NotifyCarVrState

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | isVrActive | bool | singular | 590 | 匹配 | — |

### AddNotification

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | int32 | singular | 603 | 匹配 | — |
| 2 | isOngoing | bool | singular | 604 | 匹配 | — |
| 3 | contentTitle | string | singular | 605 | 匹配 | — |
| 4 | contentText | string | optional | 606 | 匹配 | — |
| 5 | contentIntentId | int32 | optional | 607 | 匹配 | — |
| 6 | icon | bytes | optional | 608 | 匹配 | — |
| 7 | packageName | string | optional | 609 | 匹配 | — |
| 8 | contentBigIcon | bytes | optional | 610 | 匹配 | — |
| 9 | actionFirstTitle | string | optional | 611 | 匹配 | — |
| 10 | actionSecondTitle | string | optional | 612 | 匹配 | — |
| 11 | actionThirdTitle | string | optional | 613 | 匹配 | — |
| 12 | actionFirstPendingIntentId | int32 | optional | 614 | 匹配 | — |
| 13 | actionSecondPendingIntentId | int32 | optional | 615 | 匹配 | — |
| 14 | actionThirdPendingIntentId | int32 | optional | 616 | 匹配 | — |

### ClickNotification

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | int32 | singular | 620 | 匹配 | — |
| 2 | actionPendingIntentId | int32 | optional | 621 | 匹配 | — |

### DeleteNotification

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | total | int32 | singular | 625 | 匹配 | — |
| 2 | ids | int32 | repeated | 626 | 匹配 | — |

### AuthRequest

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | version | int32 | singular | 631 | 匹配 | 手机端协议版本 |
| 2 | authPk | bytes | singular | 632 | 匹配 | 手机端认证公钥R（x \|\| y） |
| 3 | authPkHmac | bytes | singular | 633 | 匹配 | 手机端认证公钥R的消息认证码 |
| 4 | agreementPk | bytes | singular | 634 | 匹配 | 手机端协商公钥R'（x \|\| y） |
| 5 | agreementPkSig | bytes | singular | 635 | 匹配 | 手机端协商公钥R'的ECDSA签名 |
| 6 | random | bytes | singular | 636 | 匹配 | 手机端随机数Na |
| 7 | id | bytes | singular | 637 | 匹配 | 手机端唯一id（6字节） |
| 8 | model | string | singular | 638 | 匹配 | 手机端型号名称（32字节，UTF-8） |
| 9 | userConfirmed | bool | singular | 639 | 匹配 | 手机密钥协商消息的用户确认状态 |
| 10 | workModes | int32 | optional | 640 | 匹配 | 手机端支持的工作模式 |
| 11 | productName | string | optional | 641 | 匹配 | 手机互联的产品名称（UTF-8） |

### AuthResponse

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | version | int32 | singular | 645 | 匹配 | 车机端协议版本 |
| 2 | authPk | bytes | singular | 646 | 匹配 | 车机端认证公钥S（x \|\| y） |
| 3 | authPkHmac | bytes | singular | 647 | 匹配 | 车机端认证公钥S的消息认证码 |
| 4 | agreementPk | bytes | singular | 648 | 匹配 | 车机端协商公钥S'（x \|\| y） |
| 5 | agreementPkSig | bytes | singular | 649 | 匹配 | 车机端协商公钥S'的ECDSA签名 |
| 6 | random | bytes | singular | 650 | 匹配 | 车机端随机数Nb |
| 7 | result | int32 | singular | 651 | 匹配 | 车机协商结果 |
| 8 | workModes | int32 | optional | 652 | 匹配 | 车机端选择的工作模式 |
| 9 | dayOrNightMode | int32 | optional | 653 | 匹配 | 车机端当前白天黑夜模式 0:unknown, 1:day, 2:night |
| 10 | screenInfo | string | optional | 654 | 匹配 | 车机端屏幕信息(w_h_dpi_sww_swh) |

### AuthConfirm

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | cipher | bytes | singular | 658 | 匹配 | 手机本地IP地址用会话密钥加密的密文 |

### AuthIndex

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | auth_request | AuthRequest | singular | 662 | 匹配 | — |
| 2 | auth_response | AuthResponse | singular | 663 | 匹配 | — |
| 3 | auth_confirm | AuthConfirm | singular | 664 | 匹配 | — |

### AudioIndex

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | audio_type | AudioType | singular | 669 | 匹配 | — |

### CarCertificate

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | content | bytes | singular | 674 | 匹配 | — |

### CertIndex

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | certificate | CarCertificate | singular | 678 | 匹配 | — |

### PictureSize

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | width | int32 | singular | 710 | 匹配 | — |
| 2 | height | int32 | singular | 711 | 匹配 | — |

### FpsRange

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | min | int32 | singular | 715 | 匹配 | — |
| 2 | max | int32 | singular | 716 | 匹配 | — |

### NotifyAddCamera

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | camera_id | string | singular | 720 | 匹配 | — |
| 2 | name | string | singular | 721 | 匹配 | — |
| 3 | lens_facing | LensFacing | singular | 722 | 匹配 | — |
| 4 | orientation | Orientation | singular | 723 | 匹配 | — |
| 5 | supported_sizes | PictureSize | repeated | 724 | 匹配 | — |
| 6 | fps_ranges | FpsRange | repeated | 725 | 匹配 | — |
| 7 | max_size | PictureSize | singular | 726 | 匹配 | — |

### NotifyRemoveCamera

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ids | string | repeated | 730 | 匹配 | — |

### SetCameraState

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | camera_id | string | singular | 734 | 匹配 | — |
| 2 | fps_range | FpsRange | singular | 735 | 匹配 | — |
| 3 | action | CameraAction | singular | 736 | 匹配 | — |
| 4 | picture_size | PictureSize | singular | 737 | 匹配 | — |

### NotifyCameraStateChanged

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | camera_id | string | singular | 750 | 匹配 | — |
| 2 | state | State | singular | 751 | 匹配 | — |

### POIDetailInfo

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | type | CoordinateType | singular | 761 | 匹配 | — |
| 2 | latitude | double | singular | 762 | 匹配 | — |
| 3 | longitude | double | singular | 763 | 匹配 | — |
| 4 | altitude | double | optional | 764 | 匹配 | — |

### POIAddress

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | address | string | singular | 768 | 匹配 | — |
| 2 | name | string | optional | 769 | 匹配 | — |
| 3 | poiInfo | POIDetailInfo | optional | 770 | 匹配 | — |

### 枚举

#### GyroScope.GyroType

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| GYRO_UNKNOWN | 0 | 0x0 | 31 | — |
| GYRO_SINGLE | 1 | 0x1 | 32 | — |
| GYRO_THREE | 2 | 0x2 | 33 | — |

#### GearInfo.GearState

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| GEAR_UNKNOWN | 0 | 0x0 | 64 | — |
| GEAR_PARK | 1 | 0x1 | 65 | — |
| GEAR_DRIVE | 2 | 0x2 | 66 | — |
| GEAR_REVERSE | 3 | 0x3 | 67 | — |
| GEAR_NEUTRAL | 4 | 0x4 | 68 | — |

#### GetPortRequest.ServerType

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| UNKNOWN | 0 | 0x0 | 100 | — |
| SENSOR | 1 | 0x1 | 101 | — |
| AUDIO | 2 | 0x2 | 102 | — |
| UIBC | 3 | 0x3 | 103 | — |

#### GetPortResponse.Result

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| UNKNOWN | 0 | 0x0 | 110 | — |
| SUCCESS | 1 | 0x1 | 111 | — |
| FAILURE | 2 | 0x2 | 112 | — |

#### ChannelMask

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| UNKNOWN_CHANNEL | 0 | 0x0 | 147 | — |
| CHANNEL_MONO | 1 | 0x1 | 148 | — |
| CHANNEL_STEREO | 2 | 0x2 | 149 | — |

#### EncodingFormat

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| UNKNOWN_FORMAT | 0 | 0x0 | 153 | — |
| ENCODING_PCM_8BIT | 1 | 0x1 | 154 | — |
| ENCODING_PCM_16BIT | 2 | 0x2 | 155 | — |
| ENCODING_PCM_24BIT_PACKED | 3 | 0x3 | 156 | — |
| ENCODING_PCM_32BIT | 4 | 0x4 | 157 | — |
| ENCODING_PCM_FLOAT | 5 | 0x5 | 158 | — |

#### SampleRate

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| UNKNOWN_RATE | 0 | 0x0 | 162 | — |
| SAMPLE_RATE_8000 | 8000 | 0x1f40 | 163 | — |
| SAMPLE_RATE_11025 | 11025 | 0x2b11 | 164 | — |
| SAMPLE_RATE_12000 | 12000 | 0x2ee0 | 165 | — |
| SAMPLE_RATE_16000 | 16000 | 0x3e80 | 166 | — |
| SAMPLE_RATE_22050 | 22050 | 0x5622 | 167 | — |
| SAMPLE_RATE_24000 | 24000 | 0x5dc0 | 168 | — |
| SAMPLE_RATE_32000 | 32000 | 0x7d00 | 169 | — |
| SAMPLE_RATE_44100 | 44100 | 0xac44 | 170 | — |
| SAMPLE_RATE_48000 | 48000 | 0xbb80 | 171 | — |
| SAMPLE_RATE_96000 | 96000 | 0x17700 | 172 | — |
| SAMPLE_RATE_192000 | 192000 | 0x2ee00 | 173 | — |

#### NotifyMirrorState.MirrorState

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| STATE_STOP_MIRROR | 0 | 0x0 | 179 | — |
| STATE_DISCONNECT_LINK | 1 | 0x1 | 180 | — |
| STATE_GO_TO_DESKTOP | 2 | 0x2 | 181 | — |
| STATE_BACK_TO_FOREGROUND | 3 | 0x3 | 182 | — |

#### NotifyAudioPlayerState.AudioPlayerState

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| START_PLAYER | 0 | 0x0 | 190 | — |
| STOP_PLAYER | 1 | 0x1 | 191 | — |
| PAUSE_PLAYER | 2 | 0x2 | 192 | — |
| RESUME_PLAYER | 3 | 0x3 | 193 | — |

#### AudioType

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| UNDEFINED | 0 | 0x0 | 205 | — |
| STREAM_IP_CALL | 1 | 0x1 | 206 | — |
| STREAM_MODEM_CALL | 2 | 0x2 | 207 | — |
| STREAM_AI_ASSISTANT | 3 | 0x3 | 208 | — |
| STREAM_RING | 4 | 0x4 | 209 | — |
| STREAM_NOTIFICATION | 5 | 0x5 | 210 | — |
| STREAM_TTS | 6 | 0x6 | 211 | — |
| STREAM_SYSTEM | 7 | 0x7 | 212 | — |
| STREAM_MICROPHONE | 9 | 0x9 | 213 | — |
| STREAM_NUM | 10 | 0xa | 214 | — |
| STREAM_CAST_MUSIC | 16 | 0x10 | 215 | — |

#### CALL_STATE

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| UNKNOWN_STATE | 0 | 0x0 | 219 | 未知状态 |
| IDLE | 1 | 0x1 | 220 | 空闲，已挂断 |
| RINGING | 2 | 0x2 | 221 | 响铃 |
| OFFHOOK | 3 | 0x3 | 222 | 通话中 |
| INCOMING | 4 | 0x4 | 223 | 来电中 |
| DIALING | 5 | 0x5 | 224 | 拨号中 |
| ALERTING | 6 | 0x6 | 225 | 拨号响铃中 |
| ACTIVE | 7 | 0x7 | 226 | 通话中 |
| HOLDING | 8 | 0x8 | 227 | 通话保持中 |

#### CustomKeyEvent.KeyCode

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| KEY_CODE_UNDEFINED | 0 | 0x0 | 271 | — |
| KEY_CODE_MAIN | 8103 | 0x1fa7 | 272 | — |
| KEY_CODE_TEL | 8104 | 0x1fa8 | 273 | — |
| KEY_CODE_NAVI | 8105 | 0x1fa9 | 274 | — |
| KEY_CODE_MEDIA | 8106 | 0x1faa | 275 | — |
| KEY_CODE_VR_START | 8107 | 0x1fab | 276 | — |
| KEY_CODE_VR_STOP | 8108 | 0x1fac | 277 | — |
| KEY_CODE_NAVI_QUIT | 8113 | 0x1fb1 | 278 | — |
| KEY_CODE_NEXT_FOCUS | 8114 | 0x1fb2 | 279 | — |
| KEY_CODE_PRE_FOCUS | 8115 | 0x1fb3 | 280 | — |
| KEY_CODE_IN_FOCUS | 8116 | 0x1fb4 | 281 | — |
| KEY_CODE_OUT_FOCUS | 8117 | 0x1fb5 | 282 | — |
| KEY_CODE_MEDIA_FAVOR | 8118 | 0x1fb6 | 283 | — |

#### VRCmdToPhone.VRCmd

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| VR_CMD_UNDEFINED | 0 | 0x0 | 293 | — |
| VR_CMD_MUSIC_PRE | 1 | 0x1 | 294 | — |
| VR_CMD_MUSIC_NEXT | 2 | 0x2 | 295 | — |
| VR_CMD_MUSIC_PAUSE | 3 | 0x3 | 296 | — |
| VR_CMD_MUSIC_PLAY | 4 | 0x4 | 297 | — |
| VR_CMD_CALL | 5 | 0x5 | 298 | — |
| VR_CMD_ENDCALL | 6 | 0x6 | 299 | — |
| VR_CMD_TEL | 7 | 0x7 | 300 | — |
| VR_CMD_MAP | 8 | 0x8 | 301 | — |
| VR_CMD_MUSIC | 9 | 0x9 | 302 | — |
| VR_CMD_VR_START | 10 | 0xa | 303 | — |
| VR_CMD_VR_STOP | 11 | 0xb | 304 | — |
| VR_CMD_NAVI_QUIT | 12 | 0xc | 305 | — |
| VR_CMD_NAVI_HOME | 13 | 0xd | 306 | — |
| VR_CMD_NAVI_COMPANY | 14 | 0xe | 307 | — |
| VR_CMD_BACK_HOMEPAGE | 15 | 0xf | 308 | — |

#### NotifySwitchDayOrNight.Mode

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| UNKNOWN | 0 | 0x0 | 320 | — |
| DAY | 1 | 0x1 | 321 | — |
| NIGHT | 2 | 0x2 | 322 | — |

#### BluetoothMacInfo.OPType

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| ADD | 0 | 0x0 | 353 | — |
| DELETE | 1 | 0x1 | 354 | — |

#### AppCategory

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| MAP | 0 | 0x0 | 399 | 地图导航类应用 |
| MEDIA | 1 | 0x1 | 400 | 音乐电台类应用 |
| VIDEO | 2 | 0x2 | 401 | 视频播放类应用 |
| IM | 3 | 0x3 | 402 | 社交通讯类应用 |
| NEWS | 4 | 0x4 | 403 | 新闻阅读类应用 |
| GAME | 5 | 0x5 | 404 | 游戏类应用 |
| SHOPPING | 6 | 0x6 | 405 | 网上购物类应用 |
| TRAVEL | 7 | 0x7 | 406 | 旅游出行类应用 |
| FINANCIAL | 8 | 0x8 | 407 | 金融理财类应用 |
| MEETING | 9 | 0x9 | 408 | 会议类应用 |
| TOOL | 10 | 0xa | 409 | 实用工具类应用 |
| OFFICE | 11 | 0xb | 410 | 办公软件类应用 |
| EDUCATION | 12 | 0xc | 411 | 教育学习类应用 |
| HEALTHY | 13 | 0xd | 412 | 医疗健康类应用 |
| SYSTEM | 14 | 0xe | 413 | 系统优化类应用 |
| LIFE | 15 | 0xf | 414 | 生活娱乐类应用 |
| SMART_SERVICE | 16 | 0x10 | 415 | 智慧类服务 |
| OTHER | 17 | 0x11 | 416 | 其它 |

#### AppInvokeCategory

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| START | 0 | 0x0 | 451 | — |
| STOP | 1 | 0x1 | 452 | — |
| PAUSE | 2 | 0x2 | 453 | — |
| RESUME | 3 | 0x3 | 454 | — |
| UPDATE | 4 | 0x4 | 455 | — |

#### AppStateCategory

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| STARTED | 0 | 0x0 | 459 | — |
| STOPPED | 1 | 0x1 | 460 | — |
| PAUSED | 2 | 0x2 | 461 | — |
| RESUMED | 3 | 0x3 | 462 | — |
| DESTROYED | 4 | 0x4 | 463 | — |

#### AppListChanged.AppListState

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| INSTALLED | 0 | 0x0 | 495 | — |
| REMOVED | 1 | 0x1 | 496 | — |
| UPDATED | 2 | 0x2 | 497 | — |

#### ShareNetworkAction

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| SHARE_NETWORK_STOP | 0 | 0x0 | 508 | — |
| SHARE_NETWORK_START | 1 | 0x1 | 509 | — |
| SHARE_NETWORK_RECONNECT | 2 | 0x2 | 510 | — |
| SHARE_NETWORK_RESTART | 3 | 0x3 | 511 | — |

#### LensFacing

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| LENS_FACING_FRONT | 0 | 0x0 | 683 | — |
| LENS_FACING_BACK | 1 | 0x1 | 684 | — |
| LENS_FACING_EXTERNAL | 2 | 0x2 | 685 | — |

#### Orientation

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| ORIENTATION_0 | 0 | 0x0 | 689 | — |
| ORIENTATION_90 | 90 | 0x5a | 690 | — |
| ORIENTATION_180 | 180 | 0xb4 | 691 | — |
| ORIENTATION_270 | 270 | 0x10e | 692 | — |

#### CameraAction

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| CAMERA_ACTION_OPEN | 0 | 0x0 | 696 | — |
| CAMERA_ACTION_CAPTURE | 1 | 0x1 | 697 | — |
| CAMERA_ACTION_CLOSE | 2 | 0x2 | 698 | — |

#### VideoType

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| VIDEO_UNDEFINED | 0 | 0x0 | 702 | — |
| VIDEO_CAST | 1 | 0x1 | 703 | — |
| VIDEO_COMMUNICATION | 2 | 0x2 | 704 | — |
| VIDEO_CAMERA_PREVIEW | 3 | 0x3 | 705 | — |
| VIDEO_CAMERA_PICTURE | 4 | 0x4 | 706 | — |

#### NotifyCameraStateChanged.State

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| OPENED | 0 | 0x0 | 742 | — |
| CLOSED | 1 | 0x1 | 743 | — |
| ERROR | 2 | 0x2 | 744 | — |
| PREEMPTED | 3 | 0x3 | 745 | — |
| NO_PERMISSION | 4 | 0x4 | 746 | — |
| BUSY | 5 | 0x5 | 747 | — |

#### POIDetailInfo.CoordinateType

| 名称 | 十进制值 | 十六进制值 | 源码行 | 包内注释 |
| --- | --- | --- | --- | --- |
| WGS84 | 0 | 0x0 | 757 | — |
| GCJ02 | 1 | 0x1 | 758 | — |
| BD09 | 2 | 0x2 | 759 | — |

## share.proto

原始文件：[source/share.proto](source/share.proto)。

### CheckStatus

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | step | uint32 | singular | 7 | 仅包内 schema | — |

### NotifyStatus

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | step | uint32 | singular | 11 | 仅包内 schema | — |
| 2 | status | uint32 | singular | 12 | 仅包内 schema | — |

### TaskInfo

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string | singular | 16 | 仅包内 schema | — |
| 2 | name | string | singular | 17 | 仅包内 schema | — |
| 3 | count | int32 | singular | 18 | 仅包内 schema | — |
| 4 | size | uint64 | singular | 19 | 仅包内 schema | — |
| 5 | thumbUri | string | singular | 20 | 仅包内 schema | — |
| 6 | imageFileCount | int32 | singular | 21 | 仅包内 schema | — |
| 7 | videoFileCount | int32 | singular | 22 | 仅包内 schema | — |
| 8 | audioFileCount | int32 | singular | 23 | 仅包内 schema | — |
| 9 | docFileCount | int32 | singular | 24 | 仅包内 schema | — |
| 10 | otherFileCount | int32 | singular | 25 | 仅包内 schema | — |
| 11 | imageFileSize | uint64 | singular | 26 | 仅包内 schema | — |
| 12 | videoFileSize | uint64 | singular | 27 | 仅包内 schema | — |
| 13 | audioFileSize | uint64 | singular | 28 | 仅包内 schema | — |
| 14 | docFileSize | uint64 | singular | 29 | 仅包内 schema | — |
| 15 | otherFileSize | uint64 | singular | 30 | 仅包内 schema | — |

### TaskAction

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string | singular | 34 | 仅包内 schema | — |
| 2 | action | uint32 | singular | 35 | 仅包内 schema | — |
| 3 | timeout | uint64 | singular | 36 | 仅包内 schema | — |

### ThumbRequest

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | fileUri | string | singular | 40 | 仅包内 schema | — |

### ThumbData

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | imageData | bytes | singular | 44 | 仅包内 schema | — |
| 2 | thumbSize | uint64 | singular | 45 | 仅包内 schema | — |

### DownloadIntention

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string | singular | 49 | 仅包内 schema | — |
| 2 | action | uint32 | singular | 50 | 仅包内 schema | — |

### FileInfo

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | name | string | singular | 54 | 仅包内 schema | — |
| 2 | size | uint64 | singular | 55 | 仅包内 schema | — |
| 3 | offset | uint64 | singular | 56 | 仅包内 schema | — |
| 4 | count | uint32 | singular | 57 | 仅包内 schema | — |
| 5 | content | bytes | singular | 58 | 仅包内 schema | — |

### DownloadFiles

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string | singular | 62 | 仅包内 schema | — |
| 2 | fileInfo | FileInfo | singular | 63 | 仅包内 schema | — |

### ShareIndex

| tag | 字段名 | 类型 | 声明 | 源码行 | 编译核对 | 包内注释 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | checkStatus | CheckStatus | singular | 67 | 仅包内 schema | — |
| 2 | notifyStatus | NotifyStatus | singular | 68 | 仅包内 schema | — |
| 3 | taskInfo | TaskInfo | singular | 69 | 仅包内 schema | — |
| 4 | taskAction | TaskAction | singular | 70 | 仅包内 schema | — |
| 5 | thumbRequest | ThumbRequest | singular | 71 | 仅包内 schema | — |
| 6 | thumbData | ThumbData | singular | 72 | 仅包内 schema | — |
| 7 | downloadIntention | DownloadIntention | singular | 73 | 仅包内 schema | — |
| 8 | fileInfo | FileInfo | singular | 74 | 仅包内 schema | — |
| 9 | downloadFiles | DownloadFiles | singular | 75 | 仅包内 schema | — |

### 枚举

