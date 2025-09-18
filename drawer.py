import subprocess
from pathlib import Path


def main():
    base_dir = Path(".")
    keymap_file = base_dir / "config/corne.keymap"
    yaml_file = base_dir / "corne_keymap.yaml"
    svg_file = base_dir / "IMG/corne.svg"

    # 確保輸出資料夾存在
    svg_file.parent.mkdir(parents=True, exist_ok=True)

    # parse -> YAML
    parse_cmd = f'keymap parse -c 10 -z "{keymap_file}" > "{yaml_file}"'
    subprocess.run(parse_cmd, shell=True, check=True)

    # draw -> SVG
    draw_cmd = f'keymap draw "{yaml_file}" > "{svg_file}"'
    subprocess.run(draw_cmd, shell=True, check=True)

    # 清理中間 YAML
    if yaml_file.exists():
        yaml_file.unlink()

    print(f"✅ 已生成 SVG: {svg_file} 並已刪除中間 YAML 檔案")


if __name__ == "__main__":
    main()
