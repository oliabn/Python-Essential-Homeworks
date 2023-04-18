"""Task3
Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким
засобом інкапсуляції, як властивості. Ознайомтеся з декоратором property.
Створіть клас, що описує температуру і дозволяє задавати та отримувати
температуру за шкалою Цельсія та Фаренгейта,
причому дані можуть бути задані в одній шкалі, а отримані в іншій.
"""


class Temperature:
    """Temperature with param:
    _celsius - temperature in Celsius.
    _fahrenheit - temperature in Fahrenheit
    """

    def __init__(self, celsius=None, fahrenheit=None):
        self._celsius, self._fahrenheit = self._get_args_for_init(celsius, fahrenheit)

    def __str__(self):
        return f'°C: {self._celsius}, °F: {self._fahrenheit}'

    @classmethod
    def _get_args_for_init(cls, celsius, fahrenheit):
        """Checks that only one of the arguments (Celsius or Fahrenheit)
        was given in __init__, count the undefined arg, and returns both"""

        if not celsius and not fahrenheit:
            raise TypeError("__init__() missing 1 required positional argument, c=celsius or f=fahrenheit")
        if celsius and fahrenheit:
            raise TypeError("__init__() missing 1 required positional argument, c=celsius or f=fahrenheit")
        if celsius and not fahrenheit:
            cls._is_number(celsius)
            return celsius, cls._convert_to_fahrenheit(celsius)
        if fahrenheit and not celsius:
            cls._is_number(fahrenheit)
        return cls._convert_to_celsius(fahrenheit), fahrenheit

    @staticmethod
    def _is_number(val):
        if not isinstance(val, (int, float)):
            raise TypeError("Incorrect temperature type. Temperature must be int or float.")

    @staticmethod
    def _convert_to_fahrenheit(celsius):
        return round(1.8*celsius+32, 1)

    @staticmethod
    def _convert_to_celsius(fahrenheit):
        return round(0.55*(fahrenheit-32), 1)

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, val):
        self._is_number(val)
        self._celsius = val
        self._fahrenheit = self._convert_to_fahrenheit(val)

    @property
    def fahrenheit(self):
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, val):
        self._is_number(val)
        self._fahrenheit = val
        self._celsius = self._convert_to_celsius(val)


# test
if __name__ == '__main__':
    t = Temperature(20)
    print(t)

    t.celsius = -40
    print(t)

    t.fahrenheit = 95
    print(t)
    print()

    t = Temperature(fahrenheit=70)
    print(t)
