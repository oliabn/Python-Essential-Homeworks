"""Task5
Створіть програму спортивного комплексу, у якій передбачене меню:
1 - перелік видів спорту, 2 - команда тренерів, 3 - розклад тренувань,
4 - вартість тренування. Дані зберігати у словниках.
Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури
у відповідному пункті меню. Якщо ключ не буде знайдений, створити
відповідний клас-Exception, який буде викликатися в обробнику виключень.
"""

from datetime import time


class Schedule:
    """
    Stores schedule in dictionary <_schedule>
    e.g.: sh = Schedule({'mon': time(17,30), 'thu': time(19)}) ->
    {'mon': 17:30:00, 'thu': 19:00:00}
    """

    DAYS = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

    def __init__(self, schedule: dict):
        self._schedule = self._is_valid_schedule(schedule)

    def __str__(self):
        string = ''
        for day, time_val in self._schedule.items():
            string += f'{str(day)}: {str(time_val)}\n'
        return string

    @classmethod
    def _is_valid_schedule(cls, schedule: dict) -> dict:
        if type(schedule) != dict:
            raise TypeError("Schedule must be dict")

        # check day values
        for day in schedule.keys():
            if day not in cls.DAYS:
                raise KeyError(f"Days must be in format {cls.DAYS}, str type")

        # check time values
        for time_val in schedule.values():
            if not isinstance(time_val, time):
                raise ValueError("Incorrect time value")

        return schedule

    @property
    def schedule(self) -> dict:
        return self._schedule

    @schedule.setter
    def schedule(self, val: dict):
        self._schedule = self._is_valid_schedule(val)

    def update_day(self, val: dict):
        """Add/overwrite time on a certain day in the schedule"""

        val = self._is_valid_schedule(val)
        self._schedule.update(val)

    def del_day(self, day: str):
        """Delete day from the schedule"""

        if day not in self.DAYS:
            raise KeyError(f"Day must be in format {self.DAYS}, str type")
        del self._schedule[day]


# test
if __name__ == '__main__':
    s = Schedule({'mon': time(17), 'thu': time(19)})
    print(s)

    s.update_day({'sat': time(20, 30), 'mon': time(17, 30)})
    print(s)

    s.del_day('sat')
    print(s)
