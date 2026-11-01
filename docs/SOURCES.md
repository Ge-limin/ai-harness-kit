# 来源与公司资料链接

本包保留个人工作规范、配置示例、工具源码和知识工作资料。公司文档通过 GitHub 链接提供，由对应仓库维护。

下方来源表列出中文版本与共用文件；完整中英文来源及对应关系见 [manifest.json](manifest.json)。

## 公司资料

以下仓库为私有仓库，请使用有相应读取权限的 GitHub 账号打开。链接指向远端分支中的正文；公司资料不作为个人配置接入的前置条件。

| 仓库 | 文件 | 状态 |
| --- | --- | --- |
| AIJobMap | [AGENTS.md](https://github.com/StartLinks/AIJobMap/blob/dev/AGENTS.md) | 远端可读 |
| AIJobMap | [development-workflow.md](https://github.com/StartLinks/AIJobMap/blob/dev/docs/contracts/development-workflow.md) | 本地新版待同步 |
| AIJobMap | [local-full-start/SKILL.md](https://github.com/StartLinks/AIJobMap/blob/dev/.agents/skills/local-full-start/SKILL.md) | 远端可读 |
| AIJobMap | [ship-release/SKILL.md](https://github.com/StartLinks/AIJobMap/blob/dev/.agents/skills/ship-release/SKILL.md) | 本地新版待同步 |
| AIJobMap | [repository-deployment.md](https://github.com/StartLinks/AIJobMap/blob/dev/.agents/skills/ship-release/references/repository-deployment.md) | 本地新版待同步 |
| AIJobMap | [post-release-acceptance.md](https://github.com/StartLinks/AIJobMap/blob/dev/.agents/skills/ship-release/references/post-release-acceptance.md) | 本地新版待同步 |
| BonjourAIO | [AGENTS.md](https://github.com/StartLinks/BonjourAIO/blob/main/AGENTS.md) | 远端可读 |
| BonjourAIO | [local-integration-tests.md](https://github.com/StartLinks/BonjourAIO/blob/main/docs/infra/local-integration-tests.md) | 远端可读 |
| bonjour-business-entry-point | [AGENTS.md](https://github.com/StartLinks/bonjour-business-entry-point/blob/main/AGENTS.md) | 远端可读 |
| bonjour-engineering-entry-point | [AGENTS.md](https://github.com/StartLinks/bonjour-engineering-entry-point/blob/main/AGENTS.md) | 远端可读 |
| bonjour-engineering-entry-point | [repository-conventions.md](https://github.com/StartLinks/bonjour-engineering-entry-point/blob/main/docs/catalog/repository-conventions.md) | 远端可读 |
| bonjour-engineering-entry-point | `docs/operations/air-execution.md` · [源仓库](https://github.com/StartLinks/bonjour-engineering-entry-point) | 文档待同步 |
| bonjour-engineering-entry-point | `docs/operations/limin-database-access.md` · [源仓库](https://github.com/StartLinks/bonjour-engineering-entry-point) | 文档待同步 |

“本地新版待同步”的链接可查看远端现有版本；“文档待同步”目前只提供仓库入口。状态依据 2026-10-30 的远端核对结果。

## 个人资料与配置

配置中的 `REDACTED_SUPPLY_YOUR_OWN_CREDENTIAL` 及 `<...>` 是需由使用者填写的占位值。接入时由 Agent 根据目标环境生成有效配置；JSON/TOML 字符串中的占位内容不会自行展开。具体依赖与路径要求见 [DEPENDENCIES.md](DEPENDENCIES.md)。

- `translated`：中文源文件的英文译文，对应关系记录在 manifest 的 `translation_of`。
- `original`：保留的个人规范、工具源码或规格文本。
- `adapted`：为分享整理的配置示例或参考资料。

插件的公开来源、版本与许可证见 [DEPENDENCIES.json](DEPENDENCIES.json)；第三方技能见[技能索引](../reference/skills/README.md)。下表由 `tools/build-guide.py` 从 [manifest.json](manifest.json) 生成。

<!-- SOURCES:START -->
| 原始来源 | 包内文件 | 状态 |
|---|---|---|
| `个人工作规范 / PRINCIPLES.general.md` | [rules/PRINCIPLES.general.md](../rules/PRINCIPLES.general.md) | original |
| `个人工作规范 / PRINCIPLES.codex.md` | [rules/PRINCIPLES.codex.md](../rules/PRINCIPLES.codex.md) | original |
| `个人工作规范 / harness/sync.py` | [rules/harness/sync.py](../rules/harness/sync.py) | adapted |
| `个人工作规范 / harness/sync.sh` | [rules/harness/sync.sh](../rules/harness/sync.sh) | original |
| `个人工作规范 / harness/targets.yaml` | [rules/harness/targets.yaml](../rules/harness/targets.yaml) | adapted |
| `个人工作规范 / harness/requirements.txt` | [rules/harness/requirements.txt](../rules/harness/requirements.txt) | original |
| `个人工作规范 / harness/test_sync.py` | [rules/harness/test_sync.py](../rules/harness/test_sync.py) | adapted |
| `个人配置 / codex/config.toml` | [configs/codex/config.toml](../configs/codex/config.toml) | adapted |
| `个人配置 / codex/hooks.json` | [configs/codex/hooks.json](../configs/codex/hooks.json) | original |
| `个人配置 / pi/settings.json` | [configs/pi/settings.json](../configs/pi/settings.json) | adapted |
| `个人配置 / pi/models.json` | [configs/pi/models.json](../configs/pi/models.json) | adapted |
| `个人配置 / pi/subagents.json` | [configs/pi/subagents.json](../configs/pi/subagents.json) | original |
| `个人配置 / pi/pi-fff.json` | [configs/pi/pi-fff.json](../configs/pi/pi-fff.json) | original |
| `个人配置 / pi/sol-pi.json` | [configs/pi/sol-pi.json](../configs/pi/sol-pi.json) | original |
| `个人配置 / pi/web-search.json` | [configs/pi/web-search.json](../configs/pi/web-search.json) | original |
| `个人配置 / claude/settings.json` | [configs/claude/settings.json](../configs/claude/settings.json) | adapted |
| `个人配置 / claude/statusline.sh` | [configs/claude/statusline.sh](../configs/claude/statusline.sh) | original |
| `个人配置 / claude/commands/hand-off.md` | [configs/claude/commands/hand-off.md](../configs/claude/commands/hand-off.md) | original |
| `个人配置 / magpie/codex-gpt-6-astra.spec.txt` | [configs/magpie/codex-gpt-6-astra.spec.txt](../configs/magpie/codex-gpt-6-astra.spec.txt) | original |
| `包内双语说明 / reference/skills/README.md` · `aba2be79b117` | [reference/skills/README.md](../reference/skills/README.md) | adapted |
| `包内双语说明 / docs/DEPENDENCIES.md` · `aba2be79b117` | [docs/DEPENDENCIES.md](../docs/DEPENDENCIES.md) | adapted |
| `包内双语说明 / docs/SOURCES.md` · `aba2be79b117` | [docs/SOURCES.md](../docs/SOURCES.md) | adapted |
| `包内双语说明 / docs/validation.md` · `aba2be79b117` | [docs/validation.md](../docs/validation.md) | adapted |
| `包内说明 / README.md` | [README.md](../README.md) | adapted |
<!-- SOURCES:END -->
