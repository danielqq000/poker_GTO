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

## 專案目錄

```bash
poker_gto_wizard/
│
├── android/                        # Android平台專用設定和程式碼
│
├── ios/                            # iOS平台專用設定和程式碼
│
├── lib/                            # Flutter主要程式碼
│   ├── models/                     # 資料模型 (Spot, Range, EV 計算等)
│   │   ├── spot.dart               # Spot資料模型
│   │   ├── range.dart              # Range資料模型
│   │   └── ev.dart                 # EV分析資料模型
│   │
│   ├── pages/                      # 頁面相關程式碼
│   │   ├── home_page.dart          # 主畫面 (Spot選擇界面)
│   │   ├── practice_page.dart      # 練習頁面 (Spot練習界面)
│   │   ├── range_management_page.dart # 範圍管理界面
│   │   └── analysis_page.dart      # 偏離分析界面
│   │
│   ├── widgets/                    # 共用組件和視覺元件
│   │   ├── spot_tile.dart          # Spot選項顯示組件
│   │   ├── range_visualizer.dart   # 範圍可視化工具
│   │   └── ev_calculator.dart      # EV計算組件
│   │
│   ├── utils/                      # 工具類別和函式
│   │   ├── storage.dart            # 資料存儲功能（localStorage/SQLite）
│   │   ├── gto_calculator.dart     # GTO計算邏輯（簡單實現）
│   │   └── range_helper.dart       # 範圍處理工具
│   │
│   └── main.dart                   # 應用程式入口
│
├── test/                           # 測試資料
│   ├── models/                     # 單元測試資料模型
│   │   ├── spot_test.dart          # Spot資料模型測試
│   │   └── range_test.dart         # Range資料模型測試
│   │
│   ├── widgets/                    # 組件測試資料
│   │   └── range_visualizer_test.dart # 範圍可視化測試
│   │
│   └── main_test.dart              # 主測試檔案
│
├── assets/                         # 靜態資源文件
│   ├── images/                     # 圖片
│   └── json/                       # JSON文件（Spot資料、範圍等）
│
├── pubspec.yaml                    # 專案的配置信息
└── README.md                       # 專案的自述文件
```

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
