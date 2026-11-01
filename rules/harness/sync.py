"""Validate and distribute PRINCIPLES documents, merging numbered sections."""

import argparse
import os
import re
import sys
import tempfile
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import cast

import yaml
from markdown_it import MarkdownIt


class SyncError(ValueError):
    pass


@dataclass
class Section:
    title: str
    heading: str
    body: str
    path: Path
    line: int
    children: dict = field(default_factory=dict)

    def fail(self, message):
        raise SyncError(f"{self.path}:{self.line}: {message}")


def parse_document(path, data):
    text = data.decode("utf-8")
    lines = text.splitlines(keepends=True)
    tokens = MarkdownIt("commonmark").parse(text)
    headings = []
    previous_level = 0
    for i, token in enumerate(tokens):
        # Nested blockquotes/lists and fenced code are not document structure.
        if token.type != "heading_open" or token.level != 0:
            continue
        level = int(token.tag[1:])
        span = cast(list[int], token.map)
        line = span[0] + 1
        if level > 4 or level > previous_level + 1:
            raise SyncError(f"{path}:{line}: Invalid heading level H{previous_level} → H{level}")
        previous_level = level
        if level <= 3:
            headings.append((level, tokens[i + 1].content, span))
    if not headings or headings[0][0] != 1:
        raise SyncError(f"{path}:1: Missing H1 document title")
    if any(line.strip() for line in lines[:headings[0][2][0]]):
        raise SyncError(f"{path}:1: Body text precedes H1")

    root = Section("", "", "", path, 1)
    chapter = None
    chapter_number = 0
    last_section = 0
    numbers = {name: i for i, name in enumerate(["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"], 1)}
    for i, (level, title, span) in enumerate(headings):
        end = headings[i + 1][2][0] if i + 1 < len(headings) else len(lines)
        section = Section(title, "".join(lines[span[0]:span[1]]),
                          "".join(lines[span[1]:end]), path, span[0] + 1)
        if level == 1:
            if i != 0:
                section.fail("Duplicate H1 document title")
            root = section
        elif level == 2:
            match = re.fullmatch(r"([一二三四五六七八九十]+)、(.+)", title)
            if not match or match[1] not in numbers or not match[2].strip():
                section.fail("Invalid chapter number or title; H2 must use a Chinese numeral from one to ten, followed by 、 and a title")
            number = numbers[match[1]]
            if number in root.children:
                section.fail(f"Duplicate chapter number {number}")
            if number <= chapter_number:
                section.fail(f"Chapter numbers out of order: {number} follows {chapter_number}")
            chapter_number = number
            last_section = 0
            root.children[number] = chapter = section
        else:
            match = re.fullmatch(r"([1-9][0-9]*)\.([1-9][0-9]*)\s+(.+)", title)
            if not match or not match[3].strip():
                section.fail("Invalid subsection number or title; H3 must use x.y followed by whitespace and a title")
            parent, number = int(match[1]), int(match[2])
            if chapter is None or parent != chapter_number:
                section.fail(f"Subsection {parent}.{number} does not belong to the current parent chapter {chapter_number}")
            if number in chapter.children:
                section.fail(f"Duplicate subsection number {parent}.{number}")
            if number <= last_section:
                section.fail(f"Subsection numbers out of order: {parent}.{number}")
            last_section = number
            chapter.children[number] = section
    return root


def join_parts(parts):
    # Only normalize boundary blank lines; section text stays verbatim.
    return "\n\n".join(part.strip("\r\n") for part in parts if part.strip("\r\n"))


def merge_into(base, extra, *, root=False):
    if not root and base.title != extra.title:
        extra.fail(f"Title mismatch for the same number: {extra.title!r}; baseline {base.path}:{base.line} has {base.title!r}")
    base.body = join_parts([base.body, extra.body])
    for number, section in extra.children.items():
        if number in base.children:
            merge_into(base.children[number], section)
        elif root:
            section.fail(f"Supplementary chapter does not exist in the baseline document: {section.title}")
        else:
            base.children[number] = section


def render(section):
    return join_parts([section.heading, section.body] +
                      [render(section.children[n]) for n in sorted(section.children)])


def resolve_path(value, directory):
    if not isinstance(value, str) or not value.strip():
        raise SyncError("Configured paths must be nonempty strings")
    path = Path(value).expanduser()
    return path if path.is_absolute() else directory / path


def prepare(config_path):
    with config_path.open(encoding="utf-8") as stream:
        config = yaml.safe_load(stream)
    if not isinstance(config, dict) or not isinstance(config.get("targets"), list) or not config["targets"]:
        raise SyncError(f"{config_path}: targets must be a nonempty list")
    prepared = []
    seen = set()
    for target in config["targets"]:
        if not isinstance(target, dict) or not isinstance(target.get("sources"), list) or not target["sources"]:
            raise SyncError(f"{config_path}: Each target must declare a nonempty sources list")
        output = resolve_path(target.get("path"), config_path.parent).resolve()
        if output in seen:
            raise SyncError(f"{config_path}: Duplicate target path {output}")
        seen.add(output)
        sources = [resolve_path(source, config_path.parent) for source in target["sources"]]
        data = [source.read_bytes() for source in sources]
        documents = [parse_document(path, content) for path, content in zip(sources, data, strict=True)]
        if len(documents) == 1:
            content = data[0]
        else:
            base = documents[0]
            for extra in documents[1:]:
                merge_into(base, extra, root=True)
            content = (render(base) + "\n").encode("utf-8")
        prepared.append((output, content))
    return prepared


def atomic_write(path, content, mode=0o600):
    # Stage beside the destination so os.replace remains on the same filesystem.
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(content)
            stream.flush()
            os.fchmod(stream.fileno(), mode)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--targets", type=Path, default=Path(__file__).with_name("targets.yaml"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        # Complete validation and rendering for ALL targets before any filesystem writes.
        prepared = prepare(args.targets.resolve())
        timestamp = datetime.now(timezone.utc).astimezone().strftime("%Y%m%d-%H%M%S-%f")
        for path, content in prepared:
            if args.dry_run:
                print(f"DRY RUN: {path} ({len(content)} bytes), validation passed, no files written")
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            mode = path.stat().st_mode & 0o777 if path.exists() else 0o600
            backup = None
            if path.exists():
                backup = path.with_name(f"{path.name}.bak-{timestamp}")
                atomic_write(backup, path.read_bytes(), mode)
            atomic_write(path, content, mode)
            # Retire old backups only after the target replacement succeeded.
            if backup is not None:
                for old in path.parent.iterdir():
                    if old.name.startswith(f"{path.name}.bak-") and old != backup and old.is_file():
                        old.unlink()
            print(f"SYNCED: {path}" + (f" (backup: {backup})" if backup else ""))
    except (SyncError, OSError, UnicodeError, yaml.YAMLError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
