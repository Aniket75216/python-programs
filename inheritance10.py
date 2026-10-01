# Combination of inheritance types

class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def drive(self):
        print(self.brand, "Car is driving")


class Bike(Vehicle):
    def ride(self):
        print(self.brand, "Bike is riding")


class SportsCar(Car):
    def speed(self):
        print(self.brand, "Sports car is fast")


class ElectricBike(Bike):
    def battery(self):
        print(self.brand, "Electric bike uses battery")


SportsCar("BMW").speed()
ElectricBike("Ola").battery()\n