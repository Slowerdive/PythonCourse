Вы - начинающий журналист. Накануне вечером вы написали статью про кошек для ветеринарного журнала,
но забыли заблокировать компьютер. На утро вы обнаружили, что вашей собаке не понравилось, что пишете вы про кошек,
а не про собак.
Она испортила вам статью и оставила следующую записку:
1) я заменила все слова "cat" в статье на "woof-woof"
2) я развернула каждое предложение и добавила в его конец, перед точкой, строку, состояющую из символа "!".
Длина этой строки восклицательных знаков равна длине предложения (без учета точки).
3) я перевела все предложения в верхний регистр

Попробуй вернуть все назад, woof-woof!

Ваша задача вернуть текст в первозданный вид.
Ограничения:
1) В результате предложения разделены символом '.\n'.
2) В результате все предложения начинаются с буквы верхнего регистра. Это единственная буква в верхнем регистре
в предложении.

Исходный текст представлен в файле [correct_article.txt](./articles/correct_article.txt).
Испорченный текст представлен в файле [wrong_article.txt](./articles/wrong_article.txt).

Реализуйте код, который восстановит статью и вернет ее в качестве результата работы функции.

Проверка результата:
```bash
pytest ./4_safe_text/test.py
```