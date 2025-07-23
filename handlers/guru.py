from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def login_guru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    # TODO: Simpan role guru ke database
    await update.message.reply_text(f"Login sebagai guru berhasil. User ID: {user_id}")

guru_login_handler = CommandHandler("login_guru", login_guru)
