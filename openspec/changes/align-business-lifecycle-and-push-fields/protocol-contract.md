# 0.2 原镜像消息合同

输入为 [protocol-audit.json](protocol-audit.json) 登记的 24A446 accessoryd 原镜像。
九个相关完整函数逐指令重反汇编与既有切片一致；handler 表从原字节读取，
出站 ID 及关键参数构造点直接对原指令断言。C16/C18 同时复核空 TLV、
U32 getter、START 替换、STOP 清理和 5003 三个参数的分支。

下表方向从手机观察。CONFIRMED 只覆盖列出的局部原字节/调用链；
未核平台消费者或外层 dispatch 的部分保留 OPEN，不能由静态函数存在推断实车已执行。

| 消息 | 方向/身份 | 已证结构及失败边界 | 未闭合部分 |
|---|---|---|---|
| 5000 | 配件→手机；表 10021c038 → 1001499f0，CONFIRMED | p0/p1/p2 为子参数组；p0 媒体、p1 播放、p2 转内部位图；p1 子项 0x11 为 U32，其余已核标记为总长 4；未知顶层跳过；非法值整条失败；成功先移除旧子特性再替换数组，CONFIRMED | 完整平台计数/PlaybackQueueList 清理 OPEN；p2 的 0..31 限制是本地策略 |
| 5001 | 手机→配件；146ac8 的 ID 构造，CONFIRMED | 多类属性使用组参数；受实际选择与方向/会话门约束；封面走文件传输，CONFIRMED（A04/A14） | 每个属性的完整单位/平台值域与失败传播不能由构造 ID 得出，逐字段处理 |
| 5002 | 配件→手机；14a93c，CONFIRMED | 复用移除 helper、清 active 与属性数组；处理器不解析附加参数，CONFIRMED | 所有异步清理完成与并发幂等 OPEN；本地实现仍要求资源所有权闭合 |
| 5003 | 配件→手机；14aa20，CONFIRMED | p0/p1/p2 均 U32；p0 到 setPlaybackElapsedTime，p1 到 setPlaybackQueueIndex，p2 为队列窗口覆盖；仅 0xffffffff 为自动选择；p2 即时请求检查 START 子项 0x11 出现位；非法长度在提交前失败，CONFIRMED | 时间单位、平台有效值与实际执行/失败反馈 OPEN；p0/p1 没有本处理器 START active 门 |
| 5200 | 配件→手机；表 21f620 → 17527c，CONFIRMED | 重复 p0 为 U16 组件；p1..5 是总长 4 的空标记；同标记重复/非空失败；无参数可走后续门；required 表检查在解析后，CONFIRMED | options 完整业务含义/无组件 profile OPEN；显示长度不能从 START 反推 |
| 5201 | 手机→配件；2a2c 的 ID 构造，CONFIRMED | 状态 p1、道路文本 p3、距离参数 p7/p10 的身份构造点直接核对；字段 getter/writer 路径与完整 body 一致 | 全字段类型/单位及通用增量顺序继续逐字段核；不能从目前 DiPlay 按米消费推断通用 Apple 单位 |
| 5202 | 手机→配件；1779fc 的 ID 构造，CONFIRMED | 完整机动编码 body 与原字节一致；定义/引用/容量以另行导航核心证据及接收消费联测验证 | 每个可选机动字段及平台默认分支继续 OPEN；单槽 reset 顺序是已登记接收兼容/本地策略 |
| 5203 | 配件→手机；17593c，CONFIRMED | p0 逐项 U16 组件，未知参数跳过；坏 p0 返回失败，平台停止入口接收解析后组件数组 | 精细组件停止效果/全部异步资源释放 OPEN；当前发布器全停是本地已明示策略 |
| 5204 | 手机→配件；177f80 的 ID 构造，CONFIRMED | lane 更新是独立消息，17527c 内还检查其出站能力；完整编码 body 与原字节一致 | 真实宿主 lane 模型、角度/状态枚举和显示合同 OPEN，当前不启用无来源字段 |

## 生命周期与声明

入站/出站消息 ID、认证及 Identification 门分别由实际控制层负责；业务 START 不创造
认证上下文。导航必需消息集合由方向能力核对，5204 的可选能力另有准入。
具体 required descriptor 全表及宿主来源不是本次九个 body 的完整覆盖范围。

C16 验证 SUS 为控制字节 0x08、恢复构造为无载荷 ACK 0x40、内部投递事件 0x1b/0x1c。
这不证明任意 ACK 是恢复，不证明平台唤醒等于 iAP2 恢复，也不证明订阅自动保留。
对恢复/计数/在途任务采用文档明示的本地有效性策略，不把它标为 Apple 完整状态机。

## 复核命令与结果

```powershell
python -X utf8 -B openspec/changes/align-business-lifecycle-and-push-fields/tools/verify_protocol.py `
  --deps local-backups/2026-11-12-business-alignment/tooldeps --report
```

Capstone 5.0.7；C18：3 个完整切片、76 个锚点、6 个 Mach-O imports、7 个 block 指针、
8 个 selector；C16：12 个完整切片、31 个锚点、6 个跳表项及空 TLV 边界；
新增复核：9 个消息完整 body、6 个 handler 注册、8 个 ID/参数锚点，全部通过。
依赖仅下载到忽略的本地工具目录。Windows 沙箱不能读取其临时目录 ACL，复核获准在沙箱外运行。
结果是静态核对，没有执行苹果服务、Gradle 或实车测试。
