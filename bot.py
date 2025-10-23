import os
import logging
import requests
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from telegram.constants import ParseMode
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
SYMBOL = os.getenv("SYMBOL", "")  # Example "BTC"
PAIR = SYMBOL + "USDT"
MEXC_API_URL = f"https://api.mexc.com/api/v3/ticker/24hr?symbol={PAIR}"
VIEW_CHART_URL = f"https://www.mexc.com/price/{SYMBOL}"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_market_data():
    try:
        resp = requests.get(MEXC_API_URL, timeout=10)
        resp.raise_for_status()
        j = resp.json()

        price = float(j["lastPrice"])
        change_pct = float(j["priceChangePercent"])
        volume = float(j["quoteVolume"])

        listing_price = 0.001  # Change to your token listing price
        since_listing = ((price - listing_price) / listing_price) * 100

        updated_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

        return {
            "price": price,
            "change_pct": change_pct,
            "since_listing": since_listing,
            "volume": volume,
            "updated_at": updated_at,
        }
    except Exception as e:
        logger.error(f"Error fetching market data: {e}")
        return None

def format_message(data):
    price_str = f"`{data['price']:.6f}`"
    change_str = f"`{data['change_pct']:.2f}%`"
    since_str = f"`{data['since_listing']:.2f}%`"
    volume_str = f"`{data['volume']:.2f}`"
    updated_str = f"`{data['updated_at']}`"
    sign_icon = "🟢" if data["change_pct"] >= 0 else "🔴"

    return (
        f"💹 {SYMBOL}/USDT Market Overview\n\n"
        f"💰 Price: {price_str}\n\n"
        f"{sign_icon} 24H Change: {change_str}\n"
        f"🔺 Since Listing: {since_str}\n"
        f"📊 Volume: {volume_str}\n\n"
        f"📅 Updated at: {updated_str}\n"
        f"🧠 _Data by MEXC_"
    )

def build_keyboard():
    return InlineKeyboardMarkup([[ 
        InlineKeyboardButton("📈 View Chart", url=VIEW_CHART_URL),
        InlineKeyboardButton("🔄 Refresh", callback_data="refresh")
    ]])

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.strip().lower() == SYMBOL.lower():
        data = fetch_market_data()
        if data:
            await update.message.reply_text(
                format_message(data),
                reply_markup=build_keyboard(),
                parse_mode=ParseMode.MARKDOWN_V2
            )
        else:
            await update.message.reply_text("⚠️ Unable to fetch market data.")

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "refresh":
        data = fetch_market_data()
        if data:
            await query.edit_message_text(
                format_message(data),
                reply_markup=build_keyboard(),
                parse_mode=ParseMode.MARKDOWN_V2
            )

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing! Set it in .env file")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.run_polling()

if __name__ == "__main__":
    main()

