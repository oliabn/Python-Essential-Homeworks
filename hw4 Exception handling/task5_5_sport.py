"""Task5
Створіть програму спортивного комплексу, у якій передбачене меню:
1 - перелік видів спорту, 2 - команда тренерів, 3 - розклад тренувань,
4 - вартість тренування. Дані зберігати у словниках.
Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури
у відповідному пункті меню. Якщо ключ не буде знайдений, створити
відповідний клас-Exception, який буде викликатися в обробнику виключень.
"""

from datetime import time

from task5_1_schedule import Schedule
from task5_2_cost import Cost
from task5_3_discipline import Discipline
from task5_4_coach import Coach


class Sport:
    """
    Sport with param: discipline, schedule, cost: (int, float), coaches_team
    """

    def __init__(self, discipline: str, schedule: Schedule, cost=0, coaches_team=None):
        self.coaches_team = ([] if coaches_team is None
                             else self._is_valid_coaches_team(coaches_team))
        self.discipline = Discipline(discipline)
        self.schedule = self.is_valid_schedule(schedule)
        self.cost = Cost(cost)

    def __str__(self):
        return f'{self.discipline}\n' \
               f'Coaches team: {self.coaches_team}\n' \
               f'{self.schedule}'

    @staticmethod
    def _is_valid_coaches_team(coaches_team):
        if type(coaches_team) != list:
            raise TypeError('The coaches_team must be list')

        if coaches_team:
            for coach in coaches_team:
                if not isinstance(coach, Coach):
                    raise ValueError("The coaches_team list must contain "
                                     "only Coach type elements")
        return coaches_team

    @staticmethod
    def is_valid_schedule(schedule: Schedule):
        if not isinstance(schedule, Schedule):
            raise TypeError("The schedule should be Schedule type")
        return schedule

    @property
    def coaches_team(self) -> list:
        return self._coaches_team

    @coaches_team.setter
    def coaches_team(self, val: list):
        self._coaches_team = self._is_valid_coaches_team(val)

    def find_coach(self, surname):
        for coach in self._coaches_team:
            if coach.surname == surname:
                return coach
        return False

    def add_coach(self, coach: Coach):
        if isinstance(coach, Coach):
            self._coaches_team.append(coach)
        else:
            raise ValueError("You can add only a Coach type element")

    def del_coach(self, name: str, surname: str):
        self._coaches_team = [coach for coach in self._coaches_team
                              if coach.name != name
                              and coach.surname != surname]


# test
if __name__ == '__main__':
    tennis = Sport(discipline='tennis', schedule=Schedule({'mon': time(17), 'thu': time(19)}),
                   cost=100, coaches_team=[Coach('Leslie', 'Mckinney')])
    tennis.add_coach(Coach('Kevin', 'Force'))

    basketball = Sport(discipline='basketball', schedule=Schedule({'sat': time(18), 'tue': time(19)}),
                       cost=100, coaches_team=[Coach('Nolan', 'Gibney')])

    football = Sport(discipline='football', schedule=Schedule({'wed': time(17), 'fri': time(17)}),
                     cost=100, coaches_team=[Coach('Terry', 'Pratchett')])

    print(tennis)
    print(basketball)
    print(football)

    print(tennis.find_coach('Mckinney'))
    print(football.find_coach('Pratchett'))
