# 工具包总览

本目录是 AboutAI 的工具包本体。已收录工具按**作用分类**（编码 / 图表 / 炒股 / 求职 / 规划 / 视频 / 自动化）分表维护，每行一个工具，标注**类型**（skill / plugin / mcp / 安装包）、**来源**与**功能**，看一眼就知道有什么、能干什么。

> 提示：`tools/INDEX.md` 是 `sync.py` 自动生成的机械索引；本文件是人工维护的总览，两者互补。目录结构见 [Dir.md](../Dir.md)。

## 编码

| 名称 | 类型 | 来源 | 功能 | 备注 | 原理 |
| --- | --- | --- | --- | --- | --- |
| node_repl | mcp | 系统自带（Codex 客户端） | Node.js REPL 执行能力，配合浏览器/桌面控制 | 启用 |  |

## 图表

| 名称 | 类型 | 来源 | 功能 | 备注 | 原理 |
| --- | --- | --- | --- | --- | --- |
| diagram-design | plugin | GitHub（[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)） | 打包 Agent Skill（27 种编辑级图表） | 2.3.5；双端已装；支持 draw.io/Mermaid 导入重绘、品牌化配色；内容包快照 `tools/plugins/diagram-design/` | 说明书+模板库：模型按 SKILL.md 规则选型并手写自包含 HTML/SVG；导入 draw.io/Mermaid 时脚本纯文本解析源文件再按品牌风格重绘；无后台服务 |
| drawio（Next AI Draw.io） | mcp | GitHub / npm（[DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io)） | AI 生成/编辑 draw.io 图表，实时浏览器预览 | 已启用；`npx @next-ai-drawio/mcp-server@latest` | MCP server：按需拉起 stdio 进程，模型调用 create/get/edit 工具改 `.drawio` 源文件，内置 HTTP 实时预览；进程结束后可能残留，需手动清理 |
| Next AI Draw.io（桌面客户端） | 安装包 | GitHub（[DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io/releases)） | AI 增强的 draw.io 桌面绘图（macOS + Windows） | 0.4.16；已收录；位置 `installers/next-ai/`；dmg `c829735a…`、exe `f12a048f…` |  |

## 炒股

| 名称 | 类型 | 来源 | 功能 | 备注 | 原理 |
| --- | --- | --- | --- | --- | --- |
| StockWin | skill | 自己创建 | A 股专业分析：智能选股、持仓深度分析、卖出/止盈止损策略（资金面优先） | 已装 |  |

## 求职

| 名称 | 类型 | 来源 | 功能 | 备注 | 原理 |
| --- | --- | --- | --- | --- | --- |
| offer | skill | 自己创建 | 求职助手：岗位搜索与评估、投递追踪、简历与岗位分析 | 已装 |  |

## 规划

| 名称 | 类型 | 来源 | 功能 | 备注 | 原理 |
| --- | --- | --- | --- | --- | --- |
| grill-me / grilling | skill | GitHub（[mattpocock/skills](https://github.com/mattpocock/skills)） | 追问式访谈打磨方案：grill-me 是入口，grilling 是具体会话流程（按设计树分轮拷问） | 已装；同源同流程 |  |

## 自动化

| 名称 | 类型 | 来源 | 功能 | 备注 | 原理 |
| --- | --- | --- | --- | --- | --- |
| computer-use | mcp | 系统自带（Codex 客户端） | 通过 Computer Use 控制 macOS 桌面应用 | 未启用（enabled=false） |  |

## 视频

| 名称 | 类型 | 来源 | 功能 | 备注 | 原理 |
| --- | --- | --- | --- | --- | --- |
| video-editing-skill | skill | GitHub（[6missedcalls/video-editing-skill](https://github.com/6missedcalls/video-editing-skill)） | 轻量剪辑：裁剪、去静音、烧字幕（3 风格）、文字叠加、变速，可链式流水线 | 未安装，信息登记；纯 FFmpeg+Bash+本地 Whisper，零云 API | Bash 脚本封装 FFmpeg 滤镜（silencedetect/drawtext/ass）+ Whisper 转写 SRT 再烧录 |
| cutcraft | skill | GitHub（[chang416/cutcraft](https://github.com/chang416/cutcraft)） | 完整剪辑工作流：素材盘点→创意确认→精剪→调色/转场/配乐→字幕→质检出片，交付单一成品 | 未安装，信息登记；Python 3.10+ / FFmpeg / uv；转写可选本地 Whisper 或 ElevenLabs | 对话式编排 + helper 脚本（EDL/字幕/渲染/QC），从原始素材渲染，支持字级修订 |

## 维护约定

- 本文件人工维护：每个作用分类一个表格，新增/删除工具在对应分类表加/删一行。
- `tools/INDEX.md` 由 `sync.py` 自动生成，只做机械索引；本文件才是给人看的"有什么、能干嘛"。
- 机器生成区（`skills/`、`agents/`、`mcp/`）勿手改；手写心得放 `tools/docs/`。
