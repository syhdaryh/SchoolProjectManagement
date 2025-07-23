import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder

from handlers.start import start_handler
from handlers.guru import guru_login_handler
from handlers.siswa import siswa_login_handler

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(BOT_TOKEN).build()

# Register command handlers
app.add_handler(start_handler)
app.add_handler(guru_login_handler)
app.add_handler(siswa_login_handler)

if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()
