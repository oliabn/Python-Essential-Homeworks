"""Task5
Створіть програму спортивного комплексу, у якій передбачене меню:
1 - перелік видів спорту, 2 - команда тренерів, 3 - розклад тренувань,
4 - вартість тренування. Дані зберігати у словниках.
Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури
у відповідному пункті меню. Якщо ключ не буде знайдений, створити
відповідний клас-Exception, який буде викликатися в обробнику виключень.
"""


class Discipline:
    DISCIPLINES = ['football', 'basketball', 'volleyball', 'tennis']

    def __init__(self, discipline):
        self._discipline = self._is_valid_discipline(discipline)

    def __str__(self):
        return f'{self._discipline.title()}'

    @classmethod
    def _is_valid_discipline(cls, discipline: str) -> str:
        if discipline not in cls.DISCIPLINES:
            raise ValueError("There is no such discipline in the club")
        return discipline

    @property
    def discipline(self) -> str:
        return self._discipline

    @discipline.setter
    def discipline(self, val: str):
        self._discipline = self._is_valid_discipline(val)
