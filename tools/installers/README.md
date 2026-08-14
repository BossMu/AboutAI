# 安装包清单

存放需要随资料包带走的安装包（dmg / pkg / exe 等）。

约定：
- 文件名建议带版本号，如 `drawio-26.0.10.dmg`。
- 同类/同项目安装包放子文件夹，如 `next-ai/`。
- 二进制文件不入 git（见 `.gitignore`），拷走请用 `python3 scripts/sync.py --zip` 打包。
- 每个安装包在下面登记一行：名称 / 版本 / 来源 / 用途。

| 名称 | 版本 | 来源 | 用途 | 位置 | SHA256 |
| --- | --- | --- | --- | --- | --- |
| Next AI Draw.io（macOS + Windows） | 0.4.16 | [GitHub Releases](https://github.com/DayuanJiang/next-ai-draw-io/releases) | AI 增强的 draw.io 桌面绘图 | `installers/next-ai/` | dmg `c829735a…`；exe `f12a048f…` |
