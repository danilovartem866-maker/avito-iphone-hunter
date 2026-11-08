
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

LIMITS = {
    "15 Pro": 40000,
    "15 Pro Max": 45000,
    "16 Pro": 55000,
    "16 Pro Max": 60000,
    "17 Pro": 70000,
    "17 Pro Max": 80000,
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 Avito iPhone Hunter SPB запущен!\n\n"
        "Пока работает тестовый режим.\n"
        "Команда /prices покажет лимиты."
    )

async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "💰 Лимиты цен:\n\n"
    for model, price in LIMITS.items():
        text += f"iPhone {model} — до {price:,} ₽\n".replace(",", " ")
    await update.message.reply_text(text)

async def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN не задан")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prices", prices))
    print("Bot started")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
