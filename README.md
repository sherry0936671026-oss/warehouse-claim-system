# 倉庫異常帳務追蹤系統
### Warehouse Claim Management System

> 「不是技術練習，是真實痛點的解法。」

---

## 這個系統解決什麼問題？

在電商倉庫的跨倉轉運作業中，當貨物發生短少，帳務會掉入 WMS 的問題區（PRB）。

**現有系統的缺陷：**
- WMS 的轉帳動作只記錄「商品＋數量移動」，沒有事件追蹤
- A 倉把問題帳轉給 B 倉，B 倉只看到一筆來路不明的帳，不知道這是哪天哪筆異常
- 跨倉對帳靠 Google 表單 ＋ Email，沒有狀態追蹤，沒有結案機制
- 同一事件可能被兩個倉庫各自建立，造成帳務混亂

**這個系統的解法：**
- 每筆 PRB 異常都有唯一事件 ID（`EVT-YYYYMMDD-XXX`）
- 轉帳動作綁定事件，不再是單純數量移動
- 對方倉庫收到 Claim 後可以操作：**異議 / 補貨結案 / 轉帳結案**
- 一個事件只能有一筆結案紀錄，避免重複帳務
- 所有操作都有 Log 紀錄，主管可完整追溯

---

## 功能展示

### Dashboard
- 待確認 / 收到的 / 已結案 / 異議中 統計
- 我發出的 Claim 列表
- 收到的 Claim（需處理）

### Claim 詳細頁
- AI 自動摘要（分析異常原因 + 建議行動）
- 完整事件 Log
- 補貨結案（填車號）/ 轉帳結案（填庫存ID）/ 異議

### 建立 Claim
- 出發倉 / 接收倉 / PRB 代碼 / 責任歸屬
- 7天內重複警示（避免同一事件被建立兩次）

### 主管 KPI 頁面
- 各倉異常次數、結案率統計
- 異議中的 Claim 列表供主管審核

---

## 技術架構

```
Frontend          Backend           AI
React (Vite)  →  FastAPI       →  Groq API
                 SQLite            llama-3.3-70b
                 SQLModel
```

**部署：**
- Frontend：Netlify
- Backend：Railway

---

## 為什麼我能做出這個？

我在酷澎擔任倉庫主管期間，親身經歷這個問題：

跨倉轉倉發生短少時，我們把問題帳（1-2）轉回給對方倉庫，但因為系統沒有事件 ID 的概念，對方收到的只是一筆謎之轉帳。PRB 問題區裡有多筆相同商品、相同數量的帳，根本無法確認轉的是哪一筆。

現行作法是靠 **Google 表單 ＋ Email**，效率極低、無法追蹤、無法結案。

這個系統是我對這個問題的解法。

---

## 本地啟動

```bash
# Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # 填入 GROQ_API_KEY
python3 seed.py       # 建立假資料
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

---

## 作者

**劉又瑄 Sherry Liu**  
倉庫主管 → Supply Chain AI Engineer  
熟悉電商倉儲實際作業，同時具備 AI 工具開發能力。

[LinkedIn](#) | [GitHub](https://github.com/sherry0936671026-oss)
