"""Task6
Використовуючи код example_10, створіть декоратори @classmethod
для формування переліку об'єктів, які підрахують кількість
повнолітніх людей в Україні та Америці.
"""

from task5_staticMethod import Person


class Human(Person):
    _adults_quantity_ua = 0
    _adults_quantity_usa = 0

    def __init__(self, surname, name, age):
        super().__init__(surname, name, age)

    def __new__(cls, surname, name, age):
        cls._verify_age(age)
        cls.__add_adults(age)
        return object.__new__(cls)

    @classmethod
    def __add_adults(cls, age):
        if cls.is_adult_in_UA(age):
            cls._adults_quantity_ua += 1
        if cls.is_adult_in_USA(age):
            cls._adults_quantity_usa += 1

    @property
    def adults_quantity_ua(self):
        return self._adults_quantity_ua

    @property
    def adults_quantity_usa(self):
        return self._adults_quantity_usa


# test
if __name__ == "__main__":
    person_1 = Human('Glushko', 'Khateryna', 19)
    person_2 = Human('Kuleba', 'Tetiana', 30)
    person_3 = Human('Karelis', 'Nikos', 20)

    print(f'UA adults: {person_3.adults_quantity_ua}')
    print(f'USA adults: {person_3.adults_quantity_usa}')
    print()
    print(f'{person_1.name} is {person_1.age}')
    print(f'{person_2.name} is {person_2.age}')
    print(f'{person_3.name} is {person_3.age}')
