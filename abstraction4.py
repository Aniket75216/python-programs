# Abstract food order

from abc import ABC, abstractmethod

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 50


for order in [RestaurantOrder(), HomeDeliveryOrder()]:
    print("Bill:", order.calculate_bill())
    print("Delivery:", order.delivery_charge())\n