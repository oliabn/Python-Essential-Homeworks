"""Task3
Створіть ієрархію класів із використанням множинного успадкування.
Виведіть на екран порядок вирішення методів для кожного класу.
Поясніть, чому лінеаризація даних класів виглядає саме так.
"""


class Salary:
    def __init__(self, monthly_rate, overtime_rate=0, overtime_hours=0):
        self._is_number(monthly_rate)
        self._is_number(overtime_rate)
        self._is_number(overtime_hours)

        self._monthly_rate = monthly_rate
        self._overtime_rate = overtime_rate
        self._overtime_hours = overtime_hours

    @staticmethod
    def _is_number(value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{value} is {type(value)} but must be int or float")

    @property
    def monthly_rate(self):
        return self._monthly_rate

    @monthly_rate.setter
    def monthly_rate(self, value):
        self._is_number(value)
        self._monthly_rate = value

    @property
    def salary(self):
        return self._monthly_rate + self._overtime_rate*self._overtime_hours

    @property
    def overtime_rate(self):
        return self._overtime_rate

    @overtime_rate.setter
    def overtime_rate(self, value):
        self._is_number(value)
        self._overtime_rate = value

    @property
    def overtime_hours(self):
        return self._overtime_hours

    @overtime_hours.setter
    def overtime_hours(self, value):
        self._is_number(value)
        self._overtime_hours = value
