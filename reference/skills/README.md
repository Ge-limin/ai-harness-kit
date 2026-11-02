# 技能名单与来源

第三方技能按以下名单从维护来源获取。项目内持续维护的技能原文见文末。

## Orca

来源：[Orca 官方文档](https://www.onorca.dev/docs/) · [Orca 应用分发](https://github.com/stablyai/orca/releases)。以下技能由 Orca 应用附带。

| 技能 | 用途 |
| --- | --- |
| `orca-cli` | 工作树、终端、嵌入式浏览器与任务交接 |
| `computer-use` | 操作可见的本机应用窗口 |
| `orchestration` | 多 Agent 任务编排与通信 |
| `orca-linear` | 通过 Orca 操作 Linear 工单 |

## CodexHost

来源：[BytePioneer-AI/codex-host](https://github.com/BytePioneer-AI/codex-host)，由 `@codexhost/cli` 提供。

- `codexhost-delegation`：委派 Agent 任务、读取及跟进外部会话。

## Lark CLI

来源：[larksuite/cli](https://github.com/larksuite/cli)，仓库内 `skills/<技能名称>/SKILL.md`。

| 技能 | 用途 |
| --- | --- |
| `lark-doc` | 飞书云文档与 Wiki 内容操作 |
| `lark-minutes` | 飞书妙记与音视频产物 |
| `lark-note` | 会议纪要详情及逐字记录 |
| `lark-openapi-explorer` | 探索飞书原生 OpenAPI |

## Pi Processes

来源：[aliou/pi-processes](https://github.com/aliou/pi-processes)，包名 `@aliou/pi-processes`。

- `pi-processes`：后台进程、日志观察与生命周期管理。

## Pi Lens

来源：[apmantza/pi-lens](https://github.com/apmantza/pi-lens)，包名 `pi-lens`，作者 Apostolos Mantzaris。

| 技能 | 用途 |
| --- | --- |
| `pi-lens-ast-grep` | 代码结构搜索与替换 |
| `pi-lens-lsp-navigation` | 代码导航与语言服务诊断 |
| `pi-lens-write-ast-grep-rule` | 编写 ast-grep 规则 |
| `pi-lens-write-tree-sitter-rule` | 编写 Tree-sitter 查询规则 |

来源依据：Orca 的随应用技能清单、CodexHost 的 CLI 包信息、飞书技能的安装来源记录，以及 Processes、Lens 的包信息。Pi 版本与依赖见[依赖说明](../../docs/DEPENDENCIES.md)。

## 自维护项目技能

以下技能由我们在公司仓库内维护，链接需要仓库权限。版本可用状态见[公司资料索引](../../docs/SOURCES.md)。

| 项目 | 技能原文 |
| --- | --- |
| AIJobMap | [local-full-start](https://github.com/StartLinks/AIJobMap/blob/dev/.agents/skills/local-full-start/SKILL.md) — 完整本地环境启动 |
| AIJobMap | [ship-release](https://github.com/StartLinks/AIJobMap/blob/dev/.agents/skills/ship-release/SKILL.md) — 项目发布 |
