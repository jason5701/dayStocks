import telebot
import os

TELEGRAM_TOKEN=os.environ['TELEGRAM_TOKEN']
CHAT_ID=os.environ['CHAT_ID']

def telegram(body):
  bot = telebot.TeleBot(token=TELEGRAM_TOKEN)
  bot.send_message(chat_id=CHAT_ID, text=body, parse_mode='Markdown')

  print('send telegram msg')