# Distance operator overloading

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.feet * 12 + self.inches
        total_inches += other.feet * 12 + other.inches

        return Distance(total_inches // 12, total_inches % 12)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(3, 6)

d3 = d1 + d2
d3.display()\n