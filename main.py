import telebot
from telebot import types
from weather_forecast import WeatherForecast
from start_module import start_module

token = '5189850186:AAHPqb5LybLL9uRTHkZKOHsIqn4HPD2OHGk'
bot = telebot.TeleBot(token)
weather_forecast = WeatherForecast()

bot.set_my_commands([
    types.BotCommand('start', 'Начните работу с ботом')
])

start_module(bot, weather_forecast)


bot.infinity_polling()


