import telebot
import os
from telebot import types

api_key = os.getenv('TELEGRAM_API')
print(api_key)
bot = telebot.TeleBot(api_key)

b2t = {
  "hotlines": "☎️Горячие Линии☎️",
  "government": "Государственная служба",
  "assist": "Гумманитарная помощь" 
}

@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
  item1 = types.KeyboardButton(b2t["hotlines"])
  item2 = types.KeyboardButton(b2t["government"])
  item3 = types.KeyboardButton(b2t["assist"])
  markup.add(item1, item2, item3)
  start_message = f"<b>Hello</b>, <i>{message.from_user.first_name}</i>"
  bot.send_message(message.chat.id, start_message, reply_markup = markup, parse_mode="html")

@bot.message_handler(content_types=['text'])
def bot_message(message):
  if message.chat.type == 'private':

    if message.text == b2t["hotlines"]:
      with open("replies/hotlines.txt") as f:
        reply = f.read()
      bot.send_message(message.chat.id, reply, parse_mode="html")

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