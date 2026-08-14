# 工具包总览

本目录是 AboutAI 的工具包本体。这份文档按分类列出已收录的工具：**来源**（GitHub 安装 / 自己创建 / 系统自带）与**简要功能**，看一眼就知道有什么、能干什么。

> 提示：`tools/INDEX.md` 是 `sync.py` 自动生成的机械索引；本文件是人工维护的总览，两者互补。

## 分类一览

| 分类 | 目录 | 状态 |
| --- | --- | --- |
| Skills | `tools/skills/` | 已收录 4 个 |
| Agents | `tools/agents/` | 空（预留） |
| MCP | `tools/mcp/` | 已收录 2 个（脱敏配置） |
| Prompts | `tools/prompts/` | 空（待维护） |
| Scripts | `tools/scripts/` | 空（待维护） |
| Configs | `tools/configs/` | 空（待维护） |
| Installers | `tools/installers/` | 已收录 1 个 |
| Docs | `tools/docs/` | 空（待维护） |

## Skills

| 名称 | 来源 | 简要功能 |
| --- | --- | --- |
| StockWin | 自己创建 | A 股专业分析：智能选股、持仓深度分析、卖出/止盈止损策略（资金面优先） |
| offer | 自己创建 | 求职助手：岗位搜索与评估、投递追踪、简历与岗位分析 |
| grill-me / grilling | GitHub（[mattpocock/skills](https://github.com/mattpocock/skills)） | 追问式访谈打磨方案：grill-me 是入口，grilling 是具体会话流程（按设计树分轮拷问） |

## MCP

| 名称 | 来源 | 功能 | 状态 |
| --- | --- | --- | --- |
| node_repl | 系统自带（Codex 客户端） | Node.js REPL 执行能力，配合浏览器/桌面控制 | 启用 |
| computer-use | 系统自带（Codex 客户端） | 通过 Computer Use 控制 macOS 桌面应用 | 未启用（enabled=false） |

## Installers

| 名称 | 版本 | 来源 | 用途 |
| --- | --- | --- | --- |
| Next AI Draw.io | 0.4.16 | GitHub（[DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io/releases)） | AI 增强的 draw.io 桌面绘图（macOS + Windows） |

## 维护约定

- 本文件人工维护：新增/删除工具后，同步更新对应分类表格。
- `tools/INDEX.md` 由 `sync.py` 自动生成，只做机械索引；本文件才是给人看的"有什么、能干嘛"。
- 机器生成区（`skills/`、`agents/`、`mcp/`）勿手改；手写心得放 `tools/docs/`。
