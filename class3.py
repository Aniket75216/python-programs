# Rectangle area and perimeter

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

rectangle = Rectangle(10, 5)

print("Length:", rectangle.length)
print("Breadth:", rectangle.breadth)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
