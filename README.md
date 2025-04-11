# Corne Wireless 5-Column View ZMK Config

這是一個為 Corne 無線鍵盤設計的 ZMK 配置，支援 5 列鍵盤視圖，並包含多種功能層和自定義巨集。

## 目錄結構

- **`config/`**: 包含 ZMK 的主要配置檔案，例如 `corne.keymap`。
- **`behaviors.dtsi`**: 定義自定義行為。
- **`macros/`**: 包含巨集的定義。

## 功能層

### 預設層 (Windows 和 MacOS)
- **Windows Default (WinDef)**: 預設的 Windows 鍵盤佈局。
- **MacOS Default (MacDef)**: 預設的 MacOS 鍵盤佈局。

### 導航層
- **Windows Navigation (WinNav)**: 提供快速導航鍵，例如 Home、End、Page Up/Down。
- **MacOS Navigation (MacNav)**: 提供 MacOS 特定的導航鍵。

### 程式碼層 (Code)
- 包含常用符號和巨集，例如 `&kp EXCL`、`&kp HASH`。

### 功能層 (Func)
- 提供功能鍵 (F1-F12) 和系統快捷鍵。

### 系統層 (SYS)
- 包含藍牙配對、重置和啟動引導模式的快捷鍵。

## 巨集功能

- **`ter_win`**: 開啟 Windows Terminal。
- **`ter_mac`**: 開啟 MacOS Terminal。
- **`max_mac`**: 最大化視窗 (MacOS)。
- **`min_mac`**: 最小化視窗 (MacOS)。
- **`rec_mac`**: 開始螢幕錄影 (MacOS)。

## 安裝與使用

1. 確保已安裝 [ZMK](https://zmk.dev/) 開發環境。
2. 將此專案克隆到本地：
   ```bash
   git clone https://github.com/你的帳號/corne-wireless-5-col-view-zmk-config.git

   ```
3. 編譯並燒錄到你的 Corne 鍵盤：
   ```bash
   west build -p -b corne_left -- -DZMK_CONFIG=$(pwd)/config
   west flash

   ```

## 貢獻
歡迎提交 Issue 或 Pull Request！請遵循以下步驟：

## Fork 此專案。
創建一個新分支：
提交更改並推送到你的分支。
發送 Pull Request。
授權
此專案基於 MIT License 授權。