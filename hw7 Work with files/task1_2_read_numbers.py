"""task1
- Напишіть скрипт, який створює текстовий файл і записує
до нього 10000 випадкових дійсних чисел.
- Створіть ще один скрипт, який читає числа з
файлу та виводить на екран їхню суму.
"""

with open('random_numbers.txt', 'r+', encoding='utf-8') as file:
    numbers = file.readline().split()
    numbers = list(map(int, numbers))

print('Sum =', sum(numbers))

# for check
print('First 3 numbers:', numbers[0], numbers[1], numbers[2])
