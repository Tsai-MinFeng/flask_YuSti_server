# 我的專案

後端的API flowchart！

![API flowchart](API_flow_chart.jpg)

## 執行專案

要執行這個專案，請遵循以下步驟：

1. 克隆這個存儲庫到你的本地端。
2. 使用編譯器開啟專案。
3. 在終端機執行 `python init.py`。
4. 開啟執行後產生的連結 `http://127.0.0.1:3000/`。

接著會看到 `upload historyData` 和 `upload PPG` 兩個連結，以下分別介紹：

## upload PPG
上傳功能
1. 在patient id欄位輸入使用者編號，e.g.：5
2. 在PPG欄位輸入一筆陣列資料，e.g.：1, 2, 3, 4, 5, 6, 7, 8, 9, 10
3. 按下 `upload` 上傳資料

刪除功能
1. 在patient id欄位輸入欲刪除資料的使用者編號，e.g.：5
2. 按下 `delete` 後會刪除最新一筆資料

## upload historyData
上傳功能
1. 在 `patient id`、`total time`、`cycle time`、`stimulation time` 欄位分別輸入任意資料
2. 按下 `upload` 上傳資料
