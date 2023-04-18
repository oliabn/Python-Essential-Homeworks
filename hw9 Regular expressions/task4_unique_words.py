"""Task4
Напишіть функцію, яка буде аналізувати текст,
що надходить до неї, і виводити тільки унікальні
слова на екран, загальну кількість слів і
кількість унікальних слів.
"""

import re


def count_words(text):
    """Return a tuple containing unique words
    from a text, the total number of words,
    and the number of unique words"""

    def split_words(text):
        words = re.findall(r"(\w+\'?\w+|\w+)", text.casefold())
        return words

    words = split_words(text)
    unique_words = set(words)
    return unique_words, len(words), len(unique_words)


text = """It's a task about unique:
          Some text. Some text. Word.
          Word, word, word"""
# text = ''

print(f'Unique: {count_words(text)[0]}\n'
      f'Total count: {count_words(text)[1]}\n'
      f'Count of unique: {count_words(text)[2]}')
