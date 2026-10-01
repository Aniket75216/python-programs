# Vehicle start polymorphism

class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with button")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with engine")


for vehicle in [Car(), Bike(), Bus()]:
    vehicle.start()\n