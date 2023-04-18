"""Task5
Створіть програму спортивного комплексу, у якій передбачене меню:
1 - перелік видів спорту, 2 - команда тренерів, 3 - розклад тренувань,
4 - вартість тренування. Дані зберігати у словниках.
Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури
у відповідному пункті меню. Якщо ключ не буде знайдений, створити
відповідний клас-Exception, який буде викликатися в обробнику виключень.
"""


class Cost:
    def __init__(self, cost):
        self._cost = self._is_valid_cost(cost)

    def __str__(self):
        return f'{self.cost}'

    @staticmethod
    def _is_valid_cost(cost):
        if not isinstance(cost, (int, float)):
            raise TypeError("The cost must be int or float")
        return cost

    @property
    def cost(self) -> (int, float):
        return self._cost

    @cost.setter
    def cost(self, val: (int, float)):
        self._cost = self._is_valid_cost(val)
