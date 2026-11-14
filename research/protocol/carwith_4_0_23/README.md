# CarWith 4.0.23 字段与接口分析

分析输入：`CarWith_4.0.23-20261016.apk`，日期 2026-11-12。

[打开 HTML 阅读版与搜索表](CarWith字段与接口分析.html) · [主报告 Markdown](REPORT.md) · [完整机器清单](INVENTORY.md)

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


[Protobuf 附录](APPENDIX_PROTO.md) · [Binder 附录](APPENDIX_BINDER.md) · [模型/配置附录](APPENDIX_MODELS.md) · [URL 附录](APPENDIX_URLS.md)

[2026-11-14 全程剩余距离复查](ROUTE_DISTANCE.md)：核对`destinationRemainingDistance`及原生概要文本候选，
撤下`total_distance`试验；真实混合回调provider仍OPEN。

本目录包含文档、CSV/JSON 清单、关键原始反汇编和可复现工具。所有结果为静态分析，未测试远端接口。
