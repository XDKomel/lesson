import telebot
from telebot import types
from weather_forecast import WeatherForecast
from start_module import start_module
import os
from flask import Flask, request

token = '5189850186:AAHPqb5LybLL9uRTHkZKOHsIqn4HPD2OHGk'
bot = telebot.TeleBot(token)
server = Flask(__name__)
weather_forecast = WeatherForecast()

bot.set_my_commands([
    types.BotCommand('start', 'Начните работу с ботом')
])

start_module(bot, weather_forecast)

bot.infinity_polling()

# @server.route('/' + token, methods=['POST'])
# def get_message():
#     json_string = request.get_data().decode('utf-8')
#     update = telebot.types.Update.de_json(json_string)
#     bot.process_new_updates([update])
#     return "!", 200
#
#
# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url='https://telegram-bot-xdkomel.herokuapp.com/' + token)
#     return "!", 200
#
#
# server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


