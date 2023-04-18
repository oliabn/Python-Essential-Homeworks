"""Task7
Створіть ієрархію класів транспортних засобів. У загальному класі опишіть
загальні всім транспортних засобів поля, у спадкоємцях – специфічні їм.
Створіть кілька екземплярів.
Виведіть інформацію щодо кожного транспортного засобу.
"""


class Vehicle:
    _DRIVING_STEPS = {'drive': ['forward', 'back'],
                      'turn': ['left', 'right']}

    def __init__(self, name):
        self.name = name

    @classmethod
    def _validate_driving_step(cls, step):
        if step not in cls._DRIVING_STEPS.keys():
            raise ValueError(f"Incorrect step. Available steps {cls._DRIVING_STEPS}")

    @classmethod
    def _validate_driving_direction(cls, step, direction):
        if direction not in cls._DRIVING_STEPS[step]:
            raise ValueError(f"Incorrect direction. Available direction{cls._DRIVING_STEPS[step]}")

    def drive(self, step, direction):
        self._validate_driving_step(step)
        self._validate_driving_direction(step, direction)
        print(f"The {self.name} {step} {direction}")


# test
if __name__ == "__main__":
    car = Vehicle('Car')
    car.drive('drive', 'forward')
    car.drive('turn', 'right')
