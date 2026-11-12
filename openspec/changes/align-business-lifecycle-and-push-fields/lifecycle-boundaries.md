# 任务1.3 — 实际挂起/恢复边界（OPEN）

原字节C16确认SUS=控制字节08、无业务payload；设备本地主动恢复构造空ACK40，
内部事件1b/1c。完整对端恢复识别和订阅保留仍OPEN，见[协议核对](protocol-contract.md)。

当前IapLink.receive在任何含08的frame上抛出 `UNSUPPORTED_LINK_CONTROL: SLP`。
它没有已接受SUS事件、挂起状态或经确认的恢复入口。异常进入RuntimeIap.fail，撤销identification，
转DEGRADED并关闭link。AirSession随state变化关闭音乐、导航和phone订阅。
这是一条未支持时的失败关闭路径，不能称为“已支持挂起且维持ACK/重传”。
字段名SLP是现有诊断标签；不由名称反推协议语义。

平台休眠/唤醒没有注册为上述owner的iAP2恢复结果。AirSession的音频stream关闭、
全会话TEARDOWN和Kotlin suspend函数也不是SUS/Resume事件。
普通ACK由IapLink可靠传输处理，RuntimeIap不据此重建认证或订阅。
任务1.2已覆盖linkReady失效及重新ready无START时拒绝音乐输出；既有导航guard同样不重放旧订阅。

本项只完成对账，**1.3保持未勾选**。实施接受SUS前需进一步读取原link/FSM接收与恢复调用链，
确认控制序号、ACK/重传在挂起期间的处理和实际恢复owner事件，再增加合成writer回归及现场验证。
不能以等待时间、任意ACK、屏幕点亮或单独布尔值放行业务。此次没有修改transport状态机，
没有运行新的Gradle或实车测试；复用了0.2原字节审计和1.2已登记的本地门控验证，未算作新测试。
