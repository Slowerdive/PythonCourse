import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    wrong_article = get_wrong_article()
    lines = wrong_article.split('\n')
    fixed_article = []

    for line in lines:
        line_reversed = line[::-1]
        content_length = len(line_reversed) // 2
        sentence = line_reversed[content_length + 1:]
        sentence = sentence.replace('WOOF-WOOF', 'cat')
        if sentence:
            sentence = sentence.capitalize() + '.'

        fixed_article.append(sentence)

    correct_article = '\n'.join(fixed_article)
    wrong_article = correct_article
    return wrong_article
