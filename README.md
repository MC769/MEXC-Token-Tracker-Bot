
```markdown
# 🚀 Telegram Crypto Price Bot (MEXC API)

This project is a lightweight **Telegram bot** that allows users to check real-time cryptocurrency prices, 24-hour change, trading volume, and performance since listing — powered by the **MEXC Exchange API**.

It uses:
✅ Python  
✅ `python-telegram-bot` v20+  
✅ Real-time REST API requests  
✅ Environment variables for secure configuration (`.env` file)

---

## 🧠 Features

✔ Get live crypto price using simple text command (e.g., typing `BTC`)  
✔ Displays:
- ✅ Current Price  
- ✅ 24H Price Change (%) with 📈/📉 emoji  
- ✅ Performance since listing  
- ✅ 24H Trading Volume  
- ✅ Last Updated Time  
✔ Inline buttons for:
- ✅ 📈 View Chart (opens MEXC price page)  
- ✅ 🔄 Refresh data in real-time  
✔ `.env` file support (no hardcoded API keys or token symbols)

---

## 📁 Project Structure

```

📂 CryptoTelegramBot
├── bot.py               # Main bot script
├── .env                 # Environment variables (not uploaded to GitHub)
├── README.md            # Documentation
├── requirements.txt     # Dependencies

```

---

## ⚙️ Environment Setup (.env File)

Create a file named `.env` in your project directory and add:

```

BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
SYMBOL=BTC

````

> 📌 Example: If `SYMBOL=BTC`, then the bot listens to the command `btc` in Telegram.

---

## 🛠 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create `.env` File (Important)

```bash
BOT_TOKEN=your_telegram_bot_token
SYMBOL=BTC
```

### 4️⃣ Run the Bot

```bash
python bot.py
```

---

## 💻 How to Use

| Action                   | What to Do                                |
| ------------------------ | ----------------------------------------- |
| ✅ Get price              | Send the symbol (e.g., `btc`) to your bot |
| 🔄 Refresh stats         | Click the **Refresh** button              |
| 📈 Open full price chart | Click the **View Chart** button           |

---

## 📦 Example Output (in Telegram)

```
💹 BTC/USDT Market Overview

💰 Price: `62439.670000`

🟢 24H Change: `+2.30%`
🔺 Since Listing: `+500000000.00%`
📊 Volume: `123456789.00`

📅 Updated at: `2025-10-23 14:22 UTC`
🧠 _Data by MEXC_
```

---

## 📚 Requirements (requirements.txt Example)

```
python-telegram-bot==20.7
requests
python-dotenv
```

---

## 🧠 Future Improvements

* 🔔 Add price alerts
* 🧾 Add multi-token support (`/btc`, `/eth`, etc.)
* 📊 Interactive inline charts
* 🌐 Add support for other exchanges (Binance, Bybit)

---

## 🤝 Contributing

Pull requests are welcome!

1. Fork the repo
2. Create a branch: `feature/new-feature`
3. Commit & push
4. Open a Pull Request ✅

---

## 📜 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and share.

---

## 🌐 Connect With Me

| Platform    | Link                                                                         |
| ----------- | ---------------------------------------------------------------------------- |
| 💼 LinkedIn | [https://linkedin.com/in/your-profile](https://linkedin.com/in/your-profile) |
| 🐙 GitHub   | [https://github.com/your-username](https://github.com/MC769)         |

---

⭐ *If this project helped you, don't forget to star the repo on GitHub!*

```

Just tell me — I can do it in seconds. 🚀
```
