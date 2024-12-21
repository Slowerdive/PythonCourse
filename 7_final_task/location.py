import requests

def get_location():
    """Определяет текущее местоположение по IP-адресу с использованием IP-API."""
    try:
        response = requests.get("http://ip-api.com/json/?lang=ru")
        response.raise_for_status()
        data = response.json()

        if data['status'] == 'success':
            city = data.get('city', 'Неизвестный город')
            region = data.get('regionName', 'Неизвестный регион')
            country = data.get('country', 'Неизвестная страна')
            lat = data.get('lat')
            lon = data.get('lon')
            return city, region, country, lat, lon
        else:
            print(f"Ошибка: {data.get('message', 'Не удалось определить местоположение.')}")
            return None
    except Exception as e:
        print(f"Ошибка при определении местоположения: {e}")
        return None

if __name__ == "__main__":
    location = get_location()
    if location:
        city, region, country, lat, lon = location
        print(f"Город: {city}")
        print(f"Регион: {region}")
        print(f"Страна: {country}")
        print(f"Широта: {lat}")
        print(f"Долгота: {lon}")
    else:
        print("Не удалось определить местоположение.")
