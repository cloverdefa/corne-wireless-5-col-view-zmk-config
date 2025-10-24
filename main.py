#!/usr/bin/env python3
"""
Corne 鍵盤 keymap SVG 生成腳本

功能：
1. 從 Corne 鍵盤的 keymap 檔案（.keymap）解析成 YAML。
2. 使用 YAML 生成對應的鍵盤布局 SVG 圖片。
3. 自動建立必要的輸出資料夾。
4. 生成完成後清理中間 YAML 檔案。

依賴：
- `keymap` CLI 工具，需要在系統 PATH 中。
- Python 3.6+。
"""

import subprocess
from pathlib import Path


def generate_svg(keymap_path: Path, svg_path: Path, yaml_path: Path, columns: int = 10):
    """
    將 Corne keymap 轉換為 SVG。

    參數：
    - keymap_path: 原始 keymap 檔案 (.keymap)
    - svg_path: 輸出 SVG 路徑
    - yaml_path: 中間 YAML 檔案路徑
    - columns: 鍵盤列數 (預設 10)
    """
    # 確保輸出資料夾存在
    svg_path.parent.mkdir(parents=True, exist_ok=True)

    # parse -> YAML
    parse_cmd = f'keymap parse -c {columns} -z "{keymap_path}" > "{yaml_path}"'
    subprocess.run(parse_cmd, shell=True, check=True)

    # draw -> SVG
    draw_cmd = f'keymap draw "{yaml_path}" > "{svg_path}"'
    subprocess.run(draw_cmd, shell=True, check=True)

    # 清理中間 YAML
    if yaml_path.exists():
        yaml_path.unlink()

    print(f"✅ 已生成 SVG: {svg_path} 並已刪除中間 YAML 檔案")


def main():
    base_dir = Path(".")
    keymap_file = base_dir / "config/corne.keymap"
    yaml_file = base_dir / "corne_keymap.yaml"
    svg_file = base_dir / "IMG/corne.svg"

    # 生成 SVG
    generate_svg(keymap_file, svg_file, yaml_file)


if __name__ == "__main__":
    main()
