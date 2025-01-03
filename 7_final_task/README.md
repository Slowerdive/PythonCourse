# Прогноз погоды


## Описание проекта
Программа предоставляет возможность получить информацию о текущей погоде для указанного города или вашего текущего местоположения. Она использует API OpenWeatherMap для получения погодных данных и IP API для определения местоположения по IP.


## Функционал
1. Получение погодных данных для конкретного города.
2. Определение погоды для вашего текущего местоположения.
3. Сохранение истории запросов с возможностью её просмотра.


## Шаги для запуска проекта
1. Установите Python
Убедитесь, что на вашем компьютере установлен Python версии 3.12, для которой разработана программа. Совместимость с другими версиями не гарантируется. Если Python отсутствует, скачайте и установите его с официального сайта Python.

2. Скачайте проект
Скачайте архив с проектом или клонируйте его с помощью Git:<br>
```git clone https://github.com/Slowerdive/PythonCourse.git```<br>
После этого вы сможете перейти в нужную папку, содержащую проект:<br>
```cd PythonCourse/7_final_task```

3. Установите зависимости:<br>
```pip install -r requirements.txt```

4. Получите API-ключ для OpenWeatherMap<br>
Зарегистрируйтесь на сайте OpenWeatherMap и получите API-ключ. Вставьте этот ключ в файл weather.py, заменив строку:<br>
```api_key = 'Ваш API-ключ'```

6. Запустите программу
В терминале перейдите в папку с проектом и выполните команду:<br>
```python main.py```

Программа предложит вам выбрать одно из действий:
1. Указать город для получения погоды.
2. Определить погоду для текущего местоположения.
3. Просмотреть историю запросов.

## Примечания
Для работы программы требуется доступ к интернету.<br>
Убедитесь, что вы правильно установили библиотеки и указали ваш API-ключ.<br>
Если возникнут ошибки, проверьте корректность шагов настройки или свяжитесь с разработчиком для получения помощи.
