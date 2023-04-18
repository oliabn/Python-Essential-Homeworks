"""task1
- Напишіть скрипт, який створює текстовий файл і записує
до нього 10000 випадкових дійсних чисел.
- Створіть ще один скрипт, який читає числа з
файлу та виводить на екран їхню суму.
"""

from random import randint

with open('random_numbers.txt', 'w', encoding='utf-8') as file:
    for _ in range(1001):
        num = randint(0, 100)
        file.write(str(num) + ' ')
