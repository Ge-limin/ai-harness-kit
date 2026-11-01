# Public configuration and external dependencies

These configurations preserve model, reasoning, context-window, autonomous execution, plugin and concurrency choices. The integrating agent must fill in installation paths and credentials before installing them in the target environment.

## Integration entry point

The `<...>` values in JSON/TOML are placeholders for the integrating agent, not executable configuration. Replace them with verified full paths on the target machine, preserving JSON/TOML escaping. Do not assume these fields expand `~` or `$HOME`. Use the same value for every occurrence of a given placeholder.

| Placeholder | Required value |
|---|---|
| `<SOL_PI_INSTALL_PATH>` | Installation directory of the customized `sol-pi` 0.1.1 implementation |
| `<PI_LOCAL_FILE_LINKS_INSTALL_PATH>` | Installation directory of the customized `pi-local-file-links` 0.1.0 implementation |
| `<CLAUDE_STATUSLINE_SCRIPT_PATH>` | Target-machine path of the included `configs/claude/statusline.sh` |
| `<CODEX_COMPUTER_USE_CLIENT_PATH>` | Codex Computer Use `SkyComputerUseClient` executable |
| `<CODEX_COMPUTER_USE_WORKING_DIRECTORY>` | Working directory for the Computer Use MCP |
| `<CODEX_COMPUTER_USE_APP_PATH>` | Codex Computer Use application directory |
| `<NODE_REPL_EXECUTABLE_PATH>` | Host-provided `node_repl` executable |
| `<NODE_REPL_NODE_EXECUTABLE_PATH>` | Node executable matching that host |
| `<NODE_REPL_NODE_MODULES_PATH>` | Host-provided Node modules directory |
| `<CODEX_HOME_PATH>` | Codex configuration directory in the target environment |
| `<CODEX_BROWSER_SERVICE_SCRIPT_PATH>` | `browser-service.mjs` matching the host version |
| `<CODEX_CLI_EXECUTABLE_PATH>` | Host-provided Codex CLI executable |
| `<OPENAI_BUNDLED_MARKETPLACE_PATH>` | Host-provided `openai-bundled` marketplace directory |
| `<OPENAI_PRIMARY_RUNTIME_MARKETPLACE_PATH>` | Host-provided `openai-primary-runtime` marketplace directory |

`NODE_REPL_TRUSTED_CODE_PATHS` preserves the original colon-separated path list; the integrating agent must adapt it to the target platform. `NODE_REPL_TRUSTED_SERVICES` contains JSON inside a TOML string, so path replacement must preserve both formats. Five identity fields retain `REDACTED_SUPPLY_YOUR_OWN_CREDENTIAL`; users supply their own credentials.

Target paths in `rules/harness/targets.yaml` may use `~`: `resolve_path()` in the adjacent `sync.py` explicitly calls `Path.expanduser()`. `${HOME-}` in Orca hooks is expanded by the shell. Both forms have explicit runtime support.

## External dependencies

| Reference | Integration requirement |
|---|---|
| Seven Pi npm packages | `configs/pi/settings.json` uses Pi's supported `npm:package@version` syntax, preserving versions and order. See [DEPENDENCIES.json](DEPENDENCIES.json) for sources, acquisition URLs and integrity values. |
| `sol-pi`, `pi-local-file-links` | Obtain matching customized implementations from their maintainers and fill in the paths above; runtime implementations are not included. |
| Orca hooks | The host supplies platform-specific scripts, session environment variables and event services; configurations preserve events, invocations and platform branches. |
| Claude status line | The included [statusline.sh](../configs/claude/statusline.sh) requires Bash, jq, awk, Git, date, basename and the client's stdin JSON. |
| Codex `context7`, `playwright` | Node/npm/npx on PATH and the corresponding npm packages; original arguments, including `@latest`, are retained. |
| Codex `codegraph` | The `codegraph` command on PATH, its compatible Node runtime and an index of the target repository; arguments are `serve --mcp`. |
| Codex official developer documentation | The official MCP URL `https://developers.openai.com/mcp` is retained. |
| Codex Computer Use, `node_repl`, notify and local marketplaces | Matching host applications and components, with paths supplied by the integrating agent; version fields, plugin toggles and the disabled Computer Use MCP state are preserved. |
| Codex `datagrip` | A local DataGrip MCP Server; `http://127.0.0.1:64402/stream` is retained as a local-port example. |
| Local model service | A service on `127.0.0.1:3425` must support the configured APIs and models; official provider URLs are retained and users supply credentials. |
| Pi subagents | Pi, Subagents, role definitions and their extensions; the [concurrency configuration](../configs/pi/subagents.json) retains a maximum of 10 concurrent agents and the original global interrupt behavior. |

## Provenance and licensing

[DEPENDENCIES.json](DEPENDENCIES.json) records nine plugins, their versions, upstream sources, authors, runtime dependencies, acquisition methods and all six available license texts. Seven npm sources have recorded versions, URLs and integrity values; the plugins were not downloaded again or executed during this preparation. No portable source is recorded for `sol-pi`. Although `pi-local-file-links` declares a Git repository, no revision identifies the customized version; obtain the matching implementation from its maintainer. Its declared Pi compatibility range is `>=0.86.0 <0.88.0` and needs confirmation in the target environment.

`@aliou/pi-processes` and `@ff-labs/pi-fff` declare MIT; their full license texts must be obtained from their distribution sources. `pi-compact-ui` has an npm acquisition record, but its manifest declares neither repository nor license, so licensing remains unconfirmed. Existing authorship, copyright notices and upstream sources are preserved.

The public configuration has undergone static format and preservation checks. Configuration templates, hooks, MCP calls, model requests and target-machine installation were not executed; runtime validation follows integration in the target environment.
