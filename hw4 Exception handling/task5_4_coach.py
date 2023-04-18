"""Task5
Створіть програму спортивного комплексу, у якій передбачене меню:
1 - перелік видів спорту, 2 - команда тренерів, 3 - розклад тренувань,
4 - вартість тренування. Дані зберігати у словниках.
Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури
у відповідному пункті меню. Якщо ключ не буде знайдений, створити
відповідний клас-Exception, який буде викликатися в обробнику виключень.
"""


class Coach:
    """Coach with param: name, surname, discipline
     (available disciplines are from the Discipline class)"""

    def __init__(self, name: str, surname: str):
        self._name = self._is_valid_name(name)
        self._surname = self._is_valid_name(surname)

    def __repr__(self):
        return f'{self._name} {self._surname}'

    def __str__(self):
        return f'{self._name} {self._surname}'

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

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, val: str):
        self._name = self._is_valid_name(val)

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, val: str):
        self._surname = self._is_valid_name(val)


# test
if __name__ == '__main__':
    coach_1 = Coach('Leslie', 'Mckinney')
    coach_2 = Coach('Terry', 'Pratchett')
    coach_3 = Coach('Nolan', 'Gibney')

    print(coach_1)
    print(coach_2)
    print(coach_3)
