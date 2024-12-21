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
    """Выводит историю запросов."""
    if not history:
        print("История запросов пуста.")
        return
    for entry in history:
        try:
            print(f"Город: {entry['city']}, Время: {entry['time']}, Погода: {entry['weather']}")
        except KeyError as e:
            print(f"Ошибка: отсутствует ключ {e} в записи истории.")