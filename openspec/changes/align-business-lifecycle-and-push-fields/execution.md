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

## 0.3 字段、源链与复现条件

0.2 独立提交为 ed7425f。本项新增 [字段对账表](field-matrix.md)，登记当前音乐全部 Track 属性、导航核心及未启用扩展的源链、接收用途、缺失/清除/零、单位与能力边界；为每个候选差异指定测试入口或真实 provider/原字节/实车待证条件。

两端生产 HEAD 未变。本项仅做源码对账；未运行 Gradle或实车验证。执行 baseline verifier 与 git diff --check 通过。

## 1.1 音乐 bootstrap owner 修正

手机提交 `27ee5f0`；0.3 文档提交 `0eba279`。
删除无人消费的全局 pendingSubscription 和 Bluetooth 的虚假成功回调；无当前 Link 发布器时明确未支持，
新 AirSession 必须独立认证并接收自己的 START。依据、差异与测试范围见
[修正记录](../../../android/docs/fixes/2026-11-12-music-bootstrap-owner.md)。

执行并成功退出（83 tasks：13 executed、70 up-to-date）：

```powershell
.\gradlew.bat :protocol-carplay:testDebugUnitTest :bridge:testDebugUnitTest :app:compileXiaomiDebugKotlin --offline --console=plain --no-configuration-cache
```

协议/bridge JUnit 共148 suites、1213 tests，failure/error/skipped均0；新增真实Link/CSM边界用例确实在本轮XML中。
按模块及文件名排序后拼接文件名+XML的SHA256为
`0b20c2a3eb5aeddafb9a0f471248ece417fb3e027900c40d8a35068496b4428f`。
默认编译没有加载接收源码。git diff --check通过；备份位于local-backups任务1.1目录。
没有打包、安装或实车验证。Bluetooth音乐发布器未实现，完整Apple早期业务路径仍OPEN。

## 1.2 音乐在途撤销

手机提交 `1a66476`。初始、快照和增量5001携带原子订阅代际；AirSession合并源owner/关闭guard。
START替换、STOP、linkReady边界撤销尚未提交工作；非法START保留旧订阅；已提交CSM继续可靠传输。
详见[修正记录](../../../android/docs/fixes/2026-11-12-music-queued-revocation.md)。

本轮 `:protocol-carplay:testDebugUnitTest :app:compileXiaomiDebugKotlin --offline --console=plain --no-configuration-cache`
成功退出；76 tasks中8 executed/68 up-to-date。协议140 suites/1156 tests，failure/error/skipped均0，
其中6个新增guarded writer用例全部执行。按XML文件名排序，拼接文件名+内容的SHA256：
`846d90607d830a19877ed27892817010cc90f80cf30f470d2f6741f3df1443d9`。
git diff --check通过，任务1.2备份完成。没有打包/安装/实车验证。

## 1.3 挂起/恢复对账（OPEN）

实际IapLink拒绝含08控制帧并进入runtime失败关闭，尚无已接受SUS/经确认Resume入口。
本项[对账记录](lifecycle-boundaries.md)明确ACK、平台休眠、流关闭的区别及完整实施待证条件。
1.3未勾选；没有把失败关闭称为挂起支持，没有新增transport行为或实车结论。
继续独立推进无需该未证恢复路径的清理与字段任务。

## 1.4 会话音乐清理

手机提交 `43bf259`；relay注册Resources，close释放回调/快照、拒绝晚到update/attach，
publisher永久close撤销待发送工作，AirSession停止/资源释放均关闭发布器，桥接释放图片及Air引用。
详见[清理记录](../../../android/docs/fixes/2026-11-12-music-owner-cleanup.md)。
本轮协议/bridge单测和小米编译成功（同1.1命令），83 tasks中12 executed/71 up-to-date。
149 suites/1222 tests，failure/error/skipped均0；新增detach/close/真实writer关闭用例执行。
git diff --check通过，任务1.4备份完成。没有打包/安装/实车验证；更细的封面引用撤销继续2.4。

## 2.1 5000订阅合同

按0.2原字节核对既有selection，新增未知顶层无nested解析、组2空flag及后置非法组保留旧writer guard回归。
顺序/重复、U32子项11、非法替换均与已核局部合同一致；本地资源上限与组2高ID防御不当作线上上限。
详见[合同记录](../../../android/docs/fixes/2026-11-12-nowplaying-subscription-contract.md)。
本轮协议单测和小米编译成功（同1.2命令），76 tasks中4 executed/72 up-to-date；
140 suites/1159 tests，failure/error/skipped均0；生产解析器未改。git diff --check通过，备份任务2.1。
没有打包/安装/实车验证。

## 2.3 请求/实况分离（provider OPEN）

5003原子解析为原始U32；只有ffffffff为auto。独立p2窗口订阅门、p0/p1无START-active门；
request hook接受不冒充播放完成。生产无provider时拒绝且不回写快照/发送5001。
[修正记录](../../../android/docs/fixes/2026-11-12-nowplaying-set-info-request.md)登记真实provider/单位/反馈仍OPEN，
2.3完整验收保持未勾选。2.2手机提交为 `571530b`。
首次编译误用不存在的U32 helper，改为大端ByteBuffer+无符号mask后，本轮协议单测和小米编译成功，
76 tasks中7 executed/69 up-to-date；141 suites/1163 tests，failure/error/skipped均0。
git diff --check通过，备份任务2.3；没有打包/安装/实车验证。

## 2.2 换曲媒体文本清除

仅替换时显式清除旧已知媒体文本，省略未知数字；START初始默认消息保持独立顺序。
详见[修正记录](../../../android/docs/fixes/2026-11-12-nowplaying-replacement-text.md)。
新增实际DiPlay parser用例确认artist/album清空、增量保留、零进度有效及未知duration未补零。
数字无清除证据时接收旧duration可能保留，此限制明确OPEN。

执行 `prepare.py C:/Users/admin/IdeaProjects/DiPlay`（干净615b32c，14源哈希/2原body），然后
`:protocol-carplay:testDebugUnitTest :bridge:testDebugUnitTest :host-carlife-mixing:testDebugUnitTest :app:compileXiaomiDebugKotlin --offline --console=plain --no-configuration-cache -I build/receiver-interop/receiver-tests.init.gradle`。
首次1个新增单测未订阅artist却期待其输出，修正测试的实际订阅后成功退出：90 tasks中2 executed/88 up-to-date。
此次第二次仅协议单测重新执行，其余使用首次已成功的有效缓存报告；不记成全部重跑。
`verify_results.py`通过，含新增换曲的全部实际接收合同无失败/跳过；摘要保存在本地task-2.2备份目录。
git diff --check通过。未改DiPlay生产、未打包/安装/实车验证。
