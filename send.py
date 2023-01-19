import telebot
import os

TELEGRAM_TOKEN='5636747753:AAH_JLSq1hhLB5kIHQfoVbpVxVeN6menFUU'
# TELEGRAM_TOKEN=os.environ['TELEGRAM_TOKEN']
CHAT_ID='5697250246'
# CHAT_ID=os.environ['CHAT_ID']
bot = telebot.TeleBot(token=TELEGRAM_TOKEN)

def telegram(body):
  bot.send_message(chat_id=CHAT_ID, text=body, parse_mode='Markdown')

  print('send telegram msg')

def lastMessage():
  chat = bot.get_updates(offset=-1)

  for update in chat:
    print(update.message)

  print(chat)
