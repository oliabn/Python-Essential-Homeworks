from string import ascii_letters


class Person:
    CYRILLIC = "абвгґдеэєжзыиіїклмнопрстуфчцчшщьъюя-'"
    CYRILLIC_UPPER = CYRILLIC.upper()

    def __init__(self, fio: str, old: int):
        self.verify_name(fio)
        self.verify_old(old)

        self.__fio = fio
        self.__old = old

    @classmethod
    def verify_name(cls, fio):
        if type(fio) != str:
            raise TypeError("The name must be a string")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("The format must be: Name Surname Middle name")

        letters = ascii_letters + cls.CYRILLIC + cls.CYRILLIC_UPPER
        for char in f:
            if len(char) < 1:
                raise TypeError("There must be at least one character")
            if len(char.strip(letters)) != 0:
                raise TypeError("Must be only alphabetic letters")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("The old must be: 14 < int number < 120")

    @property  # getter
    def fio(self):
        return self.__fio

    @property   # getter
    def old(self):
        return self.__old

    @old.setter
    def old(self, old: int):
        self.verify_old(old)
        self.__old = old


p = Person("Olha Olha Olha", 30)



