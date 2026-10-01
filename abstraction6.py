# Abstract transport fare

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 3


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 20


for transport in [Bus(), Train(), Taxi(), Flight()]:
    print("Fare:", transport.calculate_fare(100))\n