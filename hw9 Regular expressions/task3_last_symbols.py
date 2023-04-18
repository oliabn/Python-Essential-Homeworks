"""Task3
Користувач вводить з клавіатури пропозицію. Написати функцію,
яка друкуватиме на екран останні 3 символи кожного слова.
"""

import re


def get_last_symbols(text):
    return re.findall(r"[a-zA-Z]*([a-zA-Z]{3})\b", text)


text = input("Enter some text: ")
print(get_last_symbols(text))
