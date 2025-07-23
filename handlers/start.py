from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Selamat datang! Gunakan /login_guru atau /login_siswa <room_key>.")

start_handler = CommandHandler("start", start)
