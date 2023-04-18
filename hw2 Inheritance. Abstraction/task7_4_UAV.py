"""Task7
Створіть ієрархію класів транспортних засобів. У загальному класі опишіть
загальні всім транспортних засобів поля, у спадкоємцях – специфічні їм.
Створіть кілька екземплярів.
Виведіть інформацію щодо кожного транспортного засобу.
"""

from task7_2_aircraft import Aircraft
from task7_3_UAV_parameters import Speed, FlightRange, FlightHeight, FlightDuration, UAVParameter


class UAV(Aircraft):
    """
    UAV with param:
    name, model
    weigh (take-off weight), kg
    wingspan, m
    max_speed, km/h
    max_flight_range, km
    max_flight_height, m
    max_flight_duration, h
    """

    def __init__(self,
                 name: str, model: str,
                 weight: (float, int),
                 wingspan: (float, int),
                 max_speed: (float, int),
                 max_flight_range: (float, int),
                 max_flight_height: (float, int),
                 max_flight_duration: (float, int)):

        UAVParameter._is_number(weight)
        UAVParameter._is_number(wingspan)

        super().__init__(name)
        self.model = model
        self.weight = weight
        self.wingspan = wingspan
        self.speed = Speed(max_speed)
        self.flight_range = FlightRange(max_flight_range)
        self.height = FlightHeight(max_flight_height)
        self.flight_duration = FlightDuration(max_flight_duration)

    def __str__(self):
        return f"{self.name} {self.model}\n" \
               f"Weight: {self.weight} kg\n" \
               f"Wingspan: {self.wingspan} m\n" \
               f"Max speed: {self.speed.max_speed} km/h\n" \
               f"Max flight range: {self.flight_range.max_flight_range} km\n" \
               f"Max flight height: {self.height.max_height} m\n" \
               f"Max flight duration: {self.flight_duration.max_flight_duration} h"

    def check_connection(self):
        if self.height.has_connection() and self.flight_range.has_connection():
            print("There is a connection")


# test
if __name__ == "__main__":

    leleka = UAV('Leleka', '100', 5.5, 1.98, 120, 100, 1500, 2.5)
    print(leleka)
    print()

    sokil = UAV('Sokil', '300', 1220, 14, 580, 1300, 11, 5)
    print(sokil)
    print()

    leleka.fly('take-off', 'up')
    leleka.fly('fly', 'forward')
    leleka.speed.current_speed = 121
    leleka.speed.current_speed = 100
    leleka.height.current_height = 1000
    print("Current height:", leleka.height.current_height)
    leleka.flight_range.current_flight_range = 120
    leleka.fly('turn', 'right')
    leleka.check_connection()
    leleka.fly('turn', 'right')
    leleka.flight_range.current_flight_range = 90
    leleka.check_connection()
