# 💹 Telegram Market Tracker Bot

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Telegram Bot](https://img.shields.io/badge/Telegram%20Bot-Active-blue?logo=telegram)](https://t.me/)
[![License](https://img.shields.io/github/license/MC769/MarketTrackerBot)](LICENSE)
[![Stars](https://img.shields.io/github/stars/MC769/MarketTrackerBot?style=social)](https://github.com/MC769/MarketTrackerBot/stargazers)
[![Issues](https://img.shields.io/github/issues/MC769/MarketTrackerBot)](https://github.com/MC769/MarketTrackerBot/issues)
[![Last Commit](https://img.shields.io/github/last-commit/MC769/MarketTrackerBot?color=green)](https://github.com/MC769/MarketTrackerBot/commits/main)

---

## 🧠 Overview

**MarketTrackerBot** is a lightweight Telegram bot that provides **real-time price updates** for any token listed on **MEXC Exchange**.  
Simply send the token symbol (like `BTC`) in chat — and the bot responds with live market data, 24-hour change, and volume, along with quick access to the chart.

---

## ✨ Features

- 💰 **Live Price Data** — Fetches the latest price from [MEXC API](https://mexc.com/)
- 📊 **24H Stats** — Shows price change %, trading volume, and performance since listing
- 🔄 **One-Click Refresh** — Instantly updates market data
- 📈 **Chart Button** — Direct link to the MEXC chart for your token
- 🌐 **Environment Variables Support** — Easy configuration using `.env`
- 🧩 **Clean Codebase** — Structured with async `python-telegram-bot v20+`

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/MC769/MarketTrackerBot.git
cd MarketTrackerBot
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env` File
Create a `.env` file in your root directory with:
```env
BOT_TOKEN=your_telegram_bot_token
SYMBOL=BTC
```

### 5️⃣ Run the Bot
```bash
python main.py
```

---

## 🧩 Example Command

💬 **User:**  
```
BTC
```

🤖 **Bot Response:**
```
💹 BTC/USDT Market Overview

💰 Price: `64000.123456`

🟢 24H Change: `+1.32%`
🔺 Since Listing: `+6399900.00%`
📊 Volume: `123456789.00`

📅 Updated at: `2025-10-23 10:00 UTC`
🧠 Data by MEXC
```

With inline buttons:  
🔹 **📈 View Chart**  
🔹 **🔄 Refresh**

---

## 🧰 Requirements

- Python **3.10+**
- Libraries:
  - `python-telegram-bot`
  - `requests`
  - `python-dotenv`

---

## 📦 Example `requirements.txt`
```txt
python-telegram-bot==20.7
requests==2.31.0
python-dotenv==1.0.1
```

---

## 💡 Customization

You can easily modify:
- `listing_price` → set your token’s initial price  
- `SYMBOL` → default coin symbol (from `.env`)  
- `VIEW_CHART_URL` → link to any exchange or chart  

---

## 🚀 Deployment (Optional)

To run 24/7 on a server (e.g., Ubuntu VPS):

```bash
sudo apt update && sudo apt install -y python3-pip
pip install -r requirements.txt
nohup python3 main.py &
```

---

## 🧑‍💻 Author

**Chiran ([@MC769](https://github.com/MC769))**  
🚀 Building bots and automation tools for Web3, crypto, and beyond.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

⭐ **If you like this project, consider giving it a star!**  
