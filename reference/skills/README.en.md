# Skills and sources

Obtain third-party skills from the maintainers listed below. Originals of the skills maintained in our projects are linked at the end.

## Orca

Source: [Orca documentation](https://www.onorca.dev/docs/) · [Orca app releases](https://github.com/stablyai/orca/releases). These skills ship with the Orca application.

| Skill | Purpose |
| --- | --- |
| `orca-cli` | Worktrees, terminals, embedded browser, and handoffs |
| `computer-use` | Control visible local application windows |
| `orchestration` | Multi-agent task coordination and messaging |
| `orca-linear` | Work with Linear issues through Orca |

## CodexHost

Source: [BytePioneer-AI/codex-host](https://github.com/BytePioneer-AI/codex-host). Distributed with `@codexhost/cli`.

- `codexhost-delegation`: Delegate agent tasks and read or follow up on external sessions.

## Lark CLI

Source: [larksuite/cli](https://github.com/larksuite/cli). Located at `skills/<skill-name>/SKILL.md` in the upstream repository.

| Skill | Purpose |
| --- | --- |
| `lark-doc` | Lark documents and Wiki content |
| `lark-minutes` | Lark Minutes and audio/video outputs |
| `lark-note` | Meeting-note details and transcripts |
| `lark-openapi-explorer` | Discover native Lark OpenAPI endpoints |

## Pi Processes

Source: [aliou/pi-processes](https://github.com/aliou/pi-processes). Package: `@aliou/pi-processes`.

- `pi-processes`: Background processes, log watches, and lifecycle management.

## Pi Lens

Source: [apmantza/pi-lens](https://github.com/apmantza/pi-lens). Package: `pi-lens`; author: Apostolos Mantzaris.

| Skill | Purpose |
| --- | --- |
| `pi-lens-ast-grep` | Structural code search and replacement |
| `pi-lens-lsp-navigation` | Code navigation and language-server diagnostics |
| `pi-lens-write-ast-grep-rule` | Write ast-grep rules |
| `pi-lens-write-tree-sitter-rule` | Write Tree-sitter query rules |

Provenance comes from Orca’s bundled-skill manifest, CodexHost’s CLI package metadata, the Lark skill installation records, and the Processes and Lens package metadata. See [runtime requirements](../../docs/DEPENDENCIES.en.md) for Pi versions and dependencies.

## Maintained project skills

These skills are maintained in company repositories and require repository access. See the [company reference index](../../docs/SOURCES.en.md) for version availability.

| Project | Original skill |
| --- | --- |
| AIJobMap | [local-full-start](https://github.com/StartLinks/AIJobMap/blob/dev/.agents/skills/local-full-start/SKILL.md) — Start the full local environment |
| AIJobMap | [ship-release](https://github.com/StartLinks/AIJobMap/blob/dev/.agents/skills/ship-release/SKILL.md) — Release the project |
