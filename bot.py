import telebot
from telebot import types
from weather_forecast import WeatherForecast
from start_module import start_module
import schedule
from threading import Thread

token = '5189850186:AAHPqb5LybLL9uRTHkZKOHsIqn4HPD2OHGk'
bot = telebot.TeleBot(token)
weather_forecast = WeatherForecast()
chat_id = None

bot.set_my_commands([
    types.BotCommand('start', 'Начните работу с ботом'),
    types.BotCommand('schedule', 'Запланируйте отправление сообщения в определенное время'),
])


@bot.message_handler(commands=['schedule'])
def schedule_hello(message):
    global chat_id
    chat_id = message.chat.id


def send_hello():
    if chat_id is not None:
        bot.send_message(chat_id, 'hello')


def schedule_checker():
    while True:
        schedule.run_pending()
        schedule.clear()


job = schedule.every().day.at('18:52').do(send_hello)
Thread(target=schedule_checker).start()


bot.infinity_polling()





