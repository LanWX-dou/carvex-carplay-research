# 逐项执行记录

历史计划的 [baseline.json](baseline.json) 保持不变；执行开始的输入另存为
[execution-baseline.json](execution-baseline.json)。后续生产修正会改变输入哈希，
本记录和每项 fix 说明保留适用版本，不覆盖历史快照。

## 0.1 当前基线复核

手机 `6b6addc44273f6b294a52bcb45cd381c3a35a1a3`、DiPlay
`615b32ce0b40cd0b99ce94ba23a512001553684f`，开始时两端工作区均干净。
研究仓库在计划提交后增加 `fabb9b2`；当前执行读取该版本，不把计划前的既有改动当作本轮输入。
29 个已登记文件与计划 SHA256 全部一致。

本地原 accessoryd 镜像 SHA256 与 24A446 审计基线一致，关键 NowPlaying、导航、
SUS/Resume 汇编和两个原指令 verifier 可用。原始 IPSW 未在约定位置发现，
因此本轮可复核已有原镜像字节，不能宣称重新解包并认证 IPSW 来源。
完整可用性清单见 execution-baseline.json；它只证明输入身份与存在性。

执行并通过：

```powershell
python -X utf8 -B openspec/changes/align-business-lifecycle-and-push-fields/tools/verify_baseline.py --capture
python -X utf8 -B openspec/changes/align-business-lifecycle-and-push-fields/tools/verify_baseline.py
git diff --check
```

手机与车机生产文件本项未修改，没有运行 Gradle 或实车测试。下一项按原镜像与指令切片复核语义。

## 0.2 原指令与消息合同

0.1 的独立提交为 `b7cd562`。本项登记 [逐消息合同](protocol-contract.md) 和
[原指令结果](protocol-audit.json)，保持平台单位、完整可选 schema、恢复/异步清理等 OPEN。
C16/C18 及九个完整 body/六个注册/八个构造锚点复核通过；命令、计数和范围见逐消息合同。
没有修改协议研究的历史结论、原镜像或生产 Kotlin，没有把局部静态验证记作整系统行为通过。
