"""
Вам дан список предложений.
Предложение содержит только слова, которые разделены единичными пробелами.
Необходимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> int:
    """Пишите ваш код здесь."""
    max_word_count = 0
    
    for sentence in sentences:
        words = [word for word in sentence.split(' ') if word]
        word_count = len(words)
        if word_count > max_word_count:
            max_word_count = word_count

    return max_word_count

