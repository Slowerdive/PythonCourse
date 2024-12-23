import requests
from datetime import datetime, timedelta
import pytz
from location import get_location

def get_weather(city: str):
    api_key = '9dffb8fc5b389b94f248c1230a538272' 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    try:
        response = requests.get(url)
        if response.status_code == 404:
            return "Не удалось найти такой населенный пункт. Пожалуйста, проверьте ввод."
        response.raise_for_status()

        data = response.json()

        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        wind_speed = data['wind']['speed']
        timezone_offset = data['timezone']

        current_time_utc = datetime.utcnow()
        current_time = current_time_utc + timedelta(seconds=timezone_offset)
        local_timezone = pytz.FixedOffset(timezone_offset // 60)
        current_time = local_timezone.localize(current_time)

        current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S %z")
        current_time_str = current_time_str[:-2] + ':' + current_time_str[-2:]

        weather_info = f"""
Текущее время: {current_time_str}
Название города: {city}
Погодные условия: {weather_description}
Текущая температура: {temperature} градусов по Цельсию
Ощущается как: {feels_like} градусов по Цельсию
Скорость ветра: {wind_speed} м/с
"""
        return weather_info

    except requests.exceptions.RequestException as e:
        return f"Ошибка при получении данных о погоде: {e}"


def get_weather_by_coordinates(lat, lon):
    api_key = '9dffb8fc5b389b94f248c1230a538272'  # Ваш API-ключ
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=ru"

    try:
        # Определяем название города через ip-api
        location = get_location()
        city_name = location[0] if location else "Неизвестный город"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        wind_speed = data['wind']['speed']
        timezone_offset = data['timezone']

        current_time_utc = datetime.utcnow()
        current_time = current_time_utc + timedelta(seconds=timezone_offset)
        local_timezone = pytz.FixedOffset(timezone_offset // 60)
        current_time = local_timezone.localize(current_time)

        current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S %z")
        current_time_str = current_time_str[:-2] + ':' + current_time_str[-2:]

        weather_info = f"""
Текущее время: {current_time_str}
Название города: {city_name}
Погодные условия: {weather_description}
Текущая температура: {temperature} градусов по Цельсию
Ощущается как: {feels_like} градусов по Цельсию
Скорость ветра: {wind_speed} м/с
"""
        return weather_info

    except requests.exceptions.RequestException as e:
        return f"Ошибка при получении данных о погоде: {e}"
