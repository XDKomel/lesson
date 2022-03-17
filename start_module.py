city_set = False


def start_module(bot, weather_forecast):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, 'Введите свой город, начав со слова "город"')
        global city_set
        city_set = False

    @bot.message_handler(func=lambda m: 'город' in m.text)
    def set_city(message):
        global city_set
        if not city_set:
            text = message.text.split()
            text.remove('город')
            city = ' '.join(text)
            if weather_forecast.set_city(city):
                bot.send_message(message.chat.id, f'Успешно установлен город {city}')
                city_set = True
            else:
                bot.send_message(message.chat.id, 'Введите город еще раз')
