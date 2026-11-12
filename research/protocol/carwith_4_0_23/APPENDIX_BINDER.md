# 附录：完整 Binder 接口与方法

日期：2026-11-12。总计 122 个接口、616 个方法。签名来自 DEX；参数名称多数未保留，按参数类型/顺序记录。事务编号来自 `$Stub.TRANSACTION_*` 常量；`—` 表示未恢复，不按方法排列推断。

Binder 是 Android 本地跨进程接口。接口定义、exported 属性与权限需要结合；存在定义不代表普通第三方应用可绑定。

核心包前缀组：27 个接口，206 个方法。包前缀归类只表示直接相关，不能证明全部方法运行时使用。

## CarWith / CarLink / UCar / CarLife / EasyConn

### com.baidu.carlife.mixing.aidl.ICarLifeCastCallback

DEX：`classes.dex`。接口描述符：`Lcom/baidu/carlife/mixing/aidl/ICarLifeCastCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| addAudioListener | void addAudioListener(com.baidu.carlife.mixing.aidl.IRemoteAudioListener) | 12 |
| addKeyListener | void addKeyListener(com.baidu.carlife.mixing.aidl.IRemoteKeyListener) | 5 |
| addTouchListener | void addTouchListener(com.baidu.carlife.mixing.aidl.IRemoteTouchListener) | 3 |
| invokeMethod | android.os.Bundle invokeMethod(android.content.Intent) | 9 |
| notifyAudioState | void notifyAudioState(int) | 11 |
| notifyMusicProgress | void notifyMusicProgress(long) | 8 |
| onCastPrepared | void onCastPrepared(int) | 2 |
| onServiceDestroy | void onServiceDestroy() | 10 |
| onServiceReady | void onServiceReady() | 1 |
| removeAudioListener | void removeAudioListener(com.baidu.carlife.mixing.aidl.IRemoteAudioListener) | 13 |
| removeKeyListener | void removeKeyListener(com.baidu.carlife.mixing.aidl.IRemoteKeyListener) | 6 |
| removeTouchListener | void removeTouchListener(com.baidu.carlife.mixing.aidl.IRemoteTouchListener) | 4 |
| sendMusicInfo | void sendMusicInfo(com.baidu.carlife.mixing.MusicInfo) | 7 |

### com.baidu.carlife.mixing.aidl.ICarLifeCastManager

DEX：`classes.dex`。接口描述符：`Lcom/baidu/carlife/mixing/aidl/ICarLifeCastManager;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| invokeMethod | android.os.Bundle invokeMethod(android.content.Intent) | 5 |
| prepareCast | void prepareCast(com.baidu.carlife.mixing.CastConfig) | 1 |
| setCastCallback | void setCastCallback(com.baidu.carlife.mixing.aidl.ICarLifeCastCallback) | 4 |
| setSystemAudioCallback | void setSystemAudioCallback(com.baidu.carlife.mixing.aidl.ISystemAudioCallback) | 3 |
| stopCast | void stopCast() | 2 |

### com.baidu.carlife.mixing.aidl.IRemoteAudioListener

DEX：`classes.dex`。接口描述符：`Lcom/baidu/carlife/mixing/aidl/IRemoteAudioListener;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onReceiveAudioStream | void onReceiveAudioStream(byte[], int, int, int) | 1 |

### com.baidu.carlife.mixing.aidl.IRemoteKeyListener

DEX：`classes.dex`。接口描述符：`Lcom/baidu/carlife/mixing/aidl/IRemoteKeyListener;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onKeyEvent | boolean onKeyEvent(android.view.KeyEvent) | 1 |

### com.baidu.carlife.mixing.aidl.IRemoteTouchListener

DEX：`classes.dex`。接口描述符：`Lcom/baidu/carlife/mixing/aidl/IRemoteTouchListener;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onTouchEvent | boolean onTouchEvent(android.view.MotionEvent) | 1 |

### com.baidu.carlife.mixing.aidl.ISystemAudioCallback

DEX：`classes.dex`。接口描述符：`Lcom/baidu/carlife/mixing/aidl/ISystemAudioCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onAudioStateChange | void onAudioStateChange(int, int) | 2 |
| onAudioStreamReady | void onAudioStreamReady(byte[], int, int, int, int) | 1 |

### com.carwith.audio.services.IPhoneAudioCallback

DEX：`classes.dex`。接口描述符：`Lcom/carwith/audio/services/IPhoneAudioCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| controlAudioPlayer | void controlAudioPlayer(int, int, int) | 15 |
| disConnect | void disConnect() | 3 |
| onError | void onError(int, java.lang.String) | 2 |
| onNetConnect | void onNetConnect() | 5 |
| sendAudioData | void sendAudioData(byte[], int) | 4 |
| sendCurrentPhoneState | void sendCurrentPhoneState(int, boolean) | 8 |
| sendMicrophoneState | boolean sendMicrophoneState(boolean, int, int, int) | 6 |
| setAudioPlayerState | boolean setAudioPlayerState(int, int, int, int, int, java.lang.String) | 7 |
| setAudioPort | void setAudioPort(int) | 1 |
| setCarCallInitState | void setCarCallInitState(boolean, boolean) | 10 |
| setCarMicMuteState | void setCarMicMuteState(boolean) | 13 |
| setHFPSupportStatus | void setHFPSupportStatus(boolean) | 11 |
| setIsMonitoring | void setIsMonitoring(boolean) | 14 |
| setPhoneAudioState | void setPhoneAudioState(boolean, boolean, boolean, boolean, boolean) | 9 |
| setWiredHeadStatus | void setWiredHeadStatus(boolean) | 12 |

### com.carwith.audio.services.IPhoneAudioCast

DEX：`classes.dex`。接口描述符：`Lcom/carwith/audio/services/IPhoneAudioCast;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| initNetwork | void initNetwork() | 4 |
| onAudioData | void onAudioData(byte[]) | 2 |
| onAuthAndControlChannelReady | void onAuthAndControlChannelReady() | 14 |
| onNetError | void onNetError(int, java.lang.String) | 3 |
| readAssistantRecorderData | int readAssistantRecorderData(byte[]) | 7 |
| setCallback | void setCallback(com.carwith.audio.services.IPhoneAudioCallback) | 1 |
| setCarMicrophoneMuteState | void setCarMicrophoneMuteState(boolean) | 16 |
| startAssistantRecorder | void startAssistantRecorder(boolean) | 6 |
| startToRecord | void startToRecord() | 12 |
| stopService | void stopService() | 5 |
| stopToRecord | void stopToRecord() | 13 |
| switchAudioSourceToBluetooth | void switchAudioSourceToBluetooth() | 10 |
| switchAudioSourceToCar | void switchAudioSourceToCar() | 8 |
| switchAudioSourceToPhone | void switchAudioSourceToPhone() | 9 |
| switchAudioSourceToPhoneHeadSet | void switchAudioSourceToPhoneHeadSet() | 15 |
| switchAudioSourceToWired | void switchAudioSourceToWired() | 11 |

### com.carwith.dialer.recorder.ICallRecorderCommand

DEX：`classes2.dex`。接口描述符：`Lcom/carwith/dialer/recorder/ICallRecorderCommand;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| basicTypes | void basicTypes(int, long, boolean, float, double, java.lang.String) | 1 |
| checkCallRecordTime | long checkCallRecordTime() | 4 |
| isBound | boolean isBound() | 7 |
| isRecording | boolean isRecording() | 8 |
| registerCallback | void registerCallback(com.carwith.dialer.recorder.IRecorderCallback) | 5 |
| startCallRecord | void startCallRecord(java.lang.String, java.lang.String) | 2 |
| stopCallRecord | void stopCallRecord() | 3 |
| unregisterCallback | void unregisterCallback(com.carwith.dialer.recorder.IRecorderCallback) | 6 |

### com.carwith.dialer.recorder.IRecorderCallback

DEX：`classes2.dex`。接口描述符：`Lcom/carwith/dialer/recorder/IRecorderCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| basicTypes | void basicTypes(int, long, boolean, float, double, java.lang.String) | 1 |
| onCallRecorderError | void onCallRecorderError(int) | 4 |
| onCallRecorderStarted | void onCallRecorderStarted(java.lang.String) | 2 |
| onCallRecorderStoped | void onCallRecorderStoped(int, java.lang.String) | 3 |
| onCheckRecordTime | void onCheckRecordTime(long) | 5 |

### com.miui.carlink.castfwk.ICarlinkService

DEX：`classes4.dex`。接口描述符：`Lcom/miui/carlink/castfwk/ICarlinkService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| castToDevice | void castToDevice(java.lang.String, java.lang.String, java.lang.String, int) | 1 |
| getCarDensity | int getCarDensity() | 4 |
| getVirtualDisplayId | int getVirtualDisplayId() | 3 |
| setSecondaryVirtualDisplayId | void setSecondaryVirtualDisplayId(int) | 2 |

### com.miui.carlink.databus.IChannelCreationCallback

DEX：`classes4.dex`。接口描述符：`Lcom/miui/carlink/databus/IChannelCreationCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onChannelCreated | void onChannelCreated(int, boolean) | 1 |

### com.miui.carlink.databus.IDataBusService

DEX：`classes4.dex`。接口描述符：`Lcom/miui/carlink/databus/IDataBusService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| backToCarForeground | void backToCarForeground() | 16 |
| getCarLifeCallActive | boolean getCarLifeCallActive() | 28 |
| getIsCarMicMute | boolean getIsCarMicMute() | 27 |
| getIsCompleteCallSwitch | boolean getIsCompleteCallSwitch() | 25 |
| getIsPhoneAudio | boolean[] getIsPhoneAudio() | 24 |
| goToCarDesktop | void goToCarDesktop() | 15 |
| notifyDisconnectByUser | void notifyDisconnectByUser(com.miui.carlink.databus.INotifyDisconnectCallback) | 4 |
| notifyRotationChanged | boolean notifyRotationChanged(int) | 5 |
| readAssistantRecorderData | int readAssistantRecorderData(byte[]) | 13 |
| registCarSensorObserver | boolean registCarSensorObserver(com.miui.carlink.databus.IDataObserver) | 1 |
| registerChannelCreationCallback | void registerChannelCreationCallback(com.miui.carlink.databus.IChannelCreationCallback) | 30 |
| registerPauseAndResumeVideoStreamCallback | void registerPauseAndResumeVideoStreamCallback(com.miui.carlink.databus.IPauseAndResumeVideoStreamCallback) | 31 |
| sendAppListChanged | void sendAppListChanged(int[], java.lang.String) | 33 |
| sendAppStateChanged | void sendAppStateChanged(int, int, boolean, int, long, com.miui.carlink.databus.IDisplayVisibleRegionWrapper, boolean) | 32 |
| sendMicrophoneState | void sendMicrophoneState(boolean, int, int, int) | 8 |
| sendMusicInfoToCar | boolean sendMusicInfoToCar(com.miui.carlink.databus.p2cdatastructure.MusicInfo) | 10 |
| sendNavigationInfoToCar | boolean sendNavigationInfoToCar(com.miui.carlink.databus.p2cdatastructure.NavigationInfo) | 11 |
| sendPhoneStateToCar | boolean sendPhoneStateToCar(com.miui.carlink.databus.p2cdatastructure.PhoneState) | 12 |
| setAudioSvrPort | void setAudioSvrPort(int) | 7 |
| setCarMicMuteState | void setCarMicMuteState() | 26 |
| setDeviceId | void setDeviceId(java.lang.String) | 35 |
| setFloatWindowPosition | void setFloatWindowPosition(android.graphics.Point, android.graphics.Point) | 9 |
| setIsIgnoreKeyBack | void setIsIgnoreKeyBack(boolean) | 34 |
| setVoiceAssistantActive | void setVoiceAssistantActive(boolean) | 29 |
| start | void start(int, java.lang.String) | 2 |
| startAssistantRecorder | void startAssistantRecorder(boolean) | 14 |
| startHeartBeatThread | void startHeartBeatThread(boolean) | 6 |
| startToRecord | void startToRecord() | 22 |
| stop | void stop(com.miui.carlink.databus.INotifyDisconnectCallback) | 3 |
| stopToRecord | void stopToRecord() | 23 |
| switchAudioSourceToCar | void switchAudioSourceToCar() | 17 |
| switchAudioSourceToPhone | void switchAudioSourceToPhone() | 18 |
| switchAudioSourceToPhoneHeadSet | void switchAudioSourceToPhoneHeadSet() | 20 |
| switchAudioToBluetooth | void switchAudioToBluetooth() | 19 |
| switchAudioToWired | void switchAudioToWired() | 21 |

### com.miui.carlink.databus.IDataObserver

DEX：`classes4.dex`。接口描述符：`Lcom/miui/carlink/databus/IDataObserver;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| callUpPhone | void callUpPhone() | 16 |
| favourCurrentMusic | void favourCurrentMusic() | 28 |
| handleMediaKeyCode | void handleMediaKeyCode(int) | 26 |
| handleUndefineVRCmd | void handleUndefineVRCmd(java.lang.String) | 25 |
| hangUpPhone | void hangUpPhone() | 17 |
| navigationGoCompany | void navigationGoCompany() | 19 |
| navigationGoHome | void navigationGoHome() | 18 |
| onAccInfoChanged | void onAccInfoChanged(com.miui.carlink.databus.sensor.AccInfo) | 2 |
| onAwakenVoiceAssistant | void onAwakenVoiceAssistant(byte[], int, int, int) | 10 |
| onCarBackKey | void onCarBackKey() | 30 |
| onCloseVoiceAssistant | void onCloseVoiceAssistant() | 11 |
| onGearInfoChanged | void onGearInfoChanged(com.miui.carlink.databus.sensor.GearInfo) | 4 |
| onGpsInfoChagned | void onGpsInfoChagned(com.miui.carlink.databus.sensor.GpsInfo) | 1 |
| onGyroInfoChagned | void onGyroInfoChagned(com.miui.carlink.databus.sensor.GyroInfo) | 5 |
| onLightSensorInfoChanged | void onLightSensorInfoChanged(com.miui.carlink.databus.sensor.LightSensorInfo) | 7 |
| onLightsInfoChanged | void onLightsInfoChanged(com.miui.carlink.databus.sensor.LightsInfo) | 3 |
| onNotificationClick | void onNotificationClick(int, int) | 29 |
| onNotifyCallHungUpChanged | void onNotifyCallHungUpChanged() | 8 |
| onOilInfoChanged | void onOilInfoChanged(com.miui.carlink.databus.sensor.OilInfo) | 6 |
| onSwitchDayOrNightChanged | void onSwitchDayOrNightChanged(int) | 9 |
| openLauncherView | void openLauncherView() | 23 |
| openMap | void openMap() | 21 |
| openMediaAppView | void openMediaAppView() | 22 |
| openTelecomView | void openTelecomView() | 24 |
| operationAppDisplay | boolean operationAppDisplay(int, int, int) | 27 |
| pauseMedia | void pauseMedia() | 15 |
| playMedia | void playMedia() | 14 |
| quitNavigation | void quitNavigation() | 20 |
| skipToMusicNext | void skipToMusicNext() | 13 |
| skipToMusicPrevious | void skipToMusicPrevious() | 12 |

### com.miui.carlink.databus.IDisplayVisibleRegionWrapper

DEX：`classes4.dex`。接口描述符：`Lcom/miui/carlink/databus/IDisplayVisibleRegionWrapper;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getBottom | int getBottom() | 7 |
| getLeft | int getLeft() | 4 |
| getMode | int getMode() | 1 |
| getOriginHeight | int getOriginHeight() | 3 |
| getOriginWidth | int getOriginWidth() | 2 |
| getRight | int getRight() | 6 |
| getTop | int getTop() | 5 |

### com.miui.carlink.databus.INotifyDisconnectCallback

DEX：`classes4.dex`。接口描述符：`Lcom/miui/carlink/databus/INotifyDisconnectCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onComplete | void onComplete() | 1 |
| onNotifyCarDisconnect | void onNotifyCarDisconnect() | 2 |

### com.miui.carlink.databus.IPauseAndResumeVideoStreamCallback

DEX：`classes4.dex`。接口描述符：`Lcom/miui/carlink/databus/IPauseAndResumeVideoStreamCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| pauseVideoStreamCallback | void pauseVideoStreamCallback() | 1 |
| resumeVideoStreamCallback | void resumeVideoStreamCallback(boolean) | 2 |

### com.ucar.app.ability.IUCarAbilityService

DEX：`classes4.dex`。接口描述符：`Lcom/ucar/app/ability/IUCarAbilityService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| dial | boolean dial(android.os.Bundle) | 2 |
| navigate | void navigate(android.os.Bundle) | 1 |

### com.ucar.map.IUCarMapAppService

DEX：`classes5.dex`。接口描述符：`Lcom/ucar/map/IUCarMapAppService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getValue | android.os.Bundle getValue(int, android.os.Bundle) | 2 |
| setValue | void setValue(int, android.os.Bundle) | 1 |

### com.ucar.map.IUCarMapCallback

DEX：`classes5.dex`。接口描述符：`Lcom/ucar/map/IUCarMapCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getCommuterAddress | android.os.Bundle getCommuterAddress() | 1 |
| getUIMode | int getUIMode() | 5 |
| getValue | android.os.Bundle getValue(int, android.os.Bundle) | 4 |
| onUCarModeStateChange | void onUCarModeStateChange(boolean) | 2 |
| setValue | void setValue(int, android.os.Bundle) | 3 |

### com.ucar.map.IUCarMapService

DEX：`classes5.dex`。接口描述符：`Lcom/ucar/map/IUCarMapService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getValue | android.os.Bundle getValue(int, android.os.Bundle) | 8 |
| notifyCommuterAddressChanged | void notifyCommuterAddressChanged(boolean, boolean, android.os.Bundle) | 6 |
| notifyMapUIModeChanged | void notifyMapUIModeChanged(int, android.os.Bundle) | 9 |
| notifyNavStatusChanged | void notifyNavStatusChanged(boolean, android.os.Bundle) | 5 |
| notifyStatusChanged | void notifyStatusChanged(int, android.os.Bundle) | 10 |
| registerMapCallback | void registerMapCallback(com.ucar.map.IUCarMapCallback) | 1 |
| removeNavInfo | void removeNavInfo(android.os.Bundle) | 4 |
| setValue | void setValue(int, android.os.Bundle) | 7 |
| showNavInfo | void showNavInfo(android.os.Bundle, android.os.Bundle) | 3 |
| unregisterMapCallback | void unregisterMapCallback() | 2 |

### com.ucar.sdk.IShareObserver

DEX：`classes5.dex`。接口描述符：`Lcom/ucar/sdk/IShareObserver;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onReceiverTask | void onReceiverTask(com.ucar.sdk.bean.TaskInfo, byte[]) | 6 |
| onStarted | void onStarted() | 1 |
| onTaskCancel | void onTaskCancel(int) | 7 |
| onTransmitFinish | void onTransmitFinish(boolean, java.lang.String, java.lang.String) | 4 |
| onTransmitInterrupt | void onTransmitInterrupt(boolean, java.lang.String, int, int, int) | 3 |
| onTransmitProgress | void onTransmitProgress(boolean, java.lang.String, long, long) | 5 |
| onTransmitStatusChange | void onTransmitStatusChange(boolean, java.lang.String, int) | 2 |

### com.ucar.sdk.IShareService

DEX：`classes5.dex`。接口描述符：`Lcom/ucar/sdk/IShareService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| cancelTransmit | void cancelTransmit(java.lang.String) | 5 |
| download | void download(com.ucar.sdk.bean.TaskInfo) | 9 |
| getRemoteDevice | com.ucar.sdk.bean.DeviceInfo getRemoteDevice() | 3 |
| getStorePath | java.lang.String getStorePath() | 7 |
| getTransmitStatus | int getTransmitStatus(java.lang.String) | 6 |
| registerShareObserver | void registerShareObserver(com.ucar.sdk.IShareObserver) | 1 |
| setStorePath | boolean setStorePath(java.lang.String) | 8 |
| startTransmit | void startTransmit(java.lang.String, java.util.List) | 4 |
| unregisterShareObserver | void unregisterShareObserver(com.ucar.sdk.IShareObserver) | 2 |

### net.easyconn.carman.sdk.IDataCallback

DEX：`classes8.dex`。接口描述符：`Lnet/easyconn/carman/sdk/IDataCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| isForeground | boolean isForeground() | — |
| isPresentationShow | boolean isPresentationShow() | — |
| isReceiveAudioData | boolean isReceiveAudioData() | — |
| onConnectStatusChange | void onConnectStatusChange(boolean) | — |
| sendCaptureConfig | void sendCaptureConfig(int, int, android.view.Surface) | — |
| sendMemoryFile | void sendMemoryFile(android.os.ParcelFileDescriptor, int) | — |
| sendSharedMemory | void sendSharedMemory(android.os.SharedMemory) | — |
| sendTouchEvent | void sendTouchEvent(android.view.MotionEvent) | — |

### net.easyconn.carman.sdk.IPxcConnectServiceInterface

DEX：`classes8.dex`。接口描述符：`Lnet/easyconn/carman/sdk/IPxcConnectServiceInterface;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| isForeground | boolean isForeground() | — |
| onNotificationContent | void onNotificationContent(java.lang.String) | — |
| onPXCConnect | void onPXCConnect() | — |
| onPXCDisconnect | void onPXCDisconnect() | — |
| onProjectionConnected | void onProjectionConnected() | — |
| onProjectionDisconnected | void onProjectionDisconnected() | — |

### net.easyconn.carman.sdk.IRemoteService

DEX：`classes8.dex`。接口描述符：`Lnet/easyconn/carman/sdk/IRemoteService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| processAudio | void processAudio(byte[], int) | — |
| setAppStatus | void setAppStatus(java.lang.String, boolean) | — |
| setCallback | void setCallback(java.lang.String, boolean, net.easyconn.carman.sdk.IDataCallback) | — |
| setPresentationStatus | void setPresentationStatus(java.lang.String, boolean) | — |
| startAudio | void startAudio(int, int, int) | — |
| startCarMICRecord | void startCarMICRecord(boolean) | — |
| stopAudio | void stopAudio() | — |

### net.easyconn.carman.sdk.ISocksInterface

DEX：`classes8.dex`。接口描述符：`Lnet/easyconn/carman/sdk/ISocksInterface;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| start | void start(java.lang.String, java.lang.String) | — |
| stop | void stop() | — |

## 系统镜像与其它 SDK

### android.app.IMiuiActivityObserver

DEX：`classes.dex`。接口描述符：`Landroid/app/IMiuiActivityObserver;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| activityDestroyed | void activityDestroyed(android.content.Intent) | 5 |
| activityIdle | void activityIdle(android.content.Intent) | 1 |
| activityPaused | void activityPaused(android.content.Intent) | 3 |
| activityResumed | void activityResumed(android.content.Intent) | 2 |
| activityStopped | void activityStopped(android.content.Intent) | 4 |

### android.app.ITaskStackListener

DEX：`classes.dex`。接口描述符：`Landroid/app/ITaskStackListener;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onActivityDismissingDockedTask | void onActivityDismissingDockedTask() | 6 |
| onActivityForcedResizable | void onActivityForcedResizable(java.lang.String, int, int) | 5 |
| onActivityLaunchOnSecondaryDisplayFailed | void onActivityLaunchOnSecondaryDisplayFailed(android.app.ActivityManager$RunningTaskInfo, int) | 7 |
| onActivityLaunchOnSecondaryDisplayRerouted | void onActivityLaunchOnSecondaryDisplayRerouted(android.app.ActivityManager$RunningTaskInfo, int) | 8 |
| onActivityPinned | void onActivityPinned(java.lang.String, int, int, int) | 2 |
| onActivityRequestedOrientationChanged | void onActivityRequestedOrientationChanged(int, int) | 13 |
| onActivityRestartAttempt | void onActivityRestartAttempt(android.app.ActivityManager$RunningTaskInfo, boolean, boolean, boolean) | 4 |
| onActivityRotation | void onActivityRotation(int) | 23 |
| onActivityUnpinned | void onActivityUnpinned() | 3 |
| onBackPressedOnTaskRoot | void onBackPressedOnTaskRoot(android.app.ActivityManager$RunningTaskInfo) | 17 |
| onLockTaskModeChanged | void onLockTaskModeChanged(int) | 25 |
| onRecentTaskListFrozenChanged | void onRecentTaskListFrozenChanged(boolean) | 20 |
| onRecentTaskListUpdated | void onRecentTaskListUpdated() | 19 |
| onTaskCreated | void onTaskCreated(int, android.content.ComponentName) | 9 |
| onTaskDescriptionChanged | void onTaskDescriptionChanged(android.app.ActivityManager$RunningTaskInfo) | 12 |
| onTaskDisplayChanged | void onTaskDisplayChanged(int, int) | 18 |
| onTaskFocusChanged | void onTaskFocusChanged(int, boolean) | 21 |
| onTaskMovedToBack | void onTaskMovedToBack(android.app.ActivityManager$RunningTaskInfo) | 24 |
| onTaskMovedToFront | void onTaskMovedToFront(android.app.ActivityManager$RunningTaskInfo) | 11 |
| onTaskProfileLocked | void onTaskProfileLocked(android.app.ActivityManager$RunningTaskInfo, int) | 15 |
| onTaskRemovalStarted | void onTaskRemovalStarted(android.app.ActivityManager$RunningTaskInfo) | 14 |
| onTaskRemoved | void onTaskRemoved(int) | 10 |
| onTaskRequestedOrientationChanged | void onTaskRequestedOrientationChanged(int, int) | 22 |
| onTaskSnapshotChanged | void onTaskSnapshotChanged(int) | 16 |
| onTaskStackChanged | void onTaskStackChanged() | 1 |

### android.support.v4.app.INotificationSideChannel

DEX：`classes.dex`。接口描述符：`Landroid/support/v4/app/INotificationSideChannel;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| cancel | void cancel(java.lang.String, int, java.lang.String) | 2 |
| cancelAll | void cancelAll(java.lang.String) | 3 |
| notify | void notify(java.lang.String, int, java.lang.String, android.app.Notification) | 1 |

### android.support.v4.media.session.IMediaControllerCallback

DEX：`classes.dex`。接口描述符：`Landroid/support/v4/media/session/IMediaControllerCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onCaptioningEnabledChanged | void onCaptioningEnabledChanged(boolean) | 11 |
| onEvent | void onEvent(java.lang.String, android.os.Bundle) | 1 |
| onExtrasChanged | void onExtrasChanged(android.os.Bundle) | 7 |
| onMetadataChanged | void onMetadataChanged(android.support.v4.media.MediaMetadataCompat) | 4 |
| onPlaybackStateChanged | void onPlaybackStateChanged(android.support.v4.media.session.PlaybackStateCompat) | 3 |
| onQueueChanged | void onQueueChanged(java.util.List) | 5 |
| onQueueTitleChanged | void onQueueTitleChanged(java.lang.CharSequence) | 6 |
| onRepeatModeChanged | void onRepeatModeChanged(int) | 9 |
| onSessionDestroyed | void onSessionDestroyed() | 2 |
| onSessionReady | void onSessionReady() | 13 |
| onShuffleModeChanged | void onShuffleModeChanged(int) | 12 |
| onShuffleModeChangedRemoved | void onShuffleModeChangedRemoved(boolean) | 10 |
| onVolumeInfoChanged | void onVolumeInfoChanged(android.support.v4.media.session.ParcelableVolumeInfo) | 8 |

### android.support.v4.media.session.IMediaSession

DEX：`classes.dex`。接口描述符：`Landroid/support/v4/media/session/IMediaSession;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| addQueueItem | void addQueueItem(android.support.v4.media.MediaDescriptionCompat) | 41 |
| addQueueItemAt | void addQueueItemAt(android.support.v4.media.MediaDescriptionCompat, int) | 42 |
| adjustVolume | void adjustVolume(int, int, java.lang.String) | 11 |
| fastForward | void fastForward() | 22 |
| getExtras | android.os.Bundle getExtras() | 31 |
| getFlags | long getFlags() | 9 |
| getLaunchPendingIntent | android.app.PendingIntent getLaunchPendingIntent() | 8 |
| getMetadata | android.support.v4.media.MediaMetadataCompat getMetadata() | 27 |
| getPackageName | java.lang.String getPackageName() | 6 |
| getPlaybackState | android.support.v4.media.session.PlaybackStateCompat getPlaybackState() | 28 |
| getQueue | java.util.List getQueue() | 29 |
| getQueueTitle | java.lang.CharSequence getQueueTitle() | 30 |
| getRatingType | int getRatingType() | 32 |
| getRepeatMode | int getRepeatMode() | 37 |
| getShuffleMode | int getShuffleMode() | 47 |
| getTag | java.lang.String getTag() | 7 |
| getVolumeAttributes | android.support.v4.media.session.ParcelableVolumeInfo getVolumeAttributes() | 10 |
| isCaptioningEnabled | boolean isCaptioningEnabled() | 45 |
| isShuffleModeEnabledRemoved | boolean isShuffleModeEnabledRemoved() | 38 |
| isTransportControlEnabled | boolean isTransportControlEnabled() | 5 |
| next | void next() | 20 |
| pause | void pause() | 18 |
| play | void play() | 13 |
| playFromMediaId | void playFromMediaId(java.lang.String, android.os.Bundle) | 14 |
| playFromSearch | void playFromSearch(java.lang.String, android.os.Bundle) | 15 |
| playFromUri | void playFromUri(android.net.Uri, android.os.Bundle) | 16 |
| prepare | void prepare() | 33 |
| prepareFromMediaId | void prepareFromMediaId(java.lang.String, android.os.Bundle) | 34 |
| prepareFromSearch | void prepareFromSearch(java.lang.String, android.os.Bundle) | 35 |
| prepareFromUri | void prepareFromUri(android.net.Uri, android.os.Bundle) | 36 |
| previous | void previous() | 21 |
| rate | void rate(android.support.v4.media.RatingCompat) | 25 |
| rateWithExtras | void rateWithExtras(android.support.v4.media.RatingCompat, android.os.Bundle) | 51 |
| registerCallbackListener | void registerCallbackListener(android.support.v4.media.session.IMediaControllerCallback) | 3 |
| removeQueueItem | void removeQueueItem(android.support.v4.media.MediaDescriptionCompat) | 43 |
| removeQueueItemAt | void removeQueueItemAt(int) | 44 |
| rewind | void rewind() | 23 |
| seekTo | void seekTo(long) | 24 |
| sendCommand | void sendCommand(java.lang.String, android.os.Bundle, android.support.v4.media.session.MediaSessionCompat$ResultReceiverWrapper) | 1 |
| sendCustomAction | void sendCustomAction(java.lang.String, android.os.Bundle) | 26 |
| sendMediaButton | boolean sendMediaButton(android.view.KeyEvent) | 2 |
| setCaptioningEnabled | void setCaptioningEnabled(boolean) | 46 |
| setRepeatMode | void setRepeatMode(int) | 39 |
| setShuffleMode | void setShuffleMode(int) | 48 |
| setShuffleModeEnabledRemoved | void setShuffleModeEnabledRemoved(boolean) | 40 |
| setVolumeTo | void setVolumeTo(int, int, java.lang.String) | 12 |
| skipToQueueItem | void skipToQueueItem(long) | 17 |
| stop | void stop() | 19 |
| unregisterCallbackListener | void unregisterCallbackListener(android.support.v4.media.session.IMediaControllerCallback) | 4 |

### android.support.v4.os.IResultReceiver

DEX：`classes.dex`。接口描述符：`Landroid/support/v4/os/IResultReceiver;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| send | void send(int, android.os.Bundle) | 1 |

### android.view.IDisplayFoldListener

DEX：`classes.dex`。接口描述符：`Landroid/view/IDisplayFoldListener;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onDisplayFoldChanged | void onDisplayFoldChanged(int, boolean) | 1 |

### android.view.IDisplayWindowListener

DEX：`classes.dex`。接口描述符：`Landroid/view/IDisplayWindowListener;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onDisplayAdded | void onDisplayAdded(int) | 1 |
| onDisplayConfigurationChanged | void onDisplayConfigurationChanged(int, android.content.res.Configuration) | 2 |
| onDisplayRemoved | void onDisplayRemoved(int) | 3 |
| onFixedRotationFinished | void onFixedRotationFinished(int) | 5 |
| onFixedRotationStarted | void onFixedRotationStarted(int, int) | 4 |
| onKeepClearAreasChanged | void onKeepClearAreasChanged(int, java.util.List, java.util.List) | 6 |

### android.view.IRotationWatcher

DEX：`classes.dex`。接口描述符：`Landroid/view/IRotationWatcher;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onRotationChanged | void onRotationChanged(int) | 1 |

### androidx.core.app.unusedapprestrictions.IUnusedAppRestrictionsBackportCallback

DEX：`classes.dex`。接口描述符：`Landroidx/core/app/unusedapprestrictions/IUnusedAppRestrictionsBackportCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onIsPermissionRevocationEnabledForAppResult | void onIsPermissionRevocationEnabledForAppResult(boolean, boolean) | 1 |

### androidx.core.app.unusedapprestrictions.IUnusedAppRestrictionsBackportService

DEX：`classes.dex`。接口描述符：`Landroidx/core/app/unusedapprestrictions/IUnusedAppRestrictionsBackportService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| isPermissionRevocationEnabledForApp | void isPermissionRevocationEnabledForApp(androidx.core.app.unusedapprestrictions.IUnusedAppRestrictionsBackportCallback) | 1 |

### com.android.bluetooth.ble.app.IMiuiNearbyApiServiceV2

DEX：`classes.dex`。接口描述符：`Lcom/android/bluetooth/ble/app/IMiuiNearbyApiServiceV2;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| clearNearbyConnectionConfig | boolean clearNearbyConnectionConfig(java.lang.String) | 4 |
| clearScanConfig | boolean clearScanConfig(java.lang.String, java.lang.String) | 3 |
| getVersionCode | int getVersionCode() | 7 |
| notifyConnectionStatus | void notifyConnectionStatus(java.lang.String, int, java.lang.String) | 5 |
| setMiuiNearbyConnectionListenerConfig | int setMiuiNearbyConnectionListenerConfig(java.lang.String, java.lang.String, java.lang.String) | 2 |
| setMiuiNearbyScanConfig | int setMiuiNearbyScanConfig(com.android.bluetooth.ble.app.IMiuiNearbyScanCallbackV2, java.lang.String, java.lang.String, int, byte[], byte[], java.lang.String, java.lang.String, java.lang.String, java.lang.String, byte[], byte[]) | 1 |
| setMiuiNearbyScanConfigWithPara | int setMiuiNearbyScanConfigWithPara(com.android.bluetooth.ble.app.IMiuiNearbyScanCallbackParaV2, java.lang.String, java.lang.String, java.lang.String, java.lang.String) | 6 |

### com.android.bluetooth.ble.app.IMiuiNearbyScanCallbackParaV2

DEX：`classes.dex`。接口描述符：`Lcom/android/bluetooth/ble/app/IMiuiNearbyScanCallbackParaV2;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onDeviceFound | void onDeviceFound(android.bluetooth.le.ScanResult) | 3 |
| onScanStart | void onScanStart() | 1 |
| onScanStop | void onScanStop() | 2 |

### com.android.bluetooth.ble.app.IMiuiNearbyScanCallbackV2

DEX：`classes.dex`。接口描述符：`Lcom/android/bluetooth/ble/app/IMiuiNearbyScanCallbackV2;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onDeviceFound | void onDeviceFound(android.bluetooth.le.ScanResult, com.android.bluetooth.ble.app.MiuiNearbyScanInfoV2) | 3 |
| onScanStart | void onScanStart() | 1 |
| onScanStop | void onScanStop() | 2 |

### miui.car.ISecureChangedCallback

DEX：`classes.dex`。接口描述符：`Lmiui/car/ISecureChangedCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onSecureChangeCallback | void onSecureChangeCallback(java.lang.String, boolean) | 1 |

### miui.cloud.sync.IRemoteFileSyncLogger

DEX：`classes.dex`。接口描述符：`Lmiui/cloud/sync/IRemoteFileSyncLogger;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| release | void release(android.os.ResultReceiver) | 2 |
| syncLog | void syncLog(java.lang.String, java.lang.String) | 1 |

### miui.net.IXiaomiAuthService

DEX：`classes.dex`。接口描述符：`Lmiui/net/IXiaomiAuthService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getMiCloudAccessToken | android.os.Bundle getMiCloudAccessToken(android.accounts.Account, android.os.Bundle) | 2 |
| getMiCloudUserInfo | android.os.Bundle getMiCloudUserInfo(android.accounts.Account, android.os.Bundle) | 1 |
| getSnsAccessToken | android.os.Bundle getSnsAccessToken(android.accounts.Account, android.os.Bundle) | 3 |
| invalidateAccessToken | void invalidateAccessToken(android.accounts.Account, android.os.Bundle) | 4 |

### miuix.appcompat.app.floatingactivity.multiapp.IFloatingService

DEX：`classes.dex`。接口描述符：`Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| callServiceMethod | android.os.Bundle callServiceMethod(int, android.os.Bundle) | 2 |
| registerServiceNotify | int registerServiceNotify(miuix.appcompat.app.floatingactivity.multiapp.IServiceNotify, java.lang.String) | 3 |
| unregisterServiceNotify | void unregisterServiceNotify(miuix.appcompat.app.floatingactivity.multiapp.IServiceNotify, java.lang.String) | 4 |
| upDateRemoteActivityInfo | void upDateRemoteActivityInfo(java.lang.String, int) | — |

### miuix.appcompat.app.floatingactivity.multiapp.IServiceNotify

DEX：`classes.dex`。接口描述符：`Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| notifyFromService | android.os.Bundle notifyFromService(int, android.os.Bundle) | 1 |

### com.kugou.android.third.api.IKGMusicApi

DEX：`classes3.dex`。接口描述符：`Lcom/kugou/android/third/api/IKGMusicApi;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| execute | android.os.Bundle execute(java.lang.String, android.os.Bundle) | 1 |
| executeAsync | void executeAsync(java.lang.String, android.os.Bundle, com.kugou.android.third.api.IKGMusicApiCallback) | 2 |
| registerEventListener | android.os.Bundle registerEventListener(java.util.List, com.kugou.android.third.api.IKGMusicApiEventListener) | 3 |
| unregisterEventListener | android.os.Bundle unregisterEventListener(java.util.List, com.kugou.android.third.api.IKGMusicApiEventListener) | 4 |

### com.kugou.android.third.api.IKGMusicApiCallback

DEX：`classes3.dex`。接口描述符：`Lcom/kugou/android/third/api/IKGMusicApiCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onResult | void onResult(android.os.Bundle) | 1 |

### com.kugou.android.third.api.IKGMusicApiEventListener

DEX：`classes3.dex`。接口描述符：`Lcom/kugou/android/third/api/IKGMusicApiEventListener;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onEvent | void onEvent(java.lang.String, android.os.Bundle) | 1 |

### com.market.pm.IMarketInstallerService

DEX：`classes3.dex`。接口描述符：`Lcom/market/pm/IMarketInstallerService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| installPackage | void installPackage(android.net.Uri, android.os.ResultReceiver, android.os.Bundle) | 1 |

### com.market.sdk.IDesktopRecommendResponse

DEX：`classes3.dex`。接口描述符：`Lcom/market/sdk/IDesktopRecommendResponse;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onLoadFailed | void onLoadFailed() | 2 |
| onLoadSuccess | void onLoadSuccess(com.market.sdk.DesktopRecommendInfo) | 1 |

### com.market.sdk.IImageCallback

DEX：`classes3.dex`。接口描述符：`Lcom/market/sdk/IImageCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onImageLoadFailed | void onImageLoadFailed(java.lang.String) | 2 |
| onImageLoadSuccess | void onImageLoadSuccess(java.lang.String, android.net.Uri) | 1 |

### com.market.sdk.IMarketService

DEX：`classes3.dex`。接口描述符：`Lcom/market/sdk/IMarketService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| allowConnectToNetwork | boolean allowConnectToNetwork() | 3 |
| getApkCheckInfo | com.market.sdk.ApkVerifyInfo getApkCheckInfo(java.lang.String, java.lang.String, boolean) | 2 |
| getCategory | int getCategory(java.lang.String[]) | 11 |
| getCategoryV2 | void getCategoryV2(java.lang.String[], android.os.ResultReceiver) | 13 |
| getDesktopFolderConfig | void getDesktopFolderConfig(android.os.ResultReceiver) | 16 |
| getEnableSettings | java.lang.String getEnableSettings() | 10 |
| getVerifyInfo | com.market.sdk.ApkVerifyInfo getVerifyInfo(java.lang.String, java.lang.String, boolean) | 1 |
| getWhiteSet | java.lang.String getWhiteSet() | 9 |
| getWhiteSetV2 | void getWhiteSetV2(android.os.ResultReceiver) | 12 |
| isInWhiteSetForApkCheck | boolean isInWhiteSetForApkCheck(java.lang.String) | 8 |
| loadDesktopRecommendInfo | void loadDesktopRecommendInfo(long, java.lang.String, java.util.List, com.market.sdk.IDesktopRecommendResponse) | 7 |
| loadDesktopRecommendInfoV2 | void loadDesktopRecommendInfoV2(long, java.lang.String, java.util.List, android.os.ResultReceiver) | 14 |
| loadDesktopRecommendInfoV3 | void loadDesktopRecommendInfoV3(android.os.Bundle, android.os.ResultReceiver) | 15 |
| loadIcon | void loadIcon(java.lang.String, java.lang.String, com.market.sdk.IImageCallback) | 5 |
| loadImage | void loadImage(java.lang.String, int, int, com.market.sdk.IImageCallback) | 6 |
| recordStaticsCountEvent | void recordStaticsCountEvent(java.lang.String, java.lang.String) | 4 |

### com.market.sdk.homeguide.IAppstoreHomeGuideService

DEX：`classes3.dex`。接口描述符：`Lcom/market/sdk/homeguide/IAppstoreHomeGuideService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| ready | com.market.sdk.homeguide.HomeUserGuideResult ready(com.market.sdk.homeguide.HomeUserGuideData) | 1 |
| show | void show(android.os.ResultReceiver) | 2 |

### com.miui.analytics.ITrack

DEX：`classes3.dex`。接口描述符：`Lcom/miui/analytics/ITrack;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| trackEvent | void trackEvent(java.lang.String, java.lang.String, java.lang.String, java.lang.String) | 1 |

### com.miui.powerkeeper.thermal.IThermalScenario

DEX：`classes4.dex`。接口描述符：`Lcom/miui/powerkeeper/thermal/IThermalScenario;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| isInCastingWithCamera | int isInCastingWithCamera() | 1 |
| registerListener | void registerListener(int[], com.miui.powerkeeper.thermal.IThermalScenarioListener) | 2 |
| unregisterListener | void unregisterListener(com.miui.powerkeeper.thermal.IThermalScenarioListener) | 3 |

### com.miui.powerkeeper.thermal.IThermalScenarioListener

DEX：`classes4.dex`。接口描述符：`Lcom/miui/powerkeeper/thermal/IThermalScenarioListener;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onScenarioChanged | void onScenarioChanged(java.lang.String) | 1 |
| onTemperatureChanged | void onTemperatureChanged(int) | 2 |

### com.netease.cloudmusic.third.api.contract.ICMApi

DEX：`classes4.dex`。接口描述符：`Lcom/netease/cloudmusic/third/api/contract/ICMApi;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| execute | android.os.Bundle execute(java.lang.String, android.os.Bundle) | 2 |
| executeAsync | void executeAsync(java.lang.String, java.lang.String, android.os.Bundle, com.netease.cloudmusic.third.api.contract.ICMApiCallback) | 1 |
| registerEventListener | android.os.Bundle registerEventListener(com.netease.cloudmusic.third.api.contract.ICMApiEventListener) | 3 |
| unregisterEventListener | android.os.Bundle unregisterEventListener(com.netease.cloudmusic.third.api.contract.ICMApiEventListener) | 4 |

### com.netease.cloudmusic.third.api.contract.ICMApiCallback

DEX：`classes4.dex`。接口描述符：`Lcom/netease/cloudmusic/third/api/contract/ICMApiCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onReturn | void onReturn(android.os.Bundle) | 1 |

### com.netease.cloudmusic.third.api.contract.ICMApiEventListener

DEX：`classes4.dex`。接口描述符：`Lcom/netease/cloudmusic/third/api/contract/ICMApiEventListener;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| events | java.util.List events() | 1 |
| onEvent | void onEvent(java.lang.String, android.os.Bundle) | 2 |

### com.tencent.qqmusic.third.api.contract.IQQMusicApi

DEX：`classes4.dex`。接口描述符：`Lcom/tencent/qqmusic/third/api/contract/IQQMusicApi;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| execute | android.os.Bundle execute(java.lang.String, android.os.Bundle) | 1 |
| executeAsync | void executeAsync(java.lang.String, android.os.Bundle, com.tencent.qqmusic.third.api.contract.IQQMusicApiCallback) | 2 |
| registerEventListener | android.os.Bundle registerEventListener(java.util.List, com.tencent.qqmusic.third.api.contract.IQQMusicApiEventListener) | 3 |
| unregisterEventListener | android.os.Bundle unregisterEventListener(java.util.List, com.tencent.qqmusic.third.api.contract.IQQMusicApiEventListener) | 4 |

### com.tencent.qqmusic.third.api.contract.IQQMusicApiCallback

DEX：`classes4.dex`。接口描述符：`Lcom/tencent/qqmusic/third/api/contract/IQQMusicApiCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onReturn | void onReturn(android.os.Bundle) | 1 |

### com.tencent.qqmusic.third.api.contract.IQQMusicApiEventListener

DEX：`classes4.dex`。接口描述符：`Lcom/tencent/qqmusic/third/api/contract/IQQMusicApiEventListener;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onEvent | void onEvent(java.lang.String, android.os.Bundle) | 1 |

### com.voice.system.ecology.aidl.IControlVoiceChannel

DEX：`classes5.dex`。接口描述符：`Lcom/voice/system/ecology/aidl/IControlVoiceChannel;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onControlAIVoice | java.lang.String onControlAIVoice(java.lang.String, java.lang.String) | 1 |

### com.xiaomi.account.IXiaomiAuthResponse

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/account/IXiaomiAuthResponse;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onCancel | void onCancel() | 2 |
| onResult | void onResult(android.os.Bundle) | 1 |

### com.xiaomi.account.IXiaomiAuthService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/account/IXiaomiAuthService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getAccessTokenInResponse | void getAccessTokenInResponse(com.xiaomi.account.IXiaomiAuthResponse, android.os.Bundle, int, int) | 6 |
| getMiCloudAccessToken | android.os.Bundle getMiCloudAccessToken(android.accounts.Account, android.os.Bundle) | 2 |
| getMiCloudUserInfo | android.os.Bundle getMiCloudUserInfo(android.accounts.Account, android.os.Bundle) | 1 |
| getSnsAccessToken | android.os.Bundle getSnsAccessToken(android.accounts.Account, android.os.Bundle) | 3 |
| getVersionNum | int getVersionNum() | 7 |
| invalidateAccessToken | void invalidateAccessToken(android.accounts.Account, android.os.Bundle) | 4 |
| isSupport | boolean isSupport(java.lang.String) | 8 |
| supportResponseWay | boolean supportResponseWay() | 5 |

### com.xiaomi.account.passportsdk.account_lib.IAccountExchangeService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/account/passportsdk/account_lib/IAccountExchangeService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getNullableAccount | com.xiaomi.accountsdk.account.data.AccountInfo getNullableAccount(java.lang.String) | 2 |
| tryAddAccount | void tryAddAccount(com.xiaomi.accountsdk.account.data.AccountInfo, java.lang.String) | 1 |

### com.xiaomi.accounts.IAccountAuthenticator

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/accounts/IAccountAuthenticator;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| addAccount | void addAccount(com.xiaomi.accounts.IAccountAuthenticatorResponse, java.lang.String, java.lang.String, java.lang.String[], android.os.Bundle) | 1 |
| confirmCredentials | void confirmCredentials(com.xiaomi.accounts.IAccountAuthenticatorResponse, android.accounts.Account, android.os.Bundle) | 2 |
| editProperties | void editProperties(com.xiaomi.accounts.IAccountAuthenticatorResponse, java.lang.String) | 6 |
| getAccountRemovalAllowed | void getAccountRemovalAllowed(com.xiaomi.accounts.IAccountAuthenticatorResponse, android.accounts.Account) | 8 |
| getAuthToken | void getAuthToken(com.xiaomi.accounts.IAccountAuthenticatorResponse, android.accounts.Account, java.lang.String, android.os.Bundle) | 3 |
| getAuthTokenLabel | void getAuthTokenLabel(com.xiaomi.accounts.IAccountAuthenticatorResponse, java.lang.String) | 4 |
| hasFeatures | void hasFeatures(com.xiaomi.accounts.IAccountAuthenticatorResponse, android.accounts.Account, java.lang.String[]) | 7 |
| updateCredentials | void updateCredentials(com.xiaomi.accounts.IAccountAuthenticatorResponse, android.accounts.Account, java.lang.String, android.os.Bundle) | 5 |

### com.xiaomi.accounts.IAccountAuthenticatorResponse

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/accounts/IAccountAuthenticatorResponse;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onError | void onError(int, java.lang.String) | 3 |
| onRequestContinued | void onRequestContinued() | 2 |
| onResult | void onResult(android.os.Bundle) | 1 |

### com.xiaomi.accounts.IAccountManagerResponse

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/accounts/IAccountManagerResponse;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onError | void onError(int, java.lang.String) | 3 |
| onRequestContinued | void onRequestContinued() | 2 |
| onResult | void onResult(android.os.Bundle) | 1 |

### com.xiaomi.accounts.IAccountManagerService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/accounts/IAccountManagerService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| addAccount | boolean addAccount(android.accounts.Account, java.lang.String, android.os.Bundle) | 6 |
| addAcount | void addAcount(com.xiaomi.accounts.IAccountManagerResponse, java.lang.String, java.lang.String, java.lang.String[], boolean, android.os.Bundle) | 16 |
| clearPassword | void clearPassword(android.accounts.Account) | 12 |
| confirmCredentials | void confirmCredentials(com.xiaomi.accounts.IAccountManagerResponse, android.accounts.Account, android.os.Bundle, boolean) | 19 |
| editProperties | void editProperties(com.xiaomi.accounts.IAccountManagerResponse, java.lang.String, boolean) | 18 |
| getAccounts | android.accounts.Account[] getAccounts(java.lang.String) | 3 |
| getAccountsByFeatures | void getAccountsByFeatures(com.xiaomi.accounts.IAccountManagerResponse, java.lang.String, java.lang.String[]) | 5 |
| getAuthToken | void getAuthToken(com.xiaomi.accounts.IAccountManagerResponse, android.accounts.Account, java.lang.String, boolean, boolean, android.os.Bundle) | 15 |
| getAuthTokenLabel | void getAuthTokenLabel(com.xiaomi.accounts.IAccountManagerResponse, java.lang.String, java.lang.String) | 20 |
| getPassword | java.lang.String getPassword(android.accounts.Account) | 1 |
| getUserData | java.lang.String getUserData(android.accounts.Account, java.lang.String) | 2 |
| hasFeatures | void hasFeatures(com.xiaomi.accounts.IAccountManagerResponse, android.accounts.Account, java.lang.String[]) | 4 |
| invalidateAuthToken | void invalidateAuthToken(java.lang.String, java.lang.String) | 8 |
| peekAuthToken | java.lang.String peekAuthToken(android.accounts.Account, java.lang.String) | 9 |
| removeAccount | void removeAccount(com.xiaomi.accounts.IAccountManagerResponse, android.accounts.Account) | 7 |
| setAuthToken | void setAuthToken(android.accounts.Account, java.lang.String, java.lang.String) | 10 |
| setPassword | void setPassword(android.accounts.Account, java.lang.String) | 11 |
| setUserData | void setUserData(android.accounts.Account, java.lang.String, java.lang.String) | 13 |
| updateAppPermission | void updateAppPermission(android.accounts.Account, java.lang.String, int, boolean) | 14 |
| updateCredentials | void updateCredentials(com.xiaomi.accounts.IAccountManagerResponse, android.accounts.Account, java.lang.String, boolean, android.os.Bundle) | 17 |

### com.xiaomi.accounts.ILocalFeatureManagerResponse

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/accounts/ILocalFeatureManagerResponse;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onError | void onError(int, java.lang.String) | 3 |
| onRequestContinued | void onRequestContinued() | 2 |
| onResult | void onResult(android.os.Bundle) | 1 |

### com.xiaomi.accountsdk.account.IFindDeviceRemoveAccountService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/accountsdk/account/IFindDeviceRemoveAccountService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| removeAccount | boolean removeAccount() | 1 |

### com.xiaomi.accountsdk.account.IXiaomiAccountService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/accountsdk/account/IXiaomiAccountService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getAccessToken | java.lang.String getAccessToken(android.accounts.Account, java.lang.String, java.lang.String, boolean) | 9 |
| getAccountLoginHint | java.lang.String getAccountLoginHint() | 12 |
| getAvatarFd | android.os.ParcelFileDescriptor getAvatarFd(android.accounts.Account) | 6 |
| getAvatarFdByFileName | android.os.ParcelFileDescriptor getAvatarFdByFileName(java.lang.String) | 8 |
| getEmail | java.lang.String getEmail(android.accounts.Account) | 3 |
| getEncryptedUserId | java.lang.String getEncryptedUserId(android.accounts.Account) | 4 |
| getNickName | java.lang.String getNickName(android.accounts.Account) | 2 |
| getPhone | java.lang.String getPhone(android.accounts.Account) | 5 |
| getSnsAccessToken | java.lang.String getSnsAccessToken(java.lang.String) | 10 |
| getUserName | java.lang.String getUserName(android.accounts.Account) | 1 |
| getXiaomiAccount | com.xiaomi.accountsdk.account.XiaomiAccount getXiaomiAccount(boolean, android.accounts.Account) | 7 |
| invalidateSnsAccessToken | boolean invalidateSnsAccessToken(java.lang.String, java.lang.String) | 11 |

### com.xiaomi.accountsdk.guestaccount.IGuestAccountIntentHandler

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/accountsdk/guestaccount/IGuestAccountIntentHandler;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| handleIntent | boolean handleIntent(android.content.Intent) | 1 |

### com.xiaomi.accountsdk.guestaccount.IGuestAccountService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/accountsdk/guestaccount/IGuestAccountService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getGuestAccount | android.os.Bundle getGuestAccount(android.os.Bundle, com.xiaomi.accountsdk.guestaccount.IGuestAccountIntentHandler) | 1 |
| getStoredUserId | android.os.Bundle getStoredUserId(android.os.Bundle) | 4 |
| onXiaomiAccountCTAAllowed | void onXiaomiAccountCTAAllowed() | 3 |
| renewServiceToken | android.os.Bundle renewServiceToken(android.os.Bundle, com.xiaomi.accountsdk.guestaccount.IGuestAccountIntentHandler) | 2 |

### com.xiaomi.ai.android.transport.IRPCCallback

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/ai/android/transport/IRPCCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| execCommand | android.os.Bundle execCommand(int, android.os.Bundle) | 2 |
| execOnewayCommand | void execOnewayCommand(int, android.os.Bundle) | 1 |

### com.xiaomi.ai.android.transport.ITransportAID

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/ai/android/transport/ITransportAIDL;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| execCommand | android.os.Bundle execCommand(java.lang.String, int, android.os.Bundle) | 4 |
| execOnewayCommand | void execOnewayCommand(java.lang.String, int, android.os.Bundle) | 3 |
| registerCallback | void registerCallback(java.lang.String, com.xiaomi.ai.android.transport.IRPCCallback, android.os.Bundle) | 1 |
| unregisterCallback | void unregisterCallback(java.lang.String, com.xiaomi.ai.android.transport.IRPCCallback) | 2 |

### com.xiaomi.aicr.IAiCrCoreService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/aicr/IAiCrCoreService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getPluginBinder | android.os.IBinder getPluginBinder(com.xiaomi.aicr.ICoreServiceCallback, java.lang.String, java.lang.String, java.lang.String, android.os.Bundle) | 1 |
| isSupport | boolean isSupport(java.lang.String) | 3 |
| releaseConnect | void releaseConnect(java.lang.String) | 2 |

### com.xiaomi.aicr.ICoreServiceCallback

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/aicr/ICoreServiceCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onDownload | void onDownload(android.os.IBinder) | 1 |
| speed | void speed(java.lang.String, long) | 2 |

### com.xiaomi.aicr.IDownloadCallback

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/aicr/IDownloadCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onDownloadComplete | void onDownloadComplete(java.lang.String) | 2 |
| onError | void onError(int) | 3 |
| onProgressUpdate | void onProgressUpdate(int) | 1 |

### com.xiaomi.aicr.IDownloadListener

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/aicr/IDownloadListener;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| cancelDownload | void cancelDownload() | 3 |
| download | void download(java.lang.String, java.lang.String, com.xiaomi.aicr.IDownloadCallback) | 4 |
| isCanceled | boolean isCanceled() | 7 |
| isLoading | boolean isLoading() | 5 |
| isPaused | boolean isPaused() | 6 |
| pauseDownload | void pauseDownload() | 1 |
| resumeDownload | void resumeDownload() | 2 |
| setCanceled | void setCanceled() | 8 |

### com.xiaomi.aicr.paintservice.IPaintService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/aicr/paintservice/IPaintService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| paintService_check | int paintService_check() | 1 |
| paintService_getBitmap | android.graphics.Bitmap paintService_getBitmap(int) | 5 |
| paintService_getProcess | int paintService_getProcess(int) | 4 |
| paintService_init | int paintService_init() | 2 |
| paintService_paintWithCallback | int paintService_paintWithCallback(int, int, java.lang.String, com.xiaomi.aicr.paintservice.IPaintStatusCallback) | 3 |
| paintService_release | int paintService_release() | 6 |

### com.xiaomi.aicr.paintservice.IPaintStatusCallback

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/aicr/paintservice/IPaintStatusCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onPaintFailed | void onPaintFailed(byte) | 2 |
| onPaintFinished | void onPaintFinished() | 1 |

### com.xiaomi.aicr.plugin.IImageSegmentService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/aicr/plugin/IImageSegmentService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getAlgorithmVersion | java.lang.String getAlgorithmVersion() | 8 |
| initAlgorithmCachePath | int initAlgorithmCachePath() | 1 |
| initPersonModel | int initPersonModel() | 2 |
| initSkyModel | int initSkyModel() | 3 |
| releaseAll | int releaseAll() | 7 |
| releaseModel | int releaseModel(boolean, boolean) | 6 |
| segment | com.xiaomi.aicr.vision.imagesegment.SegmentResult segment(android.graphics.Bitmap, com.xiaomi.aicr.vision.VisionAttribute) | 4 |
| segmentByFd | com.xiaomi.aicr.vision.imagesegment.SegmentResult segmentByFd(android.os.ParcelFileDescriptor, com.xiaomi.aicr.vision.VisionAttribute) | 5 |

### com.xiaomi.aicr.plugin.IMIotAlgoService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/aicr/plugin/IMIotAlgoService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| doCalculation | java.lang.String doCalculation(java.lang.String) | 2 |
| getBrightness | java.lang.String getBrightness() | 4 |
| getCaculatedCurve | java.lang.String getCaculatedCurve() | 5 |
| initAlgo | void initAlgo(java.lang.String) | 1 |
| releaseAlgo | void releaseAlgo() | 3 |

### com.xiaomi.aicr.plugin.INerService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/aicr/plugin/INerService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| cut | java.util.List cut(java.lang.String) | 2 |
| extract | java.util.List extract(java.lang.String) | 1 |

### com.xiaomi.aicr.plugin.IVisionService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/aicr/plugin/IVisionService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| doDetect | int doDetect(int, java.util.List, com.xiaomi.aicr.vision.VisionAttribute) | 5 |
| doOCRDetect | com.xiaomi.aicr.vision.ocr.OCRRes$Location[] doOCRDetect(int) | 3 |
| doOCRRecognize | com.xiaomi.aicr.vision.ocr.OCRRes$OCRResult doOCRRecognize(int) | 4 |
| setImage | int setImage(android.graphics.Bitmap) | 1 |
| setImageParcelFileDesciptor | int setImageParcelFileDesciptor(android.os.ParcelFileDescriptor) | 2 |

### com.xiaomi.devauth.IMiDevAuthInterface

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/devauth/IMiDevAuthInterface;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| GetUidList | java.lang.String GetUidList() | 7 |
| UCarVerifyStart | int UCarVerifyStart(java.lang.String, java.lang.String) | 8 |
| chooseKey | byte[] chooseKey(byte[], byte[], byte[]) | 2 |
| cleanAllOnlineKeyAndUidData | int cleanAllOnlineKeyAndUidData() | 6 |
| getChallenge | byte[] getChallenge(int) | 1 |
| newKeyBlobGet | byte[] newKeyBlobGet(int, byte[], byte[], byte[]) | 5 |
| tokenGet | byte[] tokenGet(int, byte[], byte[], byte[]) | 4 |
| tokenVerify | int tokenVerify(int, byte[], byte[], byte[], byte[]) | 3 |

### com.xiaomi.market.IAppDownloadManager

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/market/IAppDownloadManager;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| cancel | boolean cancel(java.lang.String, java.lang.String) | 2 |
| download | void download(android.os.Bundle) | 1 |
| downloadByUri | void downloadByUri(android.net.Uri) | 5 |
| lifecycleChanged | void lifecycleChanged(java.lang.String, int) | 8 |
| pause | boolean pause(java.lang.String, java.lang.String) | 3 |
| pauseByUri | void pauseByUri(android.net.Uri) | 6 |
| resume | boolean resume(java.lang.String, java.lang.String) | 4 |
| resumeByUri | void resumeByUri(android.net.Uri) | 7 |

### com.xiaomi.market.IDetailsPageManager

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/market/IDetailsPageManager;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| openDetailsPage | boolean openDetailsPage(android.os.Bundle) | 1 |

### com.xiaomi.market.IPreloadAppDetailService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/market/IPreloadAppDetailService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| preloadAppDetail | void preloadAppDetail(java.lang.String) | 1 |

### com.xiaomi.market.IQueryAppInfoService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/market/IQueryAppInfoService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| queryAppInfo | void queryAppInfo(android.os.Bundle, java.util.List, com.xiaomi.market.IQueryAppInfoServiceCallback) | 1 |

### com.xiaomi.market.IQueryAppInfoServiceCallback

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/market/IQueryAppInfoServiceCallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onCall | void onCall(android.os.Bundle) | 1 |
| onError | void onError(android.os.Bundle) | 2 |

### com.xiaomi.micloudkeybag.IMiCloudKeyBagService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/micloudkeybag/IMiCloudKeyBagService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| decrypt | void decrypt(android.accounts.Account, byte[], long, com.xiaomi.micloudkeybag.IOnKeyBagCallFinishedListener) | 6 |
| encrypt | void encrypt(android.accounts.Account, byte[], long, com.xiaomi.micloudkeybag.IOnKeyBagCallFinishedListener) | 5 |
| getInstalledKeyInfo | com.xiaomi.micloudkeybag.KeyBagKeyInfo getInstalledKeyInfo(android.accounts.Account) | 4 |
| getServiceVersion | int getServiceVersion() | 1 |
| isLastSupported | boolean isLastSupported(android.accounts.Account) | 2 |
| isSupported | void isSupported(android.accounts.Account, com.xiaomi.micloudkeybag.IOnKeyBagCallFinishedListener) | 3 |
| showDownloadNotification | void showDownloadNotification() | 7 |
| showUpdateNotification | void showUpdateNotification() | 8 |

### com.xiaomi.micloudkeybag.IOnKeyBagCallFinishedListener

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/micloudkeybag/IOnKeyBagCallFinishedListener;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onDecryptFinished | void onDecryptFinished(int, byte[]) | 3 |
| onEncryptFinished | void onEncryptFinished(int, byte[]) | 2 |
| onIsSupportedFinished | void onIsSupportedFinished(int, boolean) | 1 |

### com.xiaomi.onetrack.util.DeviceUtil$GAIDClient$a

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/onetrack/util/DeviceUtil$GAIDClient$a;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| <init> | void <init>(android.os.IBinder) | — |
| a | java.lang.String a() | — |
| a | boolean a(boolean) | — |
| asBinder | android.os.IBinder asBinder() | — |

### com.xiaomi.onetrack.util.oaid.a.a

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/onetrack/util/oaid/a/a;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| a | java.lang.String a() | — |

### com.xiaomi.onetrack.util.oaid.a.b

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/onetrack/util/oaid/a/b;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| a | java.lang.String a() | — |
| b | boolean b() | — |

### com.xiaomi.onetrack.util.oaid.a.c

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/onetrack/util/oaid/a/c;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| a | java.lang.String a() | — |
| a | java.lang.String a(java.lang.String) | — |
| b | java.lang.String b() | — |
| b | java.lang.String b(java.lang.String) | — |
| c | boolean c() | — |

### com.xiaomi.onetrack.util.oaid.a.d

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/onetrack/util/oaid/a/d;`。

无方法定义。

### com.xiaomi.onetrack.util.oaid.a.e

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/onetrack/util/oaid/a/e;`。

无方法定义。

### com.xiaomi.onetrack.util.oaid.a.f

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/onetrack/util/oaid/a/f;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| a | java.lang.String a() | — |

### com.xiaomi.onetrack.util.oaid.a.g

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/onetrack/util/oaid/a/g;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| a | boolean a() | — |
| b | java.lang.String b() | — |
| c | boolean c() | — |
| d | void d() | — |

### com.xiaomi.passport.IPassportCommonService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/passport/IPassportCommonService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getDeviceInfo | com.xiaomi.accountsdk.service.DeviceInfoResult getDeviceInfo(java.lang.String, int) | 1 |
| getSystemAccountData | android.os.Bundle getSystemAccountData(java.lang.String[]) | 4 |
| getUserData | java.lang.String[] getUserData(android.accounts.Account, java.lang.String, java.lang.String[]) | 2 |
| setUserData | void setUserData(android.accounts.Account, java.lang.String, java.lang.String[], java.lang.String[]) | 3 |

### com.xiaomi.passport.IPassportServiceTokenService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/passport/IPassportServiceTokenService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| fastCheckSlhPhCompatibility | boolean fastCheckSlhPhCompatibility() | 4 |
| getAccountVisible | com.xiaomi.passport.servicetoken.data.XmAccountVisibility getAccountVisible(java.lang.String) | 7 |
| getServiceToken | com.xiaomi.passport.servicetoken.ServiceTokenResult getServiceToken(java.lang.String) | 1 |
| invalidateServiceToken | com.xiaomi.passport.servicetoken.ServiceTokenResult invalidateServiceToken(com.xiaomi.passport.servicetoken.ServiceTokenResult) | 2 |
| requestSecondaryDeviceLoginData | android.os.Bundle requestSecondaryDeviceLoginData(android.os.Bundle) | 8 |
| setAccountVisible | com.xiaomi.passport.servicetoken.data.XmAccountVisibility setAccountVisible(java.lang.String) | 6 |
| supportAccessAccount | boolean supportAccessAccount() | 5 |
| supportServiceTokenUIResponse | boolean supportServiceTokenUIResponse() | 3 |

### com.xiaomi.passport.ISecurityDeviceSignResponse

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/passport/ISecurityDeviceSignResponse;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onResult | void onResult(android.os.Bundle) | 1 |

### com.xiaomi.passport.ISecurityDeviceSignService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/passport/ISecurityDeviceSignService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| sign | void sign(com.xiaomi.passport.ISecurityDeviceSignResponse, java.lang.String, java.lang.String, android.os.Bundle) | 1 |

### com.xiaomi.passport.servicetoken.IServiceTokenUIResponse

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/passport/servicetoken/IServiceTokenUIResponse;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onError | void onError(int, java.lang.String) | 3 |
| onRequestContinued | void onRequestContinued() | 2 |
| onResult | void onResult(android.os.Bundle) | 1 |

### com.xiaomi.passport.uicontroller.IMiPassportUIControllerService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/passport/uicontroller/IMiPassportUIControllerService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| addOrUpdateAccountManager | void addOrUpdateAccountManager(com.xiaomi.accountsdk.account.data.AccountInfo) | 4 |
| loginByPassword | com.xiaomi.accountsdk.account.data.MiLoginResult loginByPassword(com.xiaomi.accountsdk.account.data.PasswordLoginParams) | 1 |
| loginByStep2 | com.xiaomi.accountsdk.account.data.MiLoginResult loginByStep2(com.xiaomi.accountsdk.account.data.Step2LoginParams) | 3 |
| onNotificationAuthEnd | com.xiaomi.accountsdk.account.data.NotificationAuthResult onNotificationAuthEnd(java.lang.String) | 5 |
| onNotificationLoginEnd | com.xiaomi.accountsdk.account.data.MiLoginResult onNotificationLoginEnd(com.xiaomi.accountsdk.account.data.NotificationLoginEndParams) | 2 |

### com.xiaomi.phonenum.service.IAccountPhoneNumberManagerService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/phonenum/service/IAccountPhoneNumberManagerService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getAccountCertifications | void getAccountCertifications(java.lang.String, java.lang.String, int, com.xiaomi.phonenum.service.IAccountPhoneNumberResponse, java.lang.String) | 2 |
| getPlainPhoneNumbers | void getPlainPhoneNumbers(java.lang.String, java.lang.String, int, com.xiaomi.phonenum.service.IAccountPhoneNumberResponse, java.lang.String) | 1 |
| getSIMInfos | void getSIMInfos(java.lang.String, java.lang.String, java.lang.String[], com.xiaomi.phonenum.service.IAccountPhoneNumberResponse, java.lang.String) | 5 |
| getVersion | int getVersion() | 4 |
| invalidateAccountCertification | int invalidateAccountCertification(java.lang.String, java.lang.String, com.xiaomi.phonenum.data.AccountCertification) | 3 |

### com.xiaomi.phonenum.service.IAccountPhoneNumberResponse

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/phonenum/service/IAccountPhoneNumberResponse;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onError | void onError(int, java.lang.String) | 2 |
| onResult | void onResult(android.os.Bundle) | 1 |

### com.xiaomi.simactivate.ISimActivateService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/simactivate/ISimActivateService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| invoke | android.os.Bundle invoke(java.lang.String, android.os.Bundle) | 2 |
| isSupported | int isSupported(java.lang.String, android.os.Bundle) | 1 |

### com.xiaomi.simactivate.service.IPhoneNumService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/simactivate/service/IPhoneNumService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| blockObtainPhoneNum | android.os.Bundle blockObtainPhoneNum(int, java.lang.String, int, boolean) | 2 |
| invalidatePhoneNum | boolean invalidatePhoneNum(int, java.lang.String, int) | 3 |
| invalidateVerifiedToken | boolean invalidateVerifiedToken(int, java.lang.String, int) | 4 |
| isSupport | boolean isSupport(int, java.lang.String, java.lang.String) | 1 |

### com.xiaomi.taiyi.sdk.transfer.core.IAIAbility

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/taiyi/sdk/transfer/core/IAIAbility;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| api | java.lang.String api() | 1 |
| bind | int bind(com.xiaomi.taiyi.sdk.transfer.core.IAIClient, com.xiaomi.taiyi.sdk.transfer.data.AIRequest) | 8 |
| execute | com.xiaomi.taiyi.sdk.transfer.data.AIResponse execute(com.xiaomi.taiyi.sdk.transfer.data.AIRequest) | 13 |
| getMemory | com.xiaomi.taiyi.sdk.transfer.core.IAIMemory getMemory(java.lang.String) | 10 |
| hasSession | boolean hasSession() | 11 |
| isAlive | boolean isAlive() | 6 |
| isInternal | boolean isInternal() | 7 |
| isLLM | boolean isLLM() | 5 |
| name | java.lang.String name() | 2 |
| post | void post(com.xiaomi.taiyi.sdk.transfer.data.AIRequest, com.xiaomi.taiyi.sdk.transfer.core.IAICallback) | 14 |
| query | com.xiaomi.taiyi.sdk.transfer.data.AIResponse query(com.xiaomi.taiyi.sdk.transfer.data.AIRequest) | 12 |
| type | int type() | 4 |
| unbind | int unbind(java.lang.String, com.xiaomi.taiyi.sdk.transfer.data.AIRequest) | 9 |
| version | long version() | 3 |

### com.xiaomi.taiyi.sdk.transfer.core.IAICallback

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/taiyi/sdk/transfer/core/IAICallback;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onResponse | void onResponse(com.xiaomi.taiyi.sdk.transfer.data.AIResponse) | 1 |

### com.xiaomi.taiyi.sdk.transfer.core.IAIClient

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/taiyi/sdk/transfer/core/IAIClient;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getId | java.lang.String getId() | 1 |
| getInfo | com.xiaomi.taiyi.sdk.transfer.data.AIHeaders getInfo() | 2 |
| getMemory | com.xiaomi.taiyi.sdk.transfer.core.IAIMemory getMemory() | 3 |

### com.xiaomi.taiyi.sdk.transfer.core.IAICoreService

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/taiyi/sdk/transfer/core/IAICoreService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| onProcessStart | void onProcessStart(java.lang.String) | 2 |
| onProcessStop | void onProcessStop(java.lang.String) | 3 |
| prepare | com.xiaomi.taiyi.sdk.transfer.data.AIResponse prepare(com.xiaomi.taiyi.sdk.transfer.data.AIRequest) | 1 |

### com.xiaomi.taiyi.sdk.transfer.core.IAIManager

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/taiyi/sdk/transfer/core/IAIManager;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| authorize | com.xiaomi.taiyi.sdk.transfer.data.AIResponse authorize(com.xiaomi.taiyi.sdk.transfer.data.AIRequest) | 1 |
| loadAsync | void loadAsync(com.xiaomi.taiyi.sdk.transfer.data.AIRequest, com.xiaomi.taiyi.sdk.transfer.core.IAICallback) | 2 |
| loadSync | com.xiaomi.taiyi.sdk.transfer.data.AIResponse loadSync(com.xiaomi.taiyi.sdk.transfer.data.AIRequest) | 3 |

### com.xiaomi.taiyi.sdk.transfer.core.IAIMemory

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/taiyi/sdk/transfer/core/IAIMemory;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| free | void free(java.util.List) | 1 |
| get | com.xiaomi.taiyi.sdk.transfer.data.ShareMemoryPool get() | 3 |
| sync | void sync(com.xiaomi.taiyi.sdk.transfer.data.ShareMemoryPool) | 2 |

### com.xiaomi.taiyi.sdk.transfer.data.IBitmap

DEX：`classes5.dex`。接口描述符：`Lcom/xiaomi/taiyi/sdk/transfer/data/IBitmap;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| get | android.graphics.Bitmap get() | 1 |

### com.xiaomi.udevid.IUDevIdService

DEX：`classes6.dex`。接口描述符：`Lcom/xiaomi/udevid/IUDevIdService;`。

| 方法 | 完整 Java 签名 | 事务编号 |
| --- | --- | --- |
| getUDevIdFromSystemAccount | android.os.Bundle getUDevIdFromSystemAccount(android.os.Bundle) | 1 |

