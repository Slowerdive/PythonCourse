from datetime import datetime

history = []

def save_history(entry):
    """Сохраняет запись в историю."""
    try:
        entry["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        history.append(entry)
    except Exception as e:
        print(f"Ошибка при сохранении истории: {e}")

def print_history():
    """Выводит историю запросов в обратном порядке."""
    if not history:
        print("История запросов пуста.")
        return

    try:
        count = input("Сколько последних запросов показать? (нажмите Enter для вывода всех): ")
        if count.isdigit():
            count = int(count)
            history_to_show = history[-count:][::-1]
        else:
            history_to_show = history[::-1]

        for entry in history_to_show:
            print(f"{entry['weather']}")
    except KeyError as e:
        print(f"Ошибка: отсутствует ключ {e} в записи истории.")
    except Exception as e:
        print(f"Ошибка при выводе истории: {e}")
