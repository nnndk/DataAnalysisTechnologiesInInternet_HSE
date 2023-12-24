import requests
import traceback
from config.config import Config


class WeatherAPI:
    _API_KEY = Config.get_config_item('WEATHER_API', 'API_KEY')
    _CURR_WEATHER_BASE_URL_ = 'https://api.openweathermap.org/data/2.5/weather?units=metric&lang=ru'
    _FORECAST_BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast?units=metric&lang=ru'

    @staticmethod
    def _format_weather(response: dict) -> str:
        try:
            weather_desc = response['weather'][0]['description'].capitalize()
            curr_temp = response['main']['temp']
            feels_like = response['main']['feels_like']
            #pressure = response['main']['pressure']
            humidity = response['main']['humidity']
            wind_speed = response['wind']['speed']

            return (f'Погода: {weather_desc}\n' +
                    f'Текущая температура: {curr_temp} °C\n' +
                    f'Ощущается как: {feels_like} °C\n' +
                    #f'Атмосферное давление: {pressure} мм.рт.ст.\n' +
                    f'Влажность: {humidity} %\n' +
                    f'Скорость ветра: {wind_speed} м/с')
        except KeyError:
            print(traceback.format_exc())
            return 'Неправильно введено название города!'
        except Exception:
            print(traceback.format_exc())
            return 'Неизвестная ошибка!'

    @staticmethod
    def _format_current_weather(response: dict) -> str:
        try:
            weather = WeatherAPI._format_weather(response)
            city = response['name']
            country_code = response['sys']['country']

            return f'Город: {city}, {country_code}\n' + weather
        except KeyError:
            print(traceback.format_exc())
            return 'Неправильно введено название города!'
        except Exception:
            print(traceback.format_exc())
            return 'Неизвестная ошибка!'

    @staticmethod
    def _get_current_weather_by_url(url: str) -> str:
        try:
            response = requests.get(url).json()
            return WeatherAPI._format_current_weather(response)
        except requests.exceptions.ConnectionError:
            print(traceback.format_exc())
            return 'Проблема с доступом к API. Повторите попытку позже!'
        except KeyError:
            print(traceback.format_exc())
            return 'Неправильно введено название города!'
        except Exception:
            print(traceback.format_exc())
            return 'Неизвестная ошибка!'

    @staticmethod
    def get_current_weather_for_city(city_name: str) -> str:
        url = WeatherAPI._CURR_WEATHER_BASE_URL_ + f'&q={city_name}&appid={WeatherAPI._API_KEY}'
        return WeatherAPI._get_current_weather_by_url(url)

    @staticmethod
    def get_current_weather_by_coord(lon: str, lat: str) -> str:
        url = WeatherAPI._CURR_WEATHER_BASE_URL_ + f'&lon={lon}&lat={lat}&appid={WeatherAPI._API_KEY}'
        return WeatherAPI._get_current_weather_by_url(url)

    @staticmethod
    def _format_weather_forecast(response: dict) -> str:
        try:
            weather = ''
            forecast_list = response['list']

            for i in range(min(len(forecast_list), 8)):
                dt = forecast_list[i]['dt_txt']
                weather += '\n\n' + f'Дата и время: {dt}\n' + WeatherAPI._format_weather(forecast_list[i])

            city = response['city']['name']
            country_code = response['city']['country']

            return f'Город: {city}, {country_code}' + weather
        except KeyError:
            print(traceback.format_exc())
            return 'Неправильно введено название города!'
        except Exception:
            print(traceback.format_exc())
            return 'Неизвестная ошибка!'

    @staticmethod
    def _get_weather_forecast_by_url(url: str) -> str:
        try:
            response = requests.get(url).json()
            return WeatherAPI._format_weather_forecast(response)
        except requests.exceptions.ConnectionError:
            print(traceback.format_exc())
            return 'Проблема с доступом к API. Повторите попытку позже!'
        except Exception:
            print(traceback.format_exc())
            return 'Неизвестная ошибка!'

    @staticmethod
    def get_weather_forecast_for_city(city_name: str) -> str:
        url = WeatherAPI._FORECAST_BASE_URL + f'&q={city_name}&appid={WeatherAPI._API_KEY}'
        return WeatherAPI._get_weather_forecast_by_url(url)

    @staticmethod
    def get_weather_forecast_by_coord(lon: str, lat: str) -> str:
        url = WeatherAPI._FORECAST_BASE_URL + f'&lon={lon}&lat={lat}&appid={WeatherAPI._API_KEY}'
        return WeatherAPI._get_weather_forecast_by_url(url)