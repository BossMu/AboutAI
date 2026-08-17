# vision-assist —— 图片/PDF 识别与 OCR

## 简介

为纯文本模型（如 DeepSeek）补上"眼睛"：用户发图片路径后，先调用**免费的智谱 GLM 视觉 API**（`glm-4.1v-thinking-flash` 优先，`glm-4.6v-flash`、`glm-4v-flash` 兜底）识图；限流或断网时自动降级到**本地 OCR**（Windows 内置 Windows.Media.Ocr，无需安装额外引擎）。

- 来源：[pudy/harness_skills](https://github.com/pudy/harness_skills)（codex/vision-assist）
- 平台：跨平台；Windows 本地 OCR 开箱即用
- 成本：免费（智谱 GLM Flash 系列免费模型）

## 安装位置

- 技能本体：`~/.codex/skills/vision-assist/`
- 同步源：`~/.agents/skills/vision-assist/`（AboutAI `sync.py` 从此导出快照）
- 仓库快照：`tools/skills/vision-assist/`（不含 `config.json`，敏感文件已排除）

## 配置

复制 `config.json.example` 为 `config.json`，填入智谱 API Key：

```json
{
  "api_key": "你的智谱Key",
  "endpoint": "https://open.bigmodel.cn/api/paas/v4/chat/completions",
  "model": "glm-4.1v-thinking-flash",
  "fallback_models": ["glm-4.6v-flash", "glm-4v-flash"],
  "allowed_models": ["deepseek-v4-flash", "deepseek-v4-pro"]
}
```

- Key 申请：https://open.bigmodel.cn → 实名认证 → API Keys 页面创建（免费）
- **Key 只存本地 `~/.codex/skills/vision-assist/config.json`，已加入 `.syncignore`，不会进入 AboutAI 仓库**
- `allowed_models` 控制哪些模型触发本技能（默认 DeepSeek 系列）

## 用法

```bash
# 环境自检（引擎、Key、模型白名单）
python scripts/vision.py --check

# 默认：视觉 API 优先，失败自动降级本地 OCR
python scripts/vision.py --image "<图片路径>"

# 强制本地 OCR（离线/隐私场景）
python scripts/vision.py --image "<图片路径>" --mode ocr

# PDF：先提取文字层，扫描件自动渲染后走 OCR
python scripts/vision.py --image "<PDF路径>"
```

在 Codex 对话里：直接给出图片文件路径并说"识别这张图"，即可自动触发。

## 验证记录（2026-08-17）

Windows 11 + DeepSeek（deepseek-v4-flash）实测通过：

- 本地 OCR：英文准确；中文有少量误差（如"识别"→"识另刂"），适合兜底；
- 智谱 GLM API：中英文均精确识别（"Hello World 12345" / "中文测试：识别图片文字"）。

## 注意

- Windows 桌面版 Codex 对纯文本模型阻断直接贴图，需以文件路径方式传图；
- 免费 API 高峰期可能 429 限流，技能会自动重试并降级，无需人工干预；
- 敏感图片若不想出本机，用 `--mode ocr` 强制本地识别。
