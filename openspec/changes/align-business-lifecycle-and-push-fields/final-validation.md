# 2026-11-14 本地实施验收

手机最终提交`7e2ce04`，准备联测时手机基线`7ac992c`；接收实现提交`ad4ccbfb`。
第4阶段根仓库记录`c9921ef`。最终提交仅增加已测试工具、修正记录及验收摘要；
没有改动协议依赖、未证provider或firmware既有修改。

## 实际结果

| 检查 | tests | failures/errors/skipped | 结果 |
|---|---:|---|---|
| 手机protocol-carplay | 1195 | 0/0/0 | PASS；最终串行命令实际重跑 |
| 手机bridge | 65 | 0/0/0 | PASS；本轮有效Gradle缓存报告 |
| 手机host-carlife-mixing | 36 | 0/0/0 | PASS；本轮有效Gradle缓存报告 |
| DiPlay shared | 1807 | 3/0/2 | FAIL |
| DiPlay common | 1730 | 0/0/0 | PASS |
| DiPlay home | 11 | 0/0/0 | PASS |

手机小米Kotlin编译成功；最终串行调用57s、90 tasks（1 executed/89 up-to-date）。
接收合同20+2和7个原worker测试全部存在、无失败/跳过。
DiPlay相关worker7、overlay owner2、PlaybackStatus5、ClusterSong9、Glance8和MediaSession12项全部通过。
mobile/home/maphost Debug lint均0 errors，warnings分别18/10/2；三个Debug构建成功，未安装。

shared的3个失败均发生在原`AmbientWorkerOwnerLockSymlinkTest`创建符号链接时，
Windows返回“客户端没有所需的特权”；另2个原`BydCarPlayCallQuotingTest`环境用例跳过。
没有修改测试或系统权限。随后剩余CI命令退出0不覆盖这些失败；5.2继续OPEN。

手机第一次最终回归与DiPlay较重CI并行，原
`IapLinkSynchronizationTest.delayedCumulativeAckIsSentWhenThresholdIsNotReached`失败一次；
该用例以40ms等待检查120ms延迟ACK，结果可能受调度影响，本轮未确定根因或修改用例。
停止并行构建后的串行回归成功，首次失败XML保留在
`local-backups/2026-11-14-align-business/phase-4-first-test-results/`。

## 复现与输入

手机准备使用干净DiPlay checkout的18个原源文件哈希、2个原body哈希。
schema 2登记所有暂存源码、合同及init的字节哈希；已执行篡改反例，结果工具拒绝修改，
随后恢复原字节并成功复核。Debug生产Kotlin输出protocol-carplay 548、宿主57个class，
均无接收或联测类。未使用`--full`，本轮没有宣称全部Release/flavor检查通过。

手机最终命令：

```powershell
$env:JAVA_HOME='C:\Users\admin\.jdks\openjdk-24.0.2+12-54'
$env:GIT_CONFIG_COUNT='2'
$env:GIT_CONFIG_KEY_0='safe.directory'
$env:GIT_CONFIG_VALUE_0='C:/Users/admin/IdeaProjects/carvex-carplay-research'
$env:GIT_CONFIG_KEY_1='safe.directory'
$env:GIT_CONFIG_VALUE_1='C:/Users/admin/IdeaProjects/carvex-carplay-research/android'
Set-Location -LiteralPath C:/Users/admin/IdeaProjects/carvex-carplay-research/android
.\gradlew.bat :protocol-carplay:testDebugUnitTest :bridge:testDebugUnitTest :host-carlife-mixing:testDebugUnitTest :app:compileXiaomiDebugKotlin --offline --console=plain --no-configuration-cache -I build/receiver-interop/receiver-tests.init.gradle
python -X utf8 -B tools/receiver-interop/verify_results.py
```

DiPlay完整CI任务与剩余任务命令见[执行记录](execution.md)和[验证入口](validation.md)。
原镜像C16/C18、9个完整消息body、6个注册及8个构造锚点本轮通过，范围仍为局部静态核对。

[可追溯摘要](validation-results-20261114.json)登记双方提交、原源/body/暂存/工具哈希、
逐模块XML组合哈希、lint和APK哈希、生产class组合哈希及实际命令退出状态。
XML组合算法：按报告文件名排序，依次拼接UTF-8文件名和原XML字节后计算SHA256。
class组合算法相同，名称使用相对路径。逐XML哈希和完整报告存放于
`local-backups/2026-11-14-align-business/validation-summary.json`及`final-test-results/`。
详细摘要SHA256：`69b1d6f967604aa4d0332b5b7a0127073077dc54e364665ea83e7a55c5efd014`。
最终文档相对链接、25项任务号与OPEN列表一致性及`git diff --check`通过；未运行OpenSpec CLI严格校验。

## 剩余任务

5.1/5.3按本地代码范围完成。1.3实际SUS/Resume、2.3真实播放器请求provider、
4.1文字长度计量、4.2距离实车角色、4.3真实时间/ETA、4.4真实lane来源、
5.2完整CI及5.4实车验证保持OPEN。
本轮没有车机屏显观察；接收源码合同与Debug构建不能代替实车验证。
