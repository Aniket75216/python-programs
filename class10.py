# Vehicle rental calculation

class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, availability=True):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self):
        self.availability = True
        print("Vehicle returned successfully.")

    def rental_charges(self, days):
        return self.rental_rate * days

    def display(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate:", self.rental_rate)
        print("Available:", self.availability)

vehicle = Vehicle("MH12AB1234", "Swift", 1500)

vehicle.display()
vehicle.rent()
print("Rental Charge for 3 days:", vehicle.rental_charges(3))
vehicle.return_vehicle()
