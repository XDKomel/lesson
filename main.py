import telebot
from telebot import types
from weather_forecast import WeatherForecast

token = '5189850186:AAHPqb5LybLL9uRTHkZKOHsIqn4HPD2OHGk'
bot = telebot.TeleBot(token)
weather_forecast = WeatherForecast()

bot.set_my_commands([
    types.BotCommand('start', 'Начните работу с ботом')
])

wait_for_city = False


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите свой город')
    global wait_for_city
    wait_for_city = True


@bot.message_handler(content_types=['text'])
def set_city(message):
    global wait_for_city
    if wait_for_city:
        if weather_forecast.set_city(message.text):
            bot.send_message(message.chat.id, f'Успешно установлен город {message.text}')
            wait_for_city = False
        else:
            bot.send_message(message.chat.id, 'Введите город еще раз')


bot.infinity_polling()
