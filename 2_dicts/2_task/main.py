import re


def top_10_most_common_words(text: str) -> dict:
    text = text.lower()

    words = re.findall(r'\b\w+\b', text)

    words = [word for word in words if len(word) >= 3]

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    def sort_key(item):
        word, count = item
        return (-count, word)

    sorted_words = sorted(word_counts.items(), key=sort_key)

    most_common = {word: count for word, count in sorted_words[:10]}

    return most_common
