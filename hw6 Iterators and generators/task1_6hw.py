"""Task1 hw6
Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable
"""

iterable_obj = iter(range(11))
for elem in iterable_obj:
    print(elem, end=', ')
