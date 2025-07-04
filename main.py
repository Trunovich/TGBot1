import telebot
from telebot import *

API_TOKEN = '8080473725:AAEUd-4XcZ11NEdzPx74GZyiDZCy64H6iP8' #бот в тг создается через BotFather получаем его ключ

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])   #комманда для стартого сообщенеия с кнопками
def welcome_massage (message):

    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('изображение', callback_data='image')
    btn2 = telebot.types.InlineKeyboardButton('Мой гитхаб)', url ='https://github.com/Trunovich')
    btn3 = telebot.types.InlineKeyboardButton('сообщенние', callback_data='sms')
    markup.row(btn1)
    markup.row(btn3, btn2)
    bot.send_message(message.chat.id, 'ПРИВЕТ! \n '
                                      'Я бот созданный для теста возможностей и работоспособности давай посмотрим что я могу🧐', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)  #обработка нажатия кнопок в стартовом сообщении
def callback(callback):
    if callback.data == 'image':
        bot.send_photo(callback.message.chat.id, open('image.png', 'rb'))
    if callback.data == 'sms':
        bot.send_message(callback.message.chat.id,'необходимое сообщение')
    bot.answer_callback_query(callback.id)

@bot.message_handler(commands=['help'])
def help_massage (message):
    bot.reply_to(message, 'Текст помощи в нем можно оставить ссылку на тех поддержку')

@bot.message_handler()
def Trigger_message(message):
    if message.text.lower() in ('триггерное сообщение', 'можно различные') :
        bot.reply_to(message, 'ответ на нужные сообщения')

bot.polling(none_stop=True)
