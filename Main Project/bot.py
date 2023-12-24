import telebot
import traceback
from telebot import types
from config.config import Config
from api.weather import WeatherAPI


bot = telebot.TeleBot(Config.get_config_item('TELEGRAM', 'TOKEN'))


@bot.message_handler(commands=['start'])
def start_handler(message):
    btn_my_geo_weather = types.KeyboardButton(text='Погода рядом со мной', request_location=True)

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(btn_my_geo_weather)

    bot.send_message(message.from_user.id, 'Привет! Это бот для получения прогноза погоды. '
                                           'Чтобы узнать погоду в каком-либо городе, просто введите '
                                           'его название!', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, 'Введите название города, чтобы узнать погоду в нем')


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        user_location = message.location
        lon = user_location.longitude
        lat = user_location.latitude

        try:
            btn_city_weather_forecast = types.InlineKeyboardButton('Получить прогноз погоды',
                                                                   callback_data=f'{lon}, {lat}')
            inline_kb = types.InlineKeyboardMarkup().add(btn_city_weather_forecast)

            bot.send_message(message.from_user.id, WeatherAPI.get_current_weather_by_coord(lon, lat),
                             reply_markup=inline_kb)
        except Exception:
            print(traceback.format_exc())
            return 'Неизвестная ошибка при получении информации из API. Повторите попытку позже!'


@bot.message_handler(content_types=['text'])
def get_city_weather(message):
    text = message.text

    if text[0] == '/':
        bot.send_message(message.from_user.id, 'Неизвестная команда!')
    else:
        try:
            btn_city_weather_forecast = types.InlineKeyboardButton('Получить прогноз погоды', callback_data=text)
            inline_kb = types.InlineKeyboardMarkup().add(btn_city_weather_forecast)

            bot.send_message(message.from_user.id, WeatherAPI.get_current_weather_for_city(text),
                             reply_markup=inline_kb)
        except Exception:
            print(traceback.format_exc())
            return 'Неизвестная ошибка при получении информации из API. Повторите попытку позже!'


@bot.callback_query_handler(func=lambda c: c.json['message']['reply_markup']['inline_keyboard'][0][0]['text'] == 'Получить прогноз погоды')
def get_city_weather_forecast(callback_query: types.CallbackQuery):
    text = callback_query.data
    lon, lat = '', ''
    for_city = True

    if len(text.split(', ')) >= 2:
        x = text.split(', ')
        lon = x[0]
        lat = x[1]
        for_city = False


    try:
        if for_city:
            forecast = WeatherAPI.get_weather_forecast_for_city(text)
            bot.send_message(callback_query.from_user.id, forecast)
        else:
            forecast = WeatherAPI.get_weather_forecast_by_coord(lon, lat)
            bot.send_message(callback_query.from_user.id, forecast)
    except Exception:
        print(traceback.format_exc())
        return 'Неизвестная ошибка при получении информации из API. Повторите попытку позже!'


bot.polling(none_stop=True, interval=0)