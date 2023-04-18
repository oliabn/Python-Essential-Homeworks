"""Task7
Створіть ієрархію класів транспортних засобів. У загальному класі опишіть
загальні всім транспортних засобів поля, у спадкоємцях – специфічні їм.
Створіть кілька екземплярів.
Виведіть інформацію щодо кожного транспортного засобу.
"""


class UAVParameter:
    """Class to validate that parameter is a number"""

    @staticmethod
    def _is_number(val):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{val} isn't a number")


class Speed(UAVParameter):
    """
    Speed
    max_speed - maximum speed, km/h
    current_speed - current speed, km/h
    """

    def __init__(self, max_speed):
        self._is_number(max_speed)

        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def max_speed(self):
        return self._max_speed

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, speed):
        self._is_number(speed)
        if speed <= self._max_speed:
            self._current_speed = speed
        else:
            print(f"Speed wasn't set {speed}. The max speed: {self._max_speed} km/h")


class FlightRange(UAVParameter):
    """
    Flight range
    max_flight_range - maximum flight range, km
    current_flight_range - how far the UAV is from the starting point now, km
    """

    def __init__(self, max_flight_range):
        self._is_number(max_flight_range)

        self._max_flight_range = max_flight_range
        self._current_flight_range = 0

    @property
    def max_flight_range(self):
        return self._max_flight_range

    @property
    def current_flight_range(self):
        return self._current_flight_range

    @current_flight_range.setter
    def current_flight_range(self, flight_range):
        self._is_number(flight_range)
        if flight_range > self._max_flight_range:
            print(f"Increased flight range, max value: {self._max_flight_range} km. Will return back. ")
        self._current_flight_range = flight_range

    def has_connection(self):
        if self._current_flight_range > self._max_flight_range:
            print("No connection. Increased flight range. Will return back")
            return False
        return True


class FlightHeight(UAVParameter):
    """
    Flight height
    max_height - maximum flight height, m
    current_height - current flight height, m
    """

    def __init__(self, max_height):
        self._is_number(max_height)

        self._max_height = max_height
        self._current_height = 0

    @property
    def max_height(self):
        return self._max_height

    @property
    def current_height(self):
        return self._current_height

    @current_height.setter
    def current_height(self, height):
        self._is_number(height)
        if height > self._max_height:
            print(f"Dangerous height, max value {self._max_height} m. Lower the height")
        self._current_height = height

    def has_connection(self):
        if self._current_height > self._max_height:
            print("No connection. Dangerous height, lower the height")
            return False
        return True


class FlightDuration(UAVParameter):
    """
    Flight Duration
    max_flight_duration - maximum flight duration, h
    current_flight_duration - how many hours has the UAV been flying at the moment, h
    """

    def __init__(self, max_flight_duration):
        self._is_number(max_flight_duration)

        self._max_flight_duration = max_flight_duration
        self._current_flight_duration = 0

    @property
    def max_flight_duration(self):
        return self._max_flight_duration

    @property
    def current_flight_duration(self):
        return self._current_flight_duration

    @current_flight_duration.setter
    def current_flight_duration(self, flight_duration):
        self._is_number(flight_duration)
        if flight_duration < self._max_flight_duration:
            self._current_flight_duration = flight_duration
        else:
            print(f"The max flight duration {self._max_flight_duration} hours. The flight is over")
