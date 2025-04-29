# Poker GTO

Poker GTO 是一款幫助撲克玩家提高 GTO（Game Theory Optimal）策略的訓練工具。該工具旨在提供一個簡單且高效的平台，讓玩家能夠根據自定義的手牌範圍進行模擬訓練，並提供基於 GTO 的策略回饋。

## 目標
- 提供 GTO 策略的即時計算與分析。
- 幫助玩家自定義手牌範圍，並根據 GTO 計算結果進行行動選擇。
- 分析玩家的選擇，並提供偏離 GTO 策略的建議。
- 在手機端提供跨平台應用，支持 Android 和 iOS。

## 功能需求
- **Spot 練習**：提供多個 GTO 情境讓使用者選擇行動，並回饋該行動是否符合 GTO 策略。
- **範圍管理**：使用者可以自定義手牌範圍，並將其儲存起來。
- **偏離分析**：分析玩家行動的偏離程度，並給出 EV 損失的建議。
- **範圍可視化**：以熱圖或 2D 網格顯示使用者的範圍。
- **本地儲存**：支持離線使用，並能儲存個人範圍與訓練紀錄。

## 技術棧
- **後端**：Python，使用 CFR 演算法實現 GTO 計算引擎。
- **前端**：Flutter（Dart），提供跨平台的手機應用（Android 和 iOS）。
- **數據儲存**：SQLite，用於儲存用戶範圍與進度。

## 安裝與運行

### 1. 安裝依賴
在後端運行之前，請先安裝所需的 Python 庫：

```bash
pip install -r requirements.txt
```

### 2. 啟動後端服務
啟動後端服務，確保計算引擎可以正確運行：

```bash
python backend/server.py
```

### 3. 安裝 Flutter 依賴
進入 Flutter 專案目錄並安裝必要的依賴：

```bash
flutter pub get
```

### 4. 執行前端應用
啟動 Flutter 應用並在本地設備上測試：

```bash
flutter run
```

## 使用說明
1. 打開應用後，使用者可以設定自己的手牌範圍。
2. 選擇一個 GTO 練習情境，並根據提示選擇對應的行動。
3. 應用將計算並顯示該行動是否符合 GTO 策略。
4. 根據偏離 GTO 的程度，應用會提供相應的建議。

## 開發進度
**4/29/25**: 正式開始

## 貢獻
如果你有任何改進建議或 bug 報告，歡迎提交 [Issues](https://github.com/yourusername/poker-gto-wizard/issues)，並開啟 Pull Request 進行貢獻。

## 授權

本專案使用 [Apache 2.0 License](LICENSE) 開源授權。

```
