"""Task3
Створіть ієрархію класів із використанням множинного успадкування.
Виведіть на екран порядок вирішення методів для кожного класу.
Поясніть, чому лінеаризація даних класів виглядає саме так.
"""


class Person:
    def __init__(self, name, age):
        self._verify_name(name)
        self._verify_age(age)

        self._name = name
        self._age = age

    @classmethod
    def _verify_name(cls, name):
        if type(name) != str:
            raise TypeError("The name must be a string")
        if len(name.split()) < 2:
            raise ValueError("The name must consist of at least a first name and a surname")
        for string in name.split():
            if not string.isalpha():
                raise TypeError("The name must consist of only alphabetic characters")

    @staticmethod
    def _verify_age(age):
        if type(age) != int:
            raise TypeError("The age must be integer")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._verify_name(value)
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._verify_age(value)
        self._age = value

    def print_info(self):
        print(f"{self._name} is {self._age}")
