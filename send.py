import telebot
import os

TELEGRAM_TOKEN=os.environ['TELEGRAM_TOKEN']
CHAT_ID=os.environ['CHAT_ID']
bot = telebot.TeleBot(token=TELEGRAM_TOKEN)

def telegram(body):
  bot.send_message(chat_id=CHAT_ID, text=body, parse_mode='Markdown')
