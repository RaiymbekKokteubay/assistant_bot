import telebot
import os
import json
from telebot import types

responses = json.load(open("responses.json", encoding="utf-8"))
buttons = json.load(open("buttons.json", encoding="utf-8"))
api_key = os.getenv('TELEGRAM_API')
api_key = "5435243295:AAEDsQRyUsBg8Cmyii0NfR5j4RJJXUJ_wv8"
bot = telebot.TeleBot(api_key)

@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1 = types.KeyboardButton("ua")
  item2 = types.KeyboardButton("ru")
  markup.add(item1, item2)
  bot.send_message(
    message.chat.id,
    "Выберите язык",
    reply_markup=markup,
    parse_mode="html"
  )

@bot.message_handler(content_types=['text'])
def bot_message(message):
  if message.chat.type == 'private':

    if message.text in ["ua", "ru", buttons["back"]["ua"]]:
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = types.KeyboardButton(buttons["hotlines"]["ua"])
      item2 = types.KeyboardButton(buttons["government"]["ua"])
      item3 = types.KeyboardButton(buttons["assist"]["ua"])
      markup.add(item1, item2, item3)
      start_message = f"Теперь выберите категорию"
      bot.send_message(
        message.chat.id,
        start_message,
        reply_markup=markup,
        parse_mode="html"
      )

    elif message.text == buttons["hotlines"]["ua"]:
      reply = responses["hotlines"]["ua"]
      bot.send_message(message.chat.id, reply, parse_mode="html")

    elif message.text == buttons["government"]["ua"]:
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = types.KeyboardButton(buttons["bank"]["ua"])
      item2 = types.KeyboardButton(buttons["psc"]["ua"])
      item3 = types.KeyboardButton(buttons["embassy"]["ua"])
      item4 = types.KeyboardButton(buttons["back"]["ua"])
      markup.add(item1, item2, item3, item4)
      bot.send_message(
        message.chat.id,
        "Выберите подходящую категорию",
        reply_markup=markup,
        parse_mode="html"
      )

    elif message.text == buttons["bank"]["ua"]:
      reply = responses["bank"]["ua"]
      bot.send_message(message.chat.id, reply, parse_mode="html")

    elif message.text == buttons["psc"]["ua"]:
      reply = responses["psc"]["ua"]
      bot.send_message(message.chat.id, reply, parse_mode="html")

    elif message.text == buttons["embassy"]["ua"]:
      reply = responses["embassy"]["ua"]
      bot.send_message(message.chat.id, reply, parse_mode="html")

    elif message.text == buttons["assist"]["ua"]:
      reply = responses["assist"]["ua"]
      bot.send_message(message.chat.id, reply, parse_mode="html")

bot.polling(non_stop=True,)