import telebot
from telebot import types

api_key = '5435243295:AAEDsQRyUsBg8Cmyii0NfR5j4RJJXUJ_wv8'
bot = telebot.TeleBot(api_key)

# @bot.message_handler(commands=["start"])
# def start(message):
#   start_message = f"<b>Hello</b>, <i>{message.from_user.first_name}</i>"
#   bot.send_message(message.chat.id, start_message, parse_mode='html')

@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
  item1 = types.KeyboardButton('1')
  item2 = types.KeyboardButton('2')
  item3 = types.KeyboardButton('3')
  item4 = types.KeyboardButton('4')
  item5 = types.KeyboardButton('5')
  

  markup.add(item1, item2, item3, item4, item5)
  start_message = f"<b>Hello</b>, <i>{message.from_user.first_name}</i>"
  bot.send_message(message.chat.id, start_message, reply_markup = markup, parse_mode="html")

@bot.message_handler(content_types=['text'])
def bot_message(message):
  if message.chat.type == 'private':
    if message.text == '1':
      bot.send_message(message.chat.id, '1')
    elif message.text == '2':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('1')
      item2 = types.KeyboardButton('2')
      item3 = types.KeyboardButton('3')
      item4 = types.KeyboardButton('4')
      back = types.KeyboardButton('назад')
      markup.add(item1, item2, item3, item4, back)
      start_message = f"<b>Hello</b>, <i>{message.from_user.first_name}</i>"
    
      bot.send_message(message.chat.id, start_message, reply_markup = markup, parse_mode="html")

    elif message.text == '3':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('1')
      item2 = types.KeyboardButton('2')
      item3 = types.KeyboardButton('3')
      item4 = types.KeyboardButton('4')
      back = types.KeyboardButton('назад')
      markup.add(item1, item2, item3, item4, back)
      start_message = f"<b>Hello</b>, <i>{message.from_user.first_name}</i>"
  
      bot.send_message(message.chat.id, start_message, reply_markup = markup, parse_mode="html")

    elif message.text == '4':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('1')
      item2 = types.KeyboardButton('2')
      item3 = types.KeyboardButton('3')
      item4 = types.KeyboardButton('4')
      back = types.KeyboardButton('назад')
      markup.add(item1, item2, item3, item4, back)
      start_message = "4"
    
      bot.send_message(message.chat.id, start_message, reply_markup = markup, parse_mode="html")

    elif message.text == '5':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('1')
      item2 = types.KeyboardButton('2')
      item3 = types.KeyboardButton('3')
      item4 = types.KeyboardButton('4')
      back = types.KeyboardButton('назад')
      markup.add(item1, item2, item3, item4, back)
      start_message = f"<b>Hello</b>, <i>{message.from_user.first_name}</i>"
      bot.send_message(message.chat.id, start_message, reply_markup = markup, parse_mode="html")

    elif message.text == 'назад':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('1')
      item2 = types.KeyboardButton('2')
      item3 = types.KeyboardButton('3')
      item4 = types.KeyboardButton('4')
      item5 = types.KeyboardButton('5')
      markup.add(item1, item2, item3, item4, item5)
      start_message = "назад"
      bot.send_message(message.chat.id, start_message, reply_markup = markup, parse_mode="html")
  
  
bot.polling(non_stop=True,)