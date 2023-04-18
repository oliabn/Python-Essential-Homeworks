""" Task1
Створіть клас, який описує автомобіль.
Які атрибути та методи мають бути повністю інкапсульовані?
Доступ до таких атрибутів та зміну даних реалізуйте через методи (get, set).
"""


class Vehicle:
    """
    Base class for Car
    Vehicle with methods: drive('step', 'direction'), stop()
    """

    _DRIVING_STEPS = {'drive': ['forward', 'back'],
                      'turn': ['left', 'right']}

    @classmethod
    def _verify_driving_step(cls, step):
        if step not in cls._DRIVING_STEPS.keys():
            raise ValueError(f"Incorrect step. Available steps {cls._DRIVING_STEPS}")
        if step == "drive":
            return "drives"
        elif step == "turn":
            return "turns"

    @classmethod
    def _verify_driving_direction(cls, step, direction):
        if direction not in cls._DRIVING_STEPS[step]:
            raise ValueError(f"Incorrect direction. Available direction{cls._DRIVING_STEPS[step]}")
        return direction

    def drive(self, step, direction):
        direction = self._verify_driving_direction(step, direction)
        step = self._verify_driving_step(step)
        print(f"The vehicle {step} {direction}")

    def stop(self):
        print(f"The vehicle was stopped")


# test
if __name__ == "__main__":
    car = Vehicle()
    car.drive('drive', 'forward')
    car.drive('turn', 'right')
    car.stop()
