import telebot
from telebot import types
import requests

urlYoutube = 'https://www.youtube.com/'
urlFacebok = 'https://ru-ru.facebook.com/'
urlInstagram = 'https://www.instagram.com/'
urlTwitter = 'https://twitter.com/?lang=ru'

def checkSocNetworks(message, url):
	try:
		res = requests.get(url)
		print(res.status_code)

		if res.status_code == 200:
			bot.send_message(message.chat.id, "Выбранный вами сервис "+str(message.text)+" функционирует нормально.")
			bot.send_message(message.chat.id, "вот ваш ресурс \n"+url)

	except Exception as e:
		bot.send_message(message.chat.id, "Выбранный вами сервис "+str(message.text)+" недоступен.")

bot = telebot.TeleBot(<token>)

@bot.message_handler(commands=['start'])
def start_message(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("youtube")
	item2=types.KeyboardButton("facebook")
	item3=types.KeyboardButton("instagram")
	item4=types.KeyboardButton("twitter")
	markup.add(item1)
	markup.add(item2)
	markup.add(item3)
	markup.add(item4)
	bot.send_message(message.chat.id,"Привет, выберите сервис который вы хотите проверить.", reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
	if message.text=="youtube":
		checkSocNetworks(message, urlYoutube)

	if message.text=="facebook":
		checkSocNetworks(message, urlFacebok)

	if message.text=="instagram":
		checkSocNetworks(message, urlInstagram)

	if message.text=="twitter":
		checkSocNetworks(message, urlTwitter)

bot.polling(none_stop=True)
