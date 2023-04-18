"""Task3
Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ
і рік початку роботи. Конструктор має генерувати виняток, якщо вказано
неправильні дані. Введіть список працівників із клавіатури.
Виведіть усіх співробітників, які були прийняті після цього року.
"""

from task3_1_employee import Employee

RED, RESET = "\033[31m", "\033[0m"
HELP = "\nEnter name, surname, department, year of employee by a space\n" \
       f"Available departments: {Employee.DEPARTMENTS}\n" \
       "e.g.: Alice Blackwood finance 2022 -> "

employees = []

# create 2 employees and add they're to the employee list
while True:
    try:
        name, surname, department, year = input(HELP).split()
        try:
            year = int(year)
        except ValueError:
            print(f"\n{RED}The year must be integer, e.g. 2022.")
            print(f"Try again{RESET}")
            continue
    except ValueError as err:
        print(f'\n{RED}{err}')
        print("Enter only name, surname, department, and year by a space.")
        print(f'Try again{RESET}')
        continue

    try:
        employees.append(Employee(name, surname, department, year))
        print('\n       Employee was added.')
        if len(employees) == 2:
            break
    except ValueError as err:
        print(f'\n{RED}{err}')
        print(f'Try again{RESET}')
        continue
    except Exception as err:
        print(f'\n{RED}{err}')
        print(f'Try again{RESET}')
        continue

print('\nAll employees')
for employee in employees:
    print(employee)

print('\nNew employees')
for employee in employees:
    if employee.year == 2022:
        print(employee)
