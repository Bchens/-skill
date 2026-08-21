# 防记忆丢失 Skill

> 维护项目级记忆，防止对话压缩后上下文丢失。

## 触发场景

在以下时机触发本 Skill：

- 开发项目、写或改代码之前
- 长对话被总结 / 压缩后
- 创建或打开项目时
- 用户描述功能、UI 风格、产品方向、框架、架构、编码方式、约束、新想法、Bug、调试结果、误解或请求修复时

## 核心机制

每个项目根目录维护两个 Markdown 文件：

| 文件 | 用途 |
| --- | --- |
| `项目重大决定.md` | 记录项目长期方向、技术栈、架构、UI 风格、新想法和长期约束 |
| `bug修复记忆.md` | 记录开发中的错误、误解、根因和预防措施 |

写代码前先识别当前项目根目录，确保两个文件存在并读取，再开始编码。

## 仓库结构

```
Prevent-memory-loss/
├── SKILL.md                       # 完整规则定义
├── README.md                      # 项目说明
├── agents/
│   └── openai.yaml                # Skill 渲染配置
└── scripts/
    └── ensure_memory_files.py     # 自动初始化两个记忆文件的脚本
```

## 快速开始

在任意项目根目录执行：

```bash
python ~/.workbuddy/skills/防记忆丢失skill/scripts/ensure_memory_files.py --project-root .
```

（也可从本仓库 `scripts/ensure_memory_files.py` 调用）

如果 Python 不可用，手动创建上面那张表里的两个 Markdown 文件即可。

## 详细规则

完整的工作流、条目格式、行为准则见 [`SKILL.md`](./SKILL.md)。
