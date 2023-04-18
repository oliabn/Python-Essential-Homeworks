"""Task3
Створіть ієрархію класів із використанням множинного успадкування.
Виведіть на екран порядок вирішення методів для кожного класу.
Поясніть, чому лінеаризація даних класів виглядає саме так.
"""

from task3_2_employee import Employee
from task3_3_salary import Salary


class SchoolEmployee(Employee, Salary):
    POSITIONS = ['teacher', 'deputy director', 'director',
                 'psychologist', 'security guard', 'cleaner']

    def __init__(self, name, age, position, monthly_rate, overtime_rate=0, overtime_hours=0):
        Employee.__init__(self, name, age, position)
        Salary.__init__(self, monthly_rate, overtime_rate, overtime_hours)

    @classmethod
    def _verify_position(cls, position):
        if type(position) != str:
            raise TypeError("The position must be a string")
        if position not in cls.POSITIONS:
            raise ValueError(f"Incorrect position, available positions {cls.POSITIONS}")


# test
if __name__ == "__main__":
    teacher = SchoolEmployee('Alice Bishop', 30, 'teacher', 2000)

    print('Print Info method:')
    teacher.print_info()
    print()

    print('Print attributes:')
    print(f'{teacher.name} is {teacher.age}, salary: {teacher.salary}')
    print()

    print("Set overtime and print salary:")
    teacher.overtime_rate = 8
    teacher.overtime_hours = 9
    print(f'{teacher.name} is {teacher.age}, salary with overtime: {teacher.salary}')
