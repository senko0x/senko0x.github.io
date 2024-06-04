import telebot
from telebot import types
from telebot.types import WebAppInfo
import json

bot = telebot.TeleBot(token='7128904242:AAFzulAY4xdPnSQ9MVUkl3yhO6BE_L_CoM4')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_info = WebAppInfo(url='https://senko0x.github.io/')
    markup.add(types.KeyboardButton(text='Открыть приложение', web_app=web_app_info))
    bot.send_message(message.chat.id, 'Чо ты лысый плаки плаки', reply_markup=markup)

@bot.message_handler(content_types=['web_app_data'])
def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    bot.send_message(message.chat.id, f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}')

bot.polling(non_stop=True)
