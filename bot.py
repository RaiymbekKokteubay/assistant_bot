import telebot
import os
import json
from telebot import types

responses = json.load(open("responses.json", encoding="utf-8"))
buttons = json.load(open("buttons.json", encoding="utf-8"))
api_key = os.getenv('TELEGRAM_API')
bot = telebot.TeleBot(api_key)

@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1 = types.KeyboardButton("ua")
  item2 = types.KeyboardButton("ru")
  markup.add(item1, item2)
  bot.send_message(
    message.chat.id,
    "Выберите язык / Choose language",
    reply_markup=markup,
    parse_mode="html"
  )

@bot.message_handler(content_types=['text'])
def bot_message(message):
  if message.chat.type == 'private':

    if message.text in ["ru", "ua", buttons["back"]["ru"]]:
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = types.KeyboardButton(buttons["hotlines"]["ru"])
      item2 = types.KeyboardButton(buttons["government"]["ru"])
      item3 = types.KeyboardButton(buttons["assist"]["ru"])
      markup.add(item1, item2, item3)
      start_message = f"Теперь выберите категорию"
      bot.send_message(
        message.chat.id,
        start_message,
        reply_markup=markup,
        parse_mode="html"
      )

    elif message.text == buttons["hotlines"]["ru"]:
      reply = responses["hotlines"]["ru"]
      bot.send_message(message.chat.id, reply, parse_mode="html")

    elif message.text == buttons["government"]["ru"]:
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = types.KeyboardButton(buttons["bank"]["ru"])
      item2 = types.KeyboardButton(buttons["psc"]["ru"])
      item3 = types.KeyboardButton(buttons["embassy"]["ru"])
      item4 = types.KeyboardButton(buttons["back"]["ru"])
      markup.add(item1, item2, item3, item4)
      bot.send_message(
        message.chat.id,
        "Выберите подходящую категорию",
        reply_markup=markup,
        parse_mode="html"
      )

    elif message.text == buttons["bank"]["ru"]:
      reply = responses["bank"]["ru"]
      bot.send_message(message.chat.id, reply, parse_mode="html")

    elif message.text == buttons["psc"]["ru"]:
      reply = responses["psc"]["ru"]
      bot.send_message(message.chat.id, reply, parse_mode="html")

    elif message.text == buttons["embassy"]["ru"]:
      reply = responses["embassy"]["ru"]
      bot.send_message(message.chat.id, reply, parse_mode="html")

    elif message.text == buttons["funds"]["ru"]:
      reply = responses["funds"]["ru"]
      bot.send_message(message.chat.id, reply, parse_mode="html")

bot.polling(non_stop=True,)