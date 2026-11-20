# Verification

This principles sync checks verbatim Chinese source parity and corresponding English rules and guide updates. All four `sync.sh --dry-run` targets and the seven public-shell unit tests pass; global clients remain untouched. `tools/build-guide.py` generates the READMEs and guide, followed by embedded-byte, manifest-target, and local-link checks. This change uses generation and static checks; the browser coverage below comes from the existing review.

Local review coverage:

- Bundled files match their embedded HTML text, and provenance targets exist.
- Company references are GitHub links; their document bodies, data-source identifiers, execution-machine addresses and internal runtime parameters are excluded from attachments.
- JSON, TOML and YAML parse successfully. Model, reasoning, autonomous execution, plugin and concurrency choices are preserved; installation paths and credentials use explicit placeholders.
- Document-first filtering, configuration and script filters, folder filters, search, reading, copy, download and returning to the guide are checked in a browser.
- Chinese and English layouts are checked at desktop and mobile widths without page overflow or JavaScript errors.
- See [SOURCES.en.md](SOURCES.en.md) for company-link availability. Private repositories require access; pending updates remain with their source repositories.

Build with `python3 tools/build-guide.py`. Principles-export unit tests and a dry run were checked without writing client settings. Configuration templates, company commands and deployments were not executed. Validate runtime behavior in the target environment as described in [DEPENDENCIES.en.md](DEPENDENCIES.en.md).
