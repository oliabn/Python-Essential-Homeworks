"""Task3
Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ
і рік початку роботи. Конструктор має генерувати виняток, якщо вказано
неправильні дані. Введіть список працівників із клавіатури.
Виведіть усіх співробітників, які були прийняті після цього року.
"""

from datetime import date


class Employee:
    """Employee with param: name, surname,
    department, and year of commencement of work"""

    DEPARTMENTS = ['marketing', 'operations', 'finance',
                   'sales', 'hr', 'purchase']

    def __init__(self, name: str, surname: str, department: str, year: int):
        self.name = self._is_valid_name(name)
        self.surname = self._is_valid_name(surname)
        self.department = self._is_valid_department(department)
        self.year = self._is_valid_year(year)

    def __str__(self):
        return f"{self.name} {self.surname} works in {self.department.title()} " \
               f"Department from {self.year}."

    def __eq__(self, other):
        if isinstance(other, Employee):
            return (self.name == other.name
                    and self.surname == other.surname
                    and self.department == other.department
                    and self.year == other.year)

    @staticmethod
    def _is_valid_name(name: str) -> str:
        if type(name) != str:
            raise TypeError(f"The name and surname must be str.")
        if not name.isalpha():
            raise ValueError("The name and surname must consist "
                             "of only alphabetic symbols.")
        if len(name) < 2:
            raise ValueError('The name and surname must be '
                             'longer than one letter.')
        return name.title()

    @staticmethod
    def _is_valid_year(year: int) -> int:
        establishment_year = 1990
        current_year = date.today().year

        if type(year) != int:
            raise TypeError("The year must be int, e.g. 2019.")
        if len(str(year)) != 4:
            raise ValueError("The year must be in format 2021.")
        if not (establishment_year < year <= current_year):
            raise ValueError(f"The year should be between "
                             f"{establishment_year} and {current_year}.")
        return year

    @classmethod
    def _is_valid_department(cls, department: str) -> str:
        if type(department) != str:
            raise TypeError("The department must be str.")
        if department not in cls.DEPARTMENTS:
            raise ValueError(f"Incorrect department. There are "
                             f"the following departments {cls.DEPARTMENTS}.")
        return department
