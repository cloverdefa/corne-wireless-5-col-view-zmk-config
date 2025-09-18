import subprocess
from pathlib import Path


def main():
    base_dir = Path(".")
    yaml_file = base_dir / "corne_keymap.yaml"
    svg_file = base_dir / "IMG/corne.svg"
    svg_file.parent.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        "keymap parse -c 10 -z ./config/corne.keymap > corne_keymap.yaml",
        shell=True,
        check=True,
    )
    subprocess.run(
        "keymap draw corne_keymap.yaml > IMG/corne.svg", shell=True, check=True
    )
    print(f"✅ 已生成 SVG: {svg_file}")


if __name__ == "__main__":
    main()
