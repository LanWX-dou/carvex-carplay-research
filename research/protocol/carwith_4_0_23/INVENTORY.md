# 完整机器清单与复现说明

日期：2026-11-12。所有清单为离线静态结果。全量 DEX 表含依赖 SDK/资源类/生成代码，不应把这些行数当作业务 API 或线上参数数量。

| 文件 | 数据行数 | 字节数 | 说明 |
| --- | --- | --- | --- |
| [action_literals.csv](inventory/action_literals.csv) | 239 | 11296 | 239 条 action/调用标识字面量，候选集 |
| [all_dex_fields.csv](inventory/all_dex_fields.csv) | 497769 | 57524400 | 全 8 个 DEX 的所有定义字段；含资源/SDK/Protobuf，非网络参数计数 |
| [all_dex_methods.csv](inventory/all_dex_methods.csv) | 233147 | 47666430 | 全 DEX 的所有定义方法；含类型、权限标志、偏移、方法及参数注解 |
| [apk_entries.csv](inventory/apk_entries.csv) | 4969 | 198052 | 4,969 条顶层 ZIP 文件条目/尺寸/CRC |
| [application_fields.csv](inventory/application_fields.csv) | 177093 | 18935800 | 指定应用/集成 SDK 包前缀字段；含大量生成代码 |
| [application_interfaces.csv](inventory/application_interfaces.csv) | 2021 | 292412 | 指定包前缀的全部 Java 接口方法；含 Protobuf OrBuilder 等 |
| [application_literals.csv](inventory/application_literals.csv) | 28069 | 5123409 | 已选择应用与入口类中的 const-string 原字面量/偏移 |
| [asset_json_fields.csv](inventory/asset_json_fields.csv) | 1128 | 91186 | 1,128 条包内 JSON 配置路径/类型/首个静态样例 |
| [binder_methods.csv](inventory/binder_methods.csv) | 616 | 99107 | 122 个 Binder 接口中的 616 个方法 |
| [binder_transactions.csv](inventory/binder_transactions.csv) | 576 | 64190 | 576 条 Stub 事务常量；可按类/方法联表 |
| [business_model_fields.csv](inventory/business_model_fields.csv) | 158 | 16319 | 158 个重点业务模型实例成员 |
| [components.csv](inventory/components.csv) | 115 | 11698 | 115 个 Manifest 组件、导出状态、权限、authority 与 action |
| [control_constants.csv](inventory/control_constants.csv) | 62 | 5179 | ControlChannel 静态常量 |
| [enum_annotation_markers.csv](inventory/enum_annotation_markers.csv) | 883 | 215541 | 883 个无 JSON 名称的枚举字段标记 |
| [http_routes.csv](inventory/http_routes.csv) | 4 | 1513 | 4 个混淆 Retrofit 注解接口；另外三条代码构造路径见主报告 |
| [javascript_interfaces.csv](inventory/javascript_interfaces.csv) | 7 | 696 | 7 个 JavascriptInterface Java 方法 |
| [key_usage.csv](inventory/key_usage.csv) | 2185 | 652988 | Intent/Bundle/JSONObject/Map/Preference/Cursor 的常量键使用和调用类型 |
| [native_exports.csv](inventory/native_exports.csv) | 21265 | 2036331 | 21,265 条 ELF 动态符号表定义的全局/弱符号；含支持库符号 |
| [native_methods.csv](inventory/native_methods.csv) | 182 | 18486 | 182 个 DEX native 方法定义与签名 |
| [nested_archive_entries.csv](inventory/nested_archive_entries.csv) | 321 | 23642 | 321 条嵌套 ZIP/RPK 文件条目 |
| [proto_enums.csv](inventory/proto_enums.csv) | 157 | 8414 | 157 个包内 Protobuf 枚举值 |
| [proto_fields.csv](inventory/proto_fields.csv) | 342 | 22979 | 342 个包内 Protobuf 字段/tag/类型/源码行 |
| [relative_path_candidates.csv](inventory/relative_path_candidates.csv) | 291 | 27920 | 291 个相对路径候选；含文件路径，未全部判为 API |
| [sdk_ai_model_fields.csv](inventory/sdk_ai_model_fields.csv) | 10828 | 2876065 | 10,828 个小爱 SDK 实例模型字段；未确认当前业务使用 |
| [serialized_fields.csv](inventory/serialized_fields.csv) | 266 | 50313 | 266 个明确 JSON 属性名称 |
| [url_references.csv](inventory/url_references.csv) | 297 | 49868 | 297 条已选择类中的 URL/URI 引用指令，部分为 SDK/文档 |
| [urls.csv](inventory/urls.csv) | 318 | 43276 | 318 次 DEX 字符串表中的 URL/URI 候选出现 |
| [uuid_literals.csv](inventory/uuid_literals.csv) | 123 | 6934 | 123 条 UUID 字面量；未全部判为蓝牙业务 UUID |
| [wire_service_ids.csv](inventory/wire_service_ids.csv) | 23 | 2903 | 23 条直接从封包构造代码恢复的消息/serviceId 映射 |

## JSON、源码和验证证据

- `manifest.json`：APK SHA-256、各 DEX/原生库尺寸与哈希、覆盖统计。
- `inventory/classes.json`：全部类定义、字段、方法、访问标志和注解；体积较大，可按 class 查询。
- `inventory/assembly_verification.json`：33,418 类与重新生成的 dexdump 逐字节对比结果。
- `inventory/proto_schema_validation.json`：每个包内 Protobuf 字段的编译 tag 核对结果。
- `inventory/http_annotations.json`：4 个混淆后 HTTP 定义的原注解和参数注解。
- `inventory/file_manifest.json`：每份 CSV 的行数、尺寸与 SHA-256。
- `source/AndroidManifest.xml`：从二进制 AXML 解析的可读 Manifest。
- `source/ucar.proto`、`source/share.proto`：包内 schema；仅规范换行，未修复原注释乱码。
- `source/assets/`：包内可解析 JSON 的原始文件。
- `source/dexdump/`：被报告引用的关键类原始反汇编。
- `source/*.so.strings.txt`：原生库相关可打印字符串，不是完整函数反编译。

## 复现

本机 Python 标准库与 Android SDK 36.0.0 即可完成；没有下载安装依赖。运行位置为仓库根目录。

```powershell
python -X utf8 research/protocol/carwith_4_0_23/tools/extract.py "C:\Users\admin\Desktop\CarWith_4.0.23-20261016.apk" --cache local-backups/carwith-navigation-apk
python -X utf8 research/protocol/carwith_4_0_23/tools/verify_assembly.py "C:\Users\admin\Desktop\CarWith_4.0.23-20261016.apk" --cache local-backups/carwith-navigation-apk
python -X utf8 research/protocol/carwith_4_0_23/tools/enrich.py "C:\Users\admin\Desktop\CarWith_4.0.23-20261016.apk" --cache local-backups/carwith-navigation-apk
python -X utf8 research/protocol/carwith_4_0_23/tools/supplement.py "C:\Users\admin\Desktop\CarWith_4.0.23-20261016.apk" --cache local-backups/carwith-navigation-apk
python -X utf8 research/protocol/carwith_4_0_23/tools/build_report.py
```

缓存使用现有的 `local-backups/carwith-navigation-apk/classes*/all-classes.zip` 与 `references.jsonl`。先核对 APK DEX 哈希，再逐类核验缓存反汇编。缓存未随文档包重复拷贝；主报告涉及的类已保存到 source/dexdump。`extract.py` 不带 cache 也能提取基本定义、Manifest、原生字符串与资源；跨引用与补充工具需要已核验缓存。

`tools` 的 SDK 路径可根据本机修改。输出都写在本分析目录，不改 APK。复现工具与文档的所有计数均来自实际清单，不声明网络可用性。
