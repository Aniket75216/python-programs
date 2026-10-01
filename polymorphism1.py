# Shape area polymorphism

import math

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        return math.pi * 5 * 5


class Rectangle(Shape):
    def area(self):
        return 10 * 5


class Triangle(Shape):
    def area(self):
        return 0.5 * 10 * 6


for shape in [Circle(), Rectangle(), Triangle()]:
    print("Area:", shape.area())\n