# Animal hierarchical inheritance

class Animal:
    def eat(self):
        print("Animal eats food")


class Dog(Animal):
    def sound(self):
        print("Dog: Bark")


class Cat(Animal):
    def sound(self):
        print("Cat: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow: Moo")


for animal in [Dog(), Cat(), Cow()]:
    animal.eat()
    animal.sound()\n