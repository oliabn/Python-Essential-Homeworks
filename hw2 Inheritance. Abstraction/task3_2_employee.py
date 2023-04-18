"""Task3
Створіть ієрархію класів із використанням множинного успадкування.
Виведіть на екран порядок вирішення методів для кожного класу.
Поясніть, чому лінеаризація даних класів виглядає саме так.
"""

from task3_1_person import Person


class Employee(Person):
    def __init__(self, name, age, position):
        self._verify_position(position)

        super().__init__(name, age)
        self._position = position

    @staticmethod
    def _verify_position(position):
        if type(position) != str:
            raise TypeError("The position must be a string")

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._verify_position(value)
        self._position = value

    def print_info(self):
        print(f'{self.name}: {self.position}')
