"""Task1
Написати функцію, яка за допомогою регулярних виразів розбиває
текст на окремі слова і знаходить частоту окремих слів.
"""

import re


def count_words(text):
    """Return dictionary where words are keys
    and counts of them are values"""

    def split_words(text):
        words = re.findall(r"(\w+\'?\w+|\w+)", text.casefold())
        return words

    words = split_words(text)
    word_count = ({word: words.count(word.lower()) for word in words})
    return word_count


text = """It's a task about words:
          Write a function, that splits using regular expressions
          text into individual words + finds the frequency! 
          of individual words."""

print(count_words(text))
