"""Task3
Створіть ієрархію класів із використанням множинного успадкування.
Виведіть на екран порядок вирішення методів для кожного класу.
Поясніть, чому лінеаризація даних класів виглядає саме так.
"""

from task3_4_schoolEmployee import SchoolEmployee


class DentalEmployee(SchoolEmployee):
    POSITIONS = ['dentist', 'assistant', 'director',
                 'manager', 'receptionist', 'cleaner']

    def __init__(self, name, age, position, monthly_rate, overtime_rate=0, overtime_hours=0):
        super().__init__(name, age, position, monthly_rate, overtime_rate, overtime_hours)


# test
if __name__ == "__main__":
    dentist = DentalEmployee('Irwin Holland', 35, 'dentist', 3000)

    print('Print Info method:')
    dentist.print_info()
    print()

    print('Print attributes:')
    print(f'{dentist.name} is {dentist.age}, salary: {dentist.salary}')
    print()

    print("set overtime and print salary:")
    dentist.overtime_rate = 10
    dentist.overtime_hours = 5
    print(f'{dentist.name} is {dentist.age}, salary with overtime: {dentist.salary}')
