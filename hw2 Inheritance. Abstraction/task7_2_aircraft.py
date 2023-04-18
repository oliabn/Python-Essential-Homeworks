"""Task7
Створіть ієрархію класів транспортних засобів. У загальному класі опишіть
загальні всім транспортних засобів поля, у спадкоємцях – специфічні їм.
Створіть кілька екземплярів.
Виведіть інформацію щодо кожного транспортного засобу.
"""

from task7_1_vehicle import Vehicle


class Aircraft(Vehicle):
    _FLYING_STEPS = {'fly': ['forward'],
                     'take-off': ['up'],
                     'land': ['down'],
                     'turn': ['left', 'right']}

    @classmethod
    def _validate_flying_step(cls, step):
        if step not in cls._FLYING_STEPS.keys():
            raise ValueError(f"Incorrect step. Available steps {cls._FLYING_STEPS}")

    @classmethod
    def _validate_flying_direction(cls, step, direction):
        if direction not in cls._FLYING_STEPS[step]:
            raise ValueError(f"Incorrect direction. Available direction{cls._FLYING_STEPS[step]}")

    def fly(self, step, direction):
        self._validate_flying_step(step)
        self._validate_flying_direction(step, direction)
        print(f"The {self.name} {step} {direction}")


# test
if __name__ == "__main__":
    aircraft = Aircraft('Aircraft')
    aircraft.drive('drive', 'forward')
    aircraft.fly('take-off', 'up')
    aircraft.fly('fly', 'forward')
    aircraft.fly('land', 'down')
