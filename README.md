# AboutAI

个人 AI 实用工具包 + 学习成果展馆。

收集我使用 AI 过程中沉淀的 skills、MCP、提示词、脚本与配置，并记录学习笔记与实验成果。本目录以 Markdown 为主，拷走即用，可分享（默认排除个人数据）。

## 快速开始

```bash
# 同步工具包（从本机导出快照 + 脱敏 MCP + 重建索引）
python3 scripts/sync.py

# 同步并打包成 zip
python3 scripts/sync.py --zip

# 在新机器上从资料包恢复
python3 scripts/install.py
```

## 目录结构

见 [Dir.md](Dir.md)；工具包内容总览见 [tools/README.md](tools/README.md)。

## 维护约定

- `tools/skills/`、`tools/agents/` 由 `sync.py` 整目录生成，**不要手改**，会被覆盖。
- `tools/mcp/` 由 `sync.py` 从 `~/.codex/config.toml` 提取并脱敏生成，同样不要手改。
- 手写内容放 `tools/docs/`（工具心得）、`tools/prompts/`、`tools/scripts/`、`tools/configs/`。
- `tools/installers/` 放安装包（dmg/pkg/exe），二进制不入 git，登记见 `tools/installers/README.md`。
- 隐私与排除：`sync.py` 会跳过 `.syncignore` 中列出的路径；MCP 配置中的 key/token/secret 一律替换为 `<redacted>`。公开分享前请自行检查一遍。
- 学习区 `learning/` 是个人笔记区，可自由增删；笔记可用链接指向 `tools/docs/` 中的条目。

- `learning/` 是个人学习区，记录笔记与实验，可自由增删。
