Во время опросов сторонних сервисов может случаться всякое. К примеру моргает сеть (на долю секунды пропадает интернет соединение), и из-за этого наши сетевые запросы возвращают ошибку.
Мы - опытные разработчики и знаем, что в таких ситуациях нам может помочь retry.
В случае получения ошибки от стороннего сервиса мы попробуем обратиться к нему снова n раз в надежде получить ответ. Используя этот паттерн мы не бездумно стучимся на сервис в тот же момент, когда получили ошибку. Мы выжидаем какой-то промежуток времени. Более продвинутые варианты наращивают это время по экспоненте.
Примерный алгоритм может выглядеть так:
* запрос к сервису, получили ошибку
* ждем 1 секунду, пытаемся повторить запрос снова
* получили ошибку
* ждем 1 секунду, пытаемся повторить запрос снова
* получили ошибку
* ждем 1 секунду, пытаемся повторить запрос снова
* успех, возвращаем результат.

Вам необходимо реализовать параметризированный декоратор вида:
```python
@retry(count=3, delay=1, handled_exceptions=(ValueError,))
```
Задержка пусть будет простой, не нужно экспоненциального увеличения промежутка между запросами.

В качестве параметров декоратор должен принимать:
* count - количество попыток
* delay - задержка между вызовыми в timedelta
* handled_exceptions - исключения, при которых мы будем делать retry 

Если за все попытки нам не удалось получить ответ, мы должы райзить тоже самое исключение, что и функция. 
В декоратор нельзя передавать count меньший 1, в противном случае надо райзить исключение ValueError.
Если не переданы исключения, то по умолчанию отлавливаем все исключения.

Код нужно реализовывать в [этом модуле](retry.py)