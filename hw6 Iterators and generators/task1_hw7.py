"""Task1 hw7
Напишіть генератор, який повертає елементи заданого
списку у зворотному порядку (аналог reversed).
"""


def reverse(lst: list):
    yield from (lst[-idx] for idx in range(1, len(lst)+1))


for elem in [1, 2, 3, 4, 59]:
    print(elem, end=', ')
