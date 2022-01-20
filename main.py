import random

import telebot
from telebot import types
token = "5045287320:AAFZIenCoItJsDMhHBrG78T6bBNOuiqyv7I"
bot = telebot.TeleBot(token)
first = ["Желаю хорошего, продуктивного, прекрасного дня! Пусть день пройдет легко, в хорошем настроении", "All Heil Mordor", "Чтобы не было проблем надо их для начала не создавать"]

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", "/music", "/wishes")
    bot.send_message(message.chat.id, 'Здравствуйте! Хотите узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею...')
    bot.send_message(message.chat.id, 'А нихрена не умею, я плод больного воображения')
    bot.send_message(message.chat.id, 'Шучу, таки могу кашерную музыку поставить /music')
    bot.send_message(message.chat.id, 'Или присылать пожелания на день, чтобы у тебя было настроение: /wishes')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Уважаемый, таки вам надо на сайт – https://mtuci.ru/')

@bot.message_handler(commands=['music'])
def wish_message(message):
    bot.send_audio(message.chat.id, open("Roki_Vulovic_-_Panteri_Mauzer_59292053.mp3", 'rb'))

@bot.message_handler(commands=['wishes'])
def wish_message(message):
    bot.send_message(message.chat.id, random.choice(first))

bot.polling()


