"""Task2 hw7
Виведіть із списку чисел список квадратів парних чисел.
Використовуйте 2 варіанти рішення: генератор та цикл
"""


def get_squares_even(lst: list):
    """By generator"""
    yield from (elem**2 for elem in lst if not elem % 2)


def get_squares_even_num(lst: list):
    """By loop. Loop in parentheses []"""
    for num in lst:
        if not num % 2:
            print(num**2, end=', ')


print('By generator:')
for num in get_squares_even([1, 2, 3, 4, 5, 6]):
    print(num, end=', ')

print()

print('\nBy loop:')
get_squares_even_num([1, 2, 3, 4, 5, 6])
