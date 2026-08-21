---
name: 防记忆丢失skill
description: 维护项目级记忆以防止对话压缩后上下文丢失。在开发项目时、写或改代码前、长对话被总结/压缩后、创建或打开项目时、用户描述功能、UI 风格、产品方向、框架、架构、编码方式、约束、新想法、bug、调试结果、误解或请求修复时使用。确保每个项目根目录有 `项目重大决定.md`（持久决定）和 `bug修复记忆.md`（bug、错误、误解、修复与预防笔记）两个记忆文件。
---

# 防止记忆缺失

## Core Rule

Treat memory as project-scoped. Each project root owns its own two Markdown files:

- `项目重大决定.md`
- `bug修复记忆.md`

Before writing or modifying project code, identify the active project root, ensure both files exist there, read both files, and compare the current request with the recorded project intent.

If there is no relevant record, proceed according to the user's current wishes.

## Project Root Selection

Choose the root that represents the user's active project, not the skill installation directory and not a previously used project.

Prefer, in order:

1. The workspace root supplied by the environment.
2. The directory the user explicitly names as the project folder.
3. The nearest ancestor containing markers such as `.git`, `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pnpm-workspace.yaml`, or similar.
4. The current working directory, when no stronger marker exists.

When the user switches projects, repeat root detection and use that project's own files. Do not copy, merge, or infer memory from another project unless the user explicitly asks.

## Quick Start

Run the helper from any directory when possible:

```bash
python <本skill目录>/scripts/ensure_memory_files.py --project-root <project-root>
```

本 skill 的辅助脚本位于 skill 目录下的 `scripts/ensure_memory_files.py`（绝对路径通常为 `~/.workbuddy/skills/防记忆丢失skill/scripts/ensure_memory_files.py`）。

If Python is unavailable, create the two Markdown files manually in the selected project root using the exact filenames above.

## Memory Files

### `项目重大决定.md`

Use this file for durable project direction, including:

- Global framework, stack, architecture, routing, state management, storage, deployment, and tooling choices.
- Overall project shape, original intention, target users, workflow, data model, feature boundaries, and non-goals.
- UI style, layout principles, visual language, interaction patterns, and product direction.
- User-described new ideas, feature requirements, implementation approaches, constraints, and preferences.
- Any decision that future coding should not accidentally contradict after context compression.

Append concise dated entries. Preserve old entries.

### `bug修复记忆.md`

Use this file for development mistakes and fixes, including:

- Errors encountered during development.
- Bugs caused by misunderstanding the user's intent or the project behavior.
- Fixes requested after an incorrect, incomplete, or off-direction change.
- Debugging conclusions, root causes, and prevention notes.
- Past errors discovered later.

Append an entry whenever modifying code to fix a problem or after realizing a prior assumption was wrong.

## Required Workflow

1. Identify the current project root.
2. Ensure `项目重大决定.md` and `bug修复记忆.md` exist in that root.
3. Read both files before planning or writing code.
4. Use the records to avoid deviating from the user's original intention.
5. If the current request conflicts with existing memory, mention the conflict briefly and follow the user's newest explicit instruction.
6. Implement the requested work.
7. After changes, append memory entries when the work creates, changes, clarifies, or corrects durable project knowledge.

## Automatic Recording Triggers

Record a major decision in `项目重大决定.md` when any of these happen:

- The user describes a new feature or what it should look like.
- The user decides or changes the overall UI style, page structure, workflow, or product direction.
- A framework, library, architecture, storage approach, API pattern, or build/deployment method is chosen or changed.
- The user gives a new idea, constraint, coding approach, naming convention, or preference that should guide future development.
- A change affects multiple files, future extensibility, or the original intention of the project.

Record a bug lesson in `bug修复记忆.md` when any of these happen:

- A bug is fixed.
- The user says a previous change was wrong, misunderstood, incomplete, or deviated from intent.
- Debugging reveals a root cause that could recur.
- A test failure, runtime error, broken UI, missing state, data mismatch, or environment issue is resolved.
- An assumption was made that should not be repeated.

## Entry Format

Use short dated entries. Keep the files easy to skim.

For `项目重大决定.md`:

```markdown
## YYYY-MM-DD

- Decision: ...
  Context: ...
  Impact: ...
```

For `bug修复记忆.md`:

```markdown
## YYYY-MM-DD

- Problem: ...
  Cause: ...
  Fix: ...
  Prevention: ...
```

## Behavior Notes

- Do not overwrite old memory. Append new entries.
- Do not record trivial implementation details unless they affect future decisions.
- Keep entries factual and concise.
- Treat these files as the user's project memory, not as generic logs.
- On conversation compression, continuation, or resumed work, read the active project's two memory files before coding.
