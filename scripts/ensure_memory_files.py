#!/usr/bin/env python3
"""Ensure project-scoped memory Markdown files exist at a project root."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


DECISIONS = "项目重大决定.md"
BUGS = "bug修复记忆.md"


def default_decisions() -> str:
    today = date.today().isoformat()
    return f"""# 项目重大决定

用于记录当前项目开发中的重大决定，例如全局框架、整体项目形态、原始意图、UI 风格、功能边界、架构选择、编码方法和需要长期遵守的约束。

## {today}

- Decision: 初始化当前项目的重大决定记忆文件。
  Context: 后续开发前应先读取本文件，避免对话压缩后偏离当前项目的原始意图和既有决定。
  Impact: 新功能、框架、UI 风格、架构、长期约束和用户新想法应追加记录在这里。
"""


def default_bugs() -> str:
    today = date.today().isoformat()
    return f"""# bug修复记忆

用于记录当前项目开发中遇到的错误、bug、误解、调试结论、修复方式和未来应避免重复的问题。

## {today}

- Problem: 初始化当前项目的 bug 修复记忆文件。
  Cause: 对话压缩、长期开发或误解用户意图时，可能导致历史错误和修复经验丢失。
  Fix: 在当前项目根目录维护本文件。
  Prevention: 每次修复 bug、纠正误解或发现错误假设后，追加记录问题、原因、修复方式和预防规则。
"""


def ensure_file(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create project memory files if they do not already exist."
    )
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root where 项目重大决定.md and bug修复记忆.md should live.",
    )
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    created = []
    if ensure_file(root / DECISIONS, default_decisions()):
        created.append(DECISIONS)
    if ensure_file(root / BUGS, default_bugs()):
        created.append(BUGS)

    if created:
        print("Created: " + ", ".join(created))
    else:
        print("Memory files already exist.")
    print(str(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
