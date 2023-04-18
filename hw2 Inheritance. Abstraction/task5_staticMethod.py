"""Task5
Використовуючи код example_10, створіть @staticmethod
для визначення повноліття людини в Україні та Америки.
"""

from datetime import date


class Person:
    def __init__(self, surname, name, age):
        self._verify_name(surname)
        self._verify_name(name)
        self._verify_age(age)

        self.surname = surname
        self.name = name
        self.age = age

    @staticmethod
    def _verify_age(age):
        if not isinstance(age, int):
            raise TypeError("The age must be integer")

    @staticmethod
    def _verify_name(name):
        if not isinstance(name, str):
            raise TypeError("The name/surname must be str")
        if not name.isalpha():
            raise ValueError("The name/surname must consist of at least a first name and a surname")

    @classmethod
    def fromBirthYear(cls, surname, name, birth_year):
        cls._verify_name(surname)
        cls._verify_name(name)
        cls._verify_age(birth_year)
        return cls(surname, name, date.today().year - birth_year)

    @staticmethod
    def is_adult_in_UA(age):
        return age > 17

    @staticmethod
    def is_adult_in_USA(age):
        return age > 21

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))


# test
if __name__ == "__main__":
    adult = Person.fromBirthYear('Alice', 'Bishop', 1990)
    ua_teenager = Person('Glushko', 'Khateryna', 15)
    usa_teenager = Person('Karelis', 'Nikos', 20)

    print(f'adult: {adult.is_adult_in_UA(adult.age)}')
    print(f'ua_teenager: {ua_teenager.is_adult_in_UA(ua_teenager.age)}')
    print(f'usa_teenager: {usa_teenager.is_adult_in_USA(usa_teenager.age)}')
