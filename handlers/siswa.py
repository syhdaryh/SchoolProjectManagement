from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def login_siswa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("Gunakan: /login_siswa <room_key>")
        return
    
    room_key = args[0]
    user_id = update.effective_user.id
    # TODO: Cek room_key valid, simpan ke database
    await update.message.reply_text(f"Login sebagai siswa berhasil di room: {room_key}")

siswa_login_handler = CommandHandler("login_siswa", login_siswa)
