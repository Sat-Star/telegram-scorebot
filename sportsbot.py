import logging
import subprocess
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import livescores

scory = livescores.get_scores()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Welcome to Sportstar\nEnter /score to get the latest cricket scores")

async def score(update: Update, context: ContextTypes.DEFAULT_TYPE):
    script_path = "livescores.py"
    subprocess.call(["python", script_path])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=scory)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('API')).build()
    #enter your API key here instead of `os.getenv('API')`
    
    start_handler = CommandHandler('start', start)
    score_handler = CommandHandler('score', score)

    application.add_handler(start_handler)
    application.add_handler(score_handler)
    application.run_polling()
