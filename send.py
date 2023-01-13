import telebot

TELEGRAM_TOKEN='5636747753:AAH_JLSq1hhLB5kIHQfoVbpVxVeN6menFUU'
CHAT_ID='5697250246'

def telegram(body):
  bot = telebot.TeleBot(token=TELEGRAM_TOKEN)
  bot.send_message(chat_id=CHAT_ID, text=body, parse_mode='Markdown')

  print('send telegram msg')