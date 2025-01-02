from weather import get_weather, get_weather_by_coordinates
from history import save_history, print_history
from location import get_location
from datetime import datetime


def handle_choice(choice):
    if choice == '1':
        city = input("Введите название города: ")
        weather_info = get_weather(city)
        if weather_info:
            print(weather_info)
            save_history({"city": city, "weather": weather_info, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        else:
            print("Не удалось получить данные о погоде.")
    elif choice == '3':
        location = get_location()
        if location:
            city, region, country, lat, lon = location
            weather_info = get_weather_by_coordinates(lat, lon)
            if weather_info:
                print(weather_info)
                save_history({"city": f"{city}, {region}, {country}",
                              "weather": weather_info,
                              "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            else:
                print("Не удалось получить данные о погоде для вашего местоположения.")
        else:
            print("Не удалось определить местоположение.")
    elif choice == '2':
        print_history()
    elif choice == '4':
        print("Выход из программы.")
        return False
    return True


def main():
    while True:
        print("\nМеню:")
        print("1. Получить погоду для города")
        print("2. Показать историю запросов")
        print("3. Получить погоду по текущему местоположению")
        print("4. Выход")

        try:
            choice = input("Выберите действие: ")
            if not handle_choice(choice):
                break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            print("Попробуйте снова или выберите другой пункт меню.")


if __name__ == '__main__':
    main()
