import requests
from enum import Enum


class Lang(Enum):
    RU = 'ru', 'russian', 'русский'
    EN = 'en', 'english', 'английский'
    FR = 'fr', 'french', 'французский'

    @staticmethod
    def get_all():
        return [
            Lang.RU,
            Lang.EN,
            Lang.FR
        ]


class Units(Enum):
    METRIC = 'metric', 'metric', 'метрическая'
    IMPERIAL = 'imperial', 'imperic', 'имперская'

    @staticmethod
    def get_all():
        return [
            Units.METRIC,
            Units.IMPERIAL
        ]


class WeatherForecast:
    _token = "7c65ce3d00f472792829dea755a97227"
    _url = 'https://api.openweathermap.org/data/2.5/weather'

    def __init__(self):
        self._city = "Москва"
        self._lang = Lang.RU
        self._units = Units.METRIC

    def _get_params(self):
        return {
            'appid': WeatherForecast._token,
            'units': self._units.value[0],
            'lang': self._lang.value[0],
            'q': self._city
        }

    def get_data(self):
        return requests.get(WeatherForecast._url, self._get_params())

    def set_city(self, new_city: str) -> bool:
        prev_city = self._city
        self._city = new_city
        if self.get_data().status_code != 200:
            self._city = prev_city
            return False
        return True

    def set_lang(self, language: str) -> bool:
        for lang in Lang.get_all():
            if language == lang.value[1] or language == lang.value[2]:
                self._lang = lang
                return True
        return False

    def set_units(self, unit: str) -> bool:
        for u in Units.get_all():
            if unit == u.value[1] or unit == u.value[2]:
                self._units = u
                return True
        return False


