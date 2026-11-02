#!/usr/bin/env python3
"""Build the standalone guide with an offline library of the bundled sources."""
from __future__ import annotations

import json
from copy import deepcopy
from datetime import date
from pathlib import Path
from unicodedata import category
from urllib.parse import urlsplit

from lxml import html, etree
from markdownify import MarkdownConverter
from markdown import Markdown
from markdown.extensions.toc import slugify_unicode
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

ROOT = Path(__file__).resolve().parents[1]
FORMATTER = HtmlFormatter(cssclass="highlight", style="friendly")
LANGUAGES = {".json": "json", ".toml": "toml", ".yaml": "yaml", ".yml": "yaml",
             ".py": "python", ".sh": "bash", ".js": "javascript", ".html": "html",
             ".css": "css", ".txt": "text"}


def render_markdown(source: str, *, generated=False):
    renderer = Markdown(
        extensions=["meta", "tables", "fenced_code", "codehilite", "toc", "sane_lists", "md_in_html"],
        extension_configs={
            "codehilite": {"css_class": "highlight", "guess_lang": False},
            "toc": {"slugify": lambda value, separator: "file-heading-" + slugify_unicode(value, separator)},
        },
    )
    # Only generated READMEs use our own disclosure blocks and explicit anchors.
    if not generated:
        renderer.preprocessors.deregister("html_block")
        renderer.inlinePatterns.deregister("html")
    body = html.fragment_fromstring(renderer.convert(source), create_parent="div")
    if generated:
        anchors = {}
        for element in body.xpath('.//*[@id]'):
            identifier = element.get("id")
            if not identifier.startswith("file-heading-"):
                anchors[identifier] = "file-heading-" + identifier
                element.set("id", anchors[identifier])
        for link in body.xpath('.//a[@href]'):
            target = link.get("href")
            if target.startswith("#") and target[1:] in anchors:
                link.set("href", "#" + anchors[target[1:]])
    if renderer.Meta:
        metadata = html.Element("details", {"class": "file-frontmatter"})
        summary = html.Element("summary")
        etree.SubElement(summary, "span", lang="zh-CN").text = "元数据"
        etree.SubElement(summary, "span", lang="en").text = "Metadata"
        metadata.append(summary)
        fields = html.Element("dl")
        for key, values in renderer.Meta.items():
            term, value = html.Element("dt"), html.Element("dd")
            term.text, value.text = key, "\n".join(values)
            fields.extend([term, value])
        metadata.append(fields)
        body.insert(0, metadata)
    for image in body.xpath(".//img"):
        link = html.Element("span") if image.getparent().tag == "a" else html.Element("a", href=image.get("src", ""))
        link.text = image.get("alt") or image.get("src") or "Image / 图片"
        link.tail = image.tail
        image.getparent().replace(image, link)
    for link in body.xpath(".//a[@href]"):
        if urlsplit(link.get("href")).scheme.lower() in {"javascript", "data", "vbscript"}:
            del link.attrib["href"]
    headings = []
    for heading in body.xpath(".//h1 | .//h2 | .//h3 | .//h4 | .//h5 | .//h6"):
        identifier = heading.get("id")
        headings.append({"id": identifier, "anchor": identifier.removeprefix("file-heading-"),
                         "text": heading.text_content(), "level": int(heading.tag[1])})
    return html.tostring(body, encoding="unicode"), headings


def attachments(manifest):
    paths = [ROOT / name for name in ("README.md", "README.zh-CN.md", ".gitignore")]
    for folder in ("rules", "configs", "reference", "docs", "tools"):
        paths.extend(path for path in (ROOT / folder).rglob("*")
                     if path.is_file() and path.name != ".DS_Store" and "__pycache__" not in path.parts)
    pinned = {"rules/PRINCIPLES.general.md": 0, "rules/PRINCIPLES.codex.md": 1,
              "README.md": 2, "README.zh-CN.md": 3}
    groups = {"configs": 10, "rules": 11, "reference": 12, "docs": 13, "tools": 14}

    def order(path):
        relative = path.relative_to(ROOT).as_posix()
        return pinned.get(relative, groups.get(relative.split("/")[0], 15)), relative

    translations = {entry["package"]: entry["translation_of"] for entry in manifest if "translation_of" in entry}
    files = []
    for path in sorted(set(paths), key=order):
        relative = path.relative_to(ROOT).as_posix()
        raw = path.read_bytes()
        source = raw.decode("utf-8")
        language = LANGUAGES.get(path.suffix, "text")
        if path.suffix == ".md":
            rendered, headings = render_markdown(source, generated=relative in {"README.md", "README.zh-CN.md"})
            kind, language = "markdown", "markdown"
        else:
            rendered = highlight(source, get_lexer_by_name(language), FORMATTER)
            headings = []
            kind = "text" if language == "text" else "code"
        category = ("document" if path.suffix == ".md" else
                    "script" if path.suffix in {".py", ".sh", ".js", ".html", ".css"} else "config")
        files.append({"path": relative, "name": path.name, "category": category,
                      "group": relative.split("/")[0] if "/" in relative else "root",
                      "type": kind, "language": language, "source": source,
                      "html": rendered, "headings": headings, "size": len(raw),
                      **({"translationOf": translations[relative]} if relative in translations else {})})
    return files


def update_sources():
    """Generate the provenance table from its maintained manifest."""
    manifest = json.loads((ROOT / "docs/manifest.json").read_text())
    translations = {entry["translation_of"] for entry in manifest if "translation_of" in entry}
    start, end = "<!-- SOURCES:START -->", "<!-- SOURCES:END -->"
    editions = (
        ("SOURCES.md", "source_zh", "| 原始来源 | 包内文件 | 状态 |"),
        ("SOURCES.en.md", "source", "| Source | Package file | Status |"),
    )
    for filename, source_key, header in editions:
        path = ROOT / "docs" / filename
        source = path.read_text()
        if source.count(start) != 1 or source.count(end) != 1:
            raise ValueError(f"{filename} must contain one pair of source-table markers")
        before, section = source.split(start)
        _, after = section.split(end)
        rows = [header, "|---|---|---|"]
        for entry in manifest:
            package = entry["package"]
            if not (ROOT / package).is_file():
                raise FileNotFoundError(f"Manifest target does not exist: {package}")
            if source_key == "source" and package in translations:
                continue
            if source_key == "source_zh" and "translation_of" in entry:
                continue
            origin = f"`{entry[source_key]}`"
            if entry.get("source_commit"):
                origin += f" · `{entry['source_commit'][:12]}`"
            rows.append(f"| {origin} | [{package}](../{package}) | {entry['status']} |")
        path.write_text(before + start + "\n" + "\n".join(rows) + "\n" + end + after)



class GuideMarkdownConverter(MarkdownConverter):
    """Keep GitHub disclosure blocks and explicit section anchors."""

    def convert_details(self, el, text, parent_tags):
        return '\n\n<details markdown="1">\n\n' + text.strip() + "\n\n</details>\n\n"

    def convert_summary(self, el, text, parent_tags):
        return "<summary>" + text.strip() + "</summary>\n\n"

    def convert_a(self, el, text, parent_tags):
        if el.get("id") and not el.get("href"):
            return f'<a id="{el["id"]}"></a>\n\n'
        return super().convert_a(el, text, parent_tags)


def update_readmes(template, manifest):
    """Select one locale from the same article used by the website."""
    document = html.document_fromstring(template)
    translations = {entry["translation_of"]: entry["package"] for entry in manifest if "translation_of" in entry}
    originals = {translated: original for original, translated in translations.items()}
    converter = GuideMarkdownConverter(heading_style="ATX", bullets="-", code_language="text", escape_underscores=False, autolinks=False)
    for locale, filename in (("zh-CN", "README.zh-CN.md"), ("en", "README.md")):
        main = deepcopy(document.get_element_by_id("main"))
        for element in main.xpath('.//*[@lang]'):
            if element.get("lang") != locale and element.getparent() is not None:
                element.drop_tree()
        for element in main.xpath('.//span[@lang]'):
            element.drop_tag()
        for element in main.xpath('.//footer | .//button | .//*[@class="eyebrow"] | .//*[@class="section-no"]'):
            element.drop_tree()
        for section in main.xpath('./section'):
            heading = section.find("h2")
            number = list(main.xpath('./section')).index(section) + 1
            heading.text = f"{number:02d} · " + (heading.text or "")
        for element in main.xpath('.//section[@id] | .//header[@id] | .//h2[@id] | .//h3[@id] | .//h4[@id] | .//h5[@id] | .//h6[@id]'):
            anchor = html.Element("a", id=element.get("id"))
            element.addprevious(anchor)
            del element.attrib["id"]
        for link in main.xpath('.//a[@href]'):
            target = link.get("href")
            if target.startswith("#file="):
                link.set("href", "guide.html" + ("?lang=en" if locale == "en" else "") + target)
            path, separator, fragment = target.partition("#")
            mapping = translations if locale == "en" else originals
            if path in mapping:
                link.set("href", mapping[path] + separator + fragment)
        for link in main.xpath('.//a[@href]'):
            if link.get("href") == filename:
                link.drop_tree()
                continue
            if link.getnext() is not None and link.getnext().tag == "a" and not (link.tail or "").strip():
                link.tail = " · " + (link.tail or "")
        # Separate punctuation-ending emphasis from adjacent CJK text for CommonMark.
        for emphasis in main.xpath('.//strong | .//em'):
            text, tail = emphasis.text_content().rstrip(), emphasis.tail
            if text and tail and category(text[-1]).startswith("P") and not tail[0].isspace() and not category(tail[0]).startswith("P"):
                emphasis.tail = " " + tail
        content = converter.convert(html.tostring(main, encoding="unicode")).strip()
        header = repository_header(document, locale, translations)
        notes = repository_notes(locale)
        (ROOT / filename).write_text("<!-- Generated by tools/build-guide.py; edit tools/guide.template.html and source rules. -->\n\n" + header + "\n\n" + content + '\n\n<a id="repository-maintenance"></a>\n\n' + notes + "\n")


def repository_header(document, locale, translations):
    chinese = locale == "zh-CN"
    updated = date.today()
    language_link = "[English](README.md)" if chinese else "[中文](README.zh-CN.md)"
    title = "AI Harness Kit（中文）" if chinese else "AI Harness Kit (English)"
    online = "https://liminge.space/" + ("cn/" if chinese else "") + "ai-harness-kit"
    offline = "guide.html" + ("" if chinese else "?lang=en")
    if chinese:
        reading = f"> 语言：{language_link}\n>\n> 完整规范位于 `rules/`，工具配置位于 `configs/`，扩展参考资料位于 `reference/`。\n>\n> 阅读：[线上阅读版]({online}) · [离线阅读版]({offline})（下载后用浏览器打开）。"
        toc_title, author, edition, update = "目录", "作者", "版本", "更新日期"
    else:
        reading = f"> Language: {language_link}\n>\n> Complete principles live in `rules/`, tool configuration in `configs/`, and supporting references in `reference/`.\n>\n> Read: [Online edition]({online}) · [Offline edition]({offline}) (download and open in a browser)."
        toc_title, author, edition, update = "Table of Contents", "Author", "Edition", "Updated"
    sections = {section.get("id") for section in document.xpath('//main/section[@id]')}
    entries = []
    for link in document.xpath('//nav/a[@href]'):
        target = link.get("href")
        if target.removeprefix("#") not in sections and "data-file-shortcut" not in link.attrib:
            continue
        number = link.find('span[@class="navnum"]').text_content()
        label = link.find(f'span[@lang="{locale}"]').text_content()
        if not chinese:
            target = translations.get(target, target)
        entries.append(f"- [{number} · {label}]({target})")
    badges = f"[![Edition 2026.10](https://img.shields.io/badge/Edition-2026.10-0a84ff)](#top)\n[![Updated {updated:%Y.%m}](https://img.shields.io/badge/Updated-{updated:%Y.%m}-34c759)](#repository-maintenance)"
    metadata = f"| {author} | [Limin Ge](https://www.linkedin.com/in/limin-ge-573b4b28a/) |\n| --- | --- |\n| {edition} | 2026.10 |\n| {update} | {updated.isoformat()} |"
    return f"# {title}\n\n{reading}\n\n{badges}\n\n## {toc_title}\n\n" + "\n".join(entries) + "\n\n" + metadata


def repository_notes(locale):
    if locale == "zh-CN":
        return """## 仓库使用与维护

仓库：[Ge-limin/ai-harness-kit](https://github.com/Ge-limin/ai-harness-kit)。当前为私有仓库审阅版，使用本机已授权的 GitHub 身份访问。将仓库链接、克隆目录或 `guide.html` 交给 Agent，按第 08 章完成接入和真实任务验证；配置中的凭据与安装路径需要按目标环境填写。

下载 [guide.html](guide.html) 后在浏览器打开，即可离线阅读、搜索、复制与下载随包文件；GitHub 文件页面显示 HTML 源码。公司资料通过 [来源索引](docs/SOURCES.md) 访问，需要相应仓库权限。插件来源、版本与许可见 [DEPENDENCIES.json](docs/DEPENDENCIES.json)，运行依赖见 [DEPENDENCIES.md](docs/DEPENDENCIES.md)，来源与拷贝验证见 [validation.md](docs/validation.md)。

正文九章维护于 `tools/guide.template.html`。目录 10 [General · 个人工作规范](rules/PRINCIPLES.general.md) 和 11 [GPT · 模型行为纠偏规范](rules/PRINCIPLES.codex.md) 直接打开文件阅读器，规范全文维护于 `rules/` 中的中英文文件。README 与 `guide.html` 都由同一条命令生成，禁止手工双写：

```sh
python3 -m pip install -r tools/requirements.txt
python3 tools/build-guide.py
```

GitHub 默认展示英文 `README.md`，中文入口为 `README.zh-CN.md`；子目录保留各自的中英文文件命名。

来源记录和英文对应关系维护在 `docs/manifest.json`，构建时同步生成两种语言的来源表。英文译文标记为 `translated`，通过 `translation_of` 指向中文源文件；离线附件中的对应字段为 `translationOf`。插件元数据维护在 `docs/DEPENDENCIES.json`。

生成器先生成 README，再嵌入全部随包文件，保留复制与下载所用原文。只有单个 HTML 时，可用标准 HTML/JSON 工具提取 `script#guide-files` 中的 `files`，按每项 `path`、`source` 保存到独立目录后接入。"""
    return """## Repository use and maintenance

Repository: [Ge-limin/ai-harness-kit](https://github.com/Ge-limin/ai-harness-kit). This is a private repository review edition; access it through a locally authorized GitHub identity. Give your agent the repository URL, a local clone, or `guide.html`, then follow chapter 08 for setup and verification through a real task. Supply credentials and installation paths for the target environment.

Download [guide.html](guide.html?lang=en) and open it in a browser to read, search, copy, and download bundled files offline. GitHub's file page displays HTML source. Company materials are linked in the [source index](docs/SOURCES.en.md) and require repository access. See [DEPENDENCIES.json](docs/DEPENDENCIES.json) for plugin sources, versions and licenses, [DEPENDENCIES.en.md](docs/DEPENDENCIES.en.md) for runtime requirements, and [validation.en.md](docs/validation.en.md) for provenance and copy verification.

Maintain the nine article chapters in `tools/guide.template.html`. Contents entries 10 [General · Personal working principles](rules/PRINCIPLES.general.en.md) and 11 [GPT · Model behavior guidelines](rules/PRINCIPLES.codex.en.md) open the file reader directly; maintain the complete principles in the Chinese and English files under `rules/`. Generate both READMEs and `guide.html` together; do not edit the outputs manually:

```sh
python3 -m pip install -r tools/requirements.txt
python3 tools/build-guide.py
```

GitHub displays the English `README.md` by default; the Chinese edition is `README.zh-CN.md`. Subdirectories retain their existing bilingual filenames.

Maintain provenance and language pairs in `docs/manifest.json`; the build updates both source tables. English translations have status `translated` and a `translation_of` field pointing to their Chinese source; the embedded attachment field is `translationOf`. Maintain plugin metadata in `docs/DEPENDENCIES.json`.

The builder generates the READMEs before embedding every bundled file, preserving the full source for copy and download. If only the HTML is available, use standard HTML/JSON tools to extract `files` from `script#guide-files`, saving each `path` and `source` into a separate directory before setup."""

def build():
    manifest = json.loads((ROOT / "docs/manifest.json").read_text())
    template = (ROOT / "tools/guide.template.html").read_text()
    update_readmes(template, manifest)
    update_sources()
    data = {"files": attachments(manifest), "builtAt": date.today().isoformat()}
    encoded = (json.dumps(data, ensure_ascii=False, separators=(",", ":"))
               .replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))
    replacements = {
        "<!-- SYNTAX_CSS -->": FORMATTER.get_style_defs(".highlight"),
        "<!-- EMBEDDED_FILES -->": '<script id="guide-files" type="application/json">' + encoded + '</script>',
    }
    for marker, value in replacements.items():
        if template.count(marker) != 1:
            raise ValueError(f"Expected exactly one template marker: {marker}")
        template = template.replace(marker, value)
    template = template.replace("<!doctype html>", "<!doctype html>\n<!-- Generated from tools/guide.template.html by tools/build-guide.py. -->", 1)
    destination = ROOT / "guide.html"
    destination.write_text(template)
    print(f"Built {destination.name}: {len(data['files'])} embedded files, {destination.stat().st_size:,} bytes")


if __name__ == "__main__":
    build()
