# 文档交付验证

2026-11-14实施验收见[最终本地结果](final-validation.md)及[哈希摘要](validation-results-20261114.json)。
以下2026-11-12内容保留为计划阶段历史记录，不代表当前实施状态。

日期：2026-11-12。状态：计划文档已形成；实现与实车验收均未开始。

## 本次检查

- `proposal.md`、`design.md`、`tasks.md`、3 份 capability delta specs、schema 配置及输入快照齐备。
- 25 项后续任务均未勾选，覆盖阶段 0–5，任务号唯一。
- 13 个 requirement 均含 SHALL/MUST，21 个 scenario 均包含 WHEN/THEN。
- 本地相对链接和 UTF-8/空白检查通过；新增本文档链接亦纳入最终检查。
- [baseline.json](baseline.json) 的 29 个源文件/规范输入哈希复核一致；手机与 DiPlay 的 HEAD、工作区均未改变。
- 研究仓库的既有 `.gitignore` 修改、91 号未跟踪文档及 firmware 工作区变化不包含在此次计划提交中。

本机未找到 OpenSpec CLI，本次执行的是本地文档结构、链接与输入快照检查，
没有运行 `openspec validate --strict`。以上结果不能解释为 OpenSpec CLI 严格校验、
固件原指令复跑、业务行为回归或实车互通通过。

最终还执行 `git diff --check` 并审查暂存文件清单，仅提交本 OPSX 变更与文档索引。

## 后续实施验证入口

具备 OpenSpec CLI 时，从研究仓库执行：

```powershell
openspec validate align-business-lifecycle-and-push-fields --strict
```

手机端每项修改从 `android/` 执行受影响模块回归及仓库最低检查；
默认生产编译不引入外部接收源码：

```powershell
.\gradlew.bat :protocol-carplay:testDebugUnitTest :app:compileXiaomiDebugKotlin
```

bridge/host 等模块发生变化时追加它们的检查。命令、环境限制和测试范围以
[Android 规则](../../../android/AGENT.md)为准，不用本例替代受影响模块的检查。

接收源码联测使用实际指定路径，并按[工具说明](../../../android/tools/receiver-interop/README.md)
核对输入和结果。该路径是本次用户指定的 DiPlay，不写入或安装外部项目：

```powershell
python -X utf8 -B tools/receiver-interop/prepare.py C:/Users/admin/IdeaProjects/DiPlay
.\gradlew.bat :protocol-carplay:testDebugUnitTest :host-carlife-mixing:testDebugUnitTest `
  --offline --console=plain --no-configuration-cache `
  -I build/receiver-interop/receiver-tests.init.gradle
python -X utf8 -B tools/receiver-interop/verify_results.py
```

若修改 DiPlay，从其仓库执行 AGENTS.md 指定的完整 CI 检查：

```powershell
.\gradlew.bat :shared:testDebugUnitTest :common:testDebugUnitTest :home:testDebugUnitTest `
  :mobile:lintDebug :home:lintDebug :maphost:lintDebug `
  :mobile:assembleDebug :home:assembleDebug :maphost:assembleDebug
```

上述 Gradle、联测及实车命令本次均未执行。未来每项任务记录自己的提交、命令、退出码、
有效报告及真实屏显观察；历史测试计数不作为本次实现验收。
