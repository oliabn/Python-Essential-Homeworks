"""
Task4
Створіть клас, який описує автомобіль. Створіть клас автосалону,
що містить в собі список автомобілів, доступних для продажу, і
функцію продажу заданого автомобіля.
"""


class Car:
    """
    Car with info about it: brand, model, transmission, engine, color
    """

    def __init__(self, brand: str, model: str, transmission: str,
                 engine: str, color: str, price: int):
        self.brand = brand
        self.model = model
        self.transmission = transmission
        self.engine = engine
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.brand}, {self.model}\n" \
               f"transmission: {self.transmission}\n" \
               f"engine: {self.engine}\n" \
               f"color: {self.color}\n" \
               f"price: {self.price}"

    def __repr__(self):
        return f"{self.brand}, {self.model}, price: {self.price}"


class CarDealership:
    """
    CarDealership - the class that contains a dict of available
    for sale cars and a function to sell a given car
    """

    def __init__(self):
        self.cars = {}

    def __str__(self):
        return f"Available cars: {self.cars}"

    def add_car(self, car_name: str,  car: Car):
        """Add cars to dict of available cars, key->car_name, val->Car"""
        self.cars[car_name] = car

    def sell(self, car_name: str):
        """The sold car is removed from the dictionary of available cars"""
        del self.cars[car_name]
        print(f"The car {car_name} was sold")


car_dealership = CarDealership()

# add two cars to car_dealership
car_dealership.add_car('range_rover',
                       Car('Land Rover', 'Range Rover EVOQUE', 'automatic', 'D200', 'Blue', 100000))
car_dealership.add_car('tesla',
                       Car('Tesla', 'Y', 'automatic', 'AWD', 'Black', 150700))
print(car_dealership)
print()

# sell tesla
car_dealership.sell('tesla')
print(car_dealership)
