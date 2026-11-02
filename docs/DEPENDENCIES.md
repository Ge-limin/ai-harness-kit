# 公开配置与外部依赖

这些配置保留模型、推理强度、上下文窗口、自主执行模式、插件开关和并发选择。接入 Agent 应先填写安装路径与凭据，再将配置安装到目标环境。

## 接入入口

JSON/TOML 中的 `<...>` 是需要接入 Agent 替换的占位符，不能直接执行。将它们替换为目标机器上已核实的完整路径，并保持 JSON/TOML 的转义规则；不要假定这些字段会展开 `~` 或 `$HOME`。同名占位符应使用相同值。

| 占位符 | 填写内容 |
|---|---|
| `<SOL_PI_INSTALL_PATH>` | `sol-pi` 0.1.1 定制实现的安装目录 |
| `<PI_LOCAL_FILE_LINKS_INSTALL_PATH>` | `pi-local-file-links` 0.1.0 定制实现的安装目录 |
| `<CLAUDE_STATUSLINE_SCRIPT_PATH>` | 随包 `configs/claude/statusline.sh` 在目标机器上的路径 |
| `<CODEX_COMPUTER_USE_CLIENT_PATH>` | Codex Computer Use 的 `SkyComputerUseClient` 可执行文件 |
| `<CODEX_COMPUTER_USE_WORKING_DIRECTORY>` | Computer Use MCP 的工作目录 |
| `<CODEX_COMPUTER_USE_APP_PATH>` | Codex Computer Use 应用目录 |
| `<NODE_REPL_EXECUTABLE_PATH>` | 宿主提供的 `node_repl` 可执行文件 |
| `<NODE_REPL_NODE_EXECUTABLE_PATH>` | 与该宿主匹配的 Node 可执行文件 |
| `<NODE_REPL_NODE_MODULES_PATH>` | 该宿主提供的 Node 模块目录 |
| `<CODEX_HOME_PATH>` | 目标环境的 Codex 配置目录 |
| `<CODEX_BROWSER_SERVICE_SCRIPT_PATH>` | 与宿主版本匹配的 `browser-service.mjs` |
| `<CODEX_CLI_EXECUTABLE_PATH>` | 宿主提供的 Codex CLI 可执行文件 |
| `<OPENAI_BUNDLED_MARKETPLACE_PATH>` | 宿主提供的 `openai-bundled` 插件市场目录 |
| `<OPENAI_PRIMARY_RUNTIME_MARKETPLACE_PATH>` | 宿主提供的 `openai-primary-runtime` 插件市场目录 |

`NODE_REPL_TRUSTED_CODE_PATHS` 保留原配置的冒号分隔路径列表；接入 Agent 应按目标平台要求填写。`NODE_REPL_TRUSTED_SERVICES` 是 TOML 字符串中的 JSON，替换路径时需同时保持两层格式有效。五个身份字段保留 `REDACTED_SUPPLY_YOUR_OWN_CREDENTIAL`，由使用者提供自己的凭据。

`rules/harness/targets.yaml` 的目标路径可以使用 `~`：同目录 `sync.py` 的 `resolve_path()` 明确调用 `Path.expanduser()`。Orca hook 中的 `${HOME-}` 由 shell 展开。两者都有实际执行语义支持。

## 外部依赖

| 配置引用 | 接入要求 |
|---|---|
| Pi 的七个 npm 包 | `configs/pi/settings.json` 使用 Pi 支持的 `npm:包名@版本` 格式，保留原版本与顺序。具体来源、获取地址和完整性值见 [DEPENDENCIES.json](DEPENDENCIES.json)。 |
| `sol-pi`、`pi-local-file-links` | 向维护者获取匹配版本的定制实现并填写上述路径；运行实现未包含在本包中。 |
| Orca hooks | 宿主提供平台对应的 hook 脚本、会话环境变量和事件服务；配置保留事件、调用方式和平台分支。 |
| Claude 状态栏 | 随包提供 [statusline.sh](../configs/claude/statusline.sh)，运行需要 Bash、jq、awk、Git、date、basename 和客户端 stdin JSON。 |
| Codex `context7`、`playwright` | PATH 中的 Node/npm/npx 及对应 npm 包；保留原参数，包括 `@latest`。 |
| Codex `codegraph` | PATH 中的 `codegraph` 命令、匹配的 Node 运行环境和目标仓库索引；启动参数为 `serve --mcp`。 |
| Codex 官方开发文档 | 保留 `https://developers.openai.com/mcp` 官方地址。 |
| Codex Computer Use、`node_repl`、notify 与本地插件市场 | 对应宿主应用及其匹配组件，由接入 Agent 填写路径；保留版本字段、插件开关及 Computer Use MCP 的禁用状态。 |
| Codex `datagrip` | 本机 DataGrip MCP Server；`http://127.0.0.1:64402/stream` 保留为本地端口示例。 |
| 本地模型服务 | `127.0.0.1:3425` 的服务需支持相应 API 和模型；官方模型服务地址保留，凭据由使用者提供。 |
| Pi 子 Agent | Pi、Subagents、角色定义及角色使用的扩展；[并发配置](../configs/pi/subagents.json) 保留最大并发 10 和整体中断行为。 |

## 来源与许可

[DEPENDENCIES.json](DEPENDENCIES.json) 记录九个插件的版本、上游来源、作者、运行依赖、获取方式和已有的六份许可全文。七个 npm 来源有版本、获取地址和完整性记录；本次未重新下载或执行这些插件。`sol-pi` 没有可移植来源记录；`pi-local-file-links` 虽声明 Git 仓库，但没有对应定制版本的提交记录，需要向维护者获取匹配实现。该插件声明的 Pi 兼容范围是 `>=0.86.0 <0.88.0`，需在接入环境确认兼容性。

`@aliou/pi-processes` 和 `@ff-labs/pi-fff` 仅有 MIT 声明，许可全文需从分发来源获取。`pi-compact-ui` 有 npm 获取记录，原 manifest 未声明 repository/license，许可状态待确认。已有作者、版权信息和上游来源完整保留。

此公开配置已做静态格式与保留项验证。未执行配置模板、hook、MCP、模型请求或目标机器安装；填入路径后的实际运行由接入环境验收。
