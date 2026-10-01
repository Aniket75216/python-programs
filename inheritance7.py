# Shape hierarchical inheritance

class Shape:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Shape:", self.name)


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius


class Rectangle(Shape):
    def area(self, length, breadth):
        return length * breadth


class Triangle(Shape):
    def area(self, base, height):
        return 0.5 * base * height


Circle("Circle").display_name()
print("Circle Area:", Circle("Circle").area(5))

Rectangle("Rectangle").display_name()
print("Rectangle Area:", Rectangle("Rectangle").area(10, 5))

Triangle("Triangle").display_name()
print("Triangle Area:", Triangle("Triangle").area(10, 6))\n