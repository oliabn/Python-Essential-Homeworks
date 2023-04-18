""" Task1
Створіть клас, який описує автомобіль.
Які атрибути та методи мають бути повністю інкапсульовані?
Доступ до таких атрибутів та зміну даних реалізуйте через методи (get, set).
"""

from task1_1_vehicle import Vehicle


class Car(Vehicle):
    """
    Car with param: brand, model, _transmission, engine, _fuel, color
    methods: drive('step', 'direction'), stop()
    """

    _TRANSMISSION = ['manual', 'automatic', 'semi-automatic']
    _FUEL = ['petrol', 'diesel', 'cng', 'electricity', 'hybrid']

    def __init__(self, brand: str, model: str, transmission: str,
                 engine: str, fuel: str, color: str):
        self.brand = brand
        self.model = model
        self._transmission = self._verify_trn(transmission)
        self.engine = engine
        self._fuel = self._verify_fuel(fuel)
        self.color = color

    def __str__(self):
        return f"{self.brand}, {self.model}\n" \
               f"transmission: {self._transmission}\n" \
               f"engine: {self.engine}\n" \
               f"fuel: {self._fuel}\n" \
               f"color: {self.color}"

    @classmethod
    def _verify_trn(cls, trn_val):
        if trn_val not in cls._TRANSMISSION:
            raise ValueError("Not set. There is no such type of transmission.\n"
                  f"Choose from these: {cls._TRANSMISSION}")
        return trn_val

    @classmethod
    def _verify_fuel(cls, fuel_val):
        if fuel_val not in cls._FUEL:
            raise ValueError("Not set. There is no such type of fuel.\n"
                  f"Choose from these: {cls._FUEL}")
        return fuel_val

    @property
    def transmission(self):
        return self._transmission

    @transmission.setter
    def transmission(self, trn_val):
        self._transmission = self._verify_trn(trn_val)

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, fuel_val):
        self._fuel = self._verify_fuel(fuel_val)

    def drive(self, step, direction):
        self._verify_driving_direction(step, direction)
        self._verify_driving_step(step)
        print(f"{self.color} {self.brand} {step} {direction}")

    def stop(self):
        print(f"{self.color} {self.brand} was stopped")


# test
if __name__ == '__main__':
    range_rover = Car('Land Rover', 'Range Rover EVOQUE', 'automatic', 'D200', 'petrol', 'Blue')
    tesla = Car('Tesla', 'Y', 'automatic', 'AWD', 'electricity', 'Black')

    range_rover.fuel = 'cng'

    print(range_rover)
    print()

    print(tesla)
    print()

    tesla.drive('drive', 'forward')
    range_rover.drive('turn', 'right')
    tesla.stop()
