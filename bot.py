import telebot
import sqlite3
import os
import json
from telebot import types

responses = json.load(open("responses.json", encoding="utf-8"))
buttons = json.load(open("buttons.json", encoding="utf-8"))
api_key = os.getenv('TELEGRAM_API')
bot = telebot.TeleBot(api_key)

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()

def start_menu(message, lang):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add(
		types.KeyboardButton(buttons["hotlines"][lang]),
		types.KeyboardButton(buttons["government"][lang]),
		types.KeyboardButton(buttons["assist"][lang]),
		types.KeyboardButton(buttons["hot_lines"][lang]),
		types.KeyboardButton(buttons["change_lang"][lang])
	)
	bot.send_message(
		message.chat.id,
		responses["start_message"][lang],
		reply_markup=markup,
		parse_mode="html"
	)

def set_language(message):
	user_id = message.from_user.id
	markup = types.InlineKeyboardMarkup()
	markup.width = 2
	markup.add(
		types.InlineKeyboardButton("🇺🇦", callback_data=f"ua:{user_id}"),
		types.InlineKeyboardButton("🇷🇺", callback_data=f"ru:{user_id}"),
	)
	bot.send_message(
		message.chat.id,
		"Выберите язык / Оберіть мову",
		reply_markup=markup,
		parse_mode="html"
	)

@bot.callback_query_handler(func=lambda call: True)
def callback_handle(call):
	if call.data[:2] in ["ru", "ua"]:
		lang, user_id = call.data.split(":")
		user_id = int(user_id)
		cursor.execute(
			'REPLACE INTO main (user_id, lang) VALUES (?, ?)',
			(user_id, lang),
		)
		conn.commit()
		start_menu(call.message, lang)

@bot.message_handler(commands=['start'])
def start(message):
	set_language(message)

@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type == 'private':
		user_id = message.from_user.id
		cursor.execute("SELECT lang FROM main WHERE user_id=?", (user_id,))
		lang = cursor.fetchone()[0]
		if message.text == buttons["back"][lang]:
			start_menu(message, lang)
		elif message.text == buttons["change_lang"][lang]:
			set_language(message)
		elif message.text == buttons["hotlines"][lang]:
			reply = responses["hotlines"][lang]
			bot.send_message(message.chat.id, reply, parse_mode="html")
		elif message.text == buttons["hot_lines"][lang]:
			reply = responses["hot_lines"][lang]
			bot.send_message(message.chat.id, reply, parse_mode="html")
		elif message.text == buttons["government"][lang]:
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			markup.add(
				types.KeyboardButton(buttons["bank"][lang]),
				types.KeyboardButton(buttons["embassy"][lang]),
				types.KeyboardButton(buttons["psc"][lang]),
				types.KeyboardButton(buttons["back"][lang]),
			)
			bot.send_message(
				message.chat.id,
				"Выберите подходящую категорию",
				reply_markup=markup,
				parse_mode="html"
	  		)
		elif message.text == buttons["bank"][lang]:
			reply = responses["bank"][lang]
			bot.send_message(message.chat.id, reply, parse_mode="html")
		elif message.text == buttons["psc"][lang]:
			reply = responses["psc"][lang]
			bot.send_message(message.chat.id, reply, parse_mode="html")
		elif message.text == buttons["embassy"][lang]:
			reply = responses["embassy"][lang]
			bot.send_message(message.chat.id, reply, parse_mode="html")
		elif message.text == buttons["assist"][lang]:
			reply = responses["assist"][lang]
			bot.send_message(message.chat.id, reply, parse_mode="html")

bot.polling(non_stop=True,)