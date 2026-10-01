# Smart device polymorphism

class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        print("Light ON")

    def turn_off(self):
        print("Light OFF")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan ON")

    def turn_off(self):
        print("Fan OFF")


class AC(SmartDevice):
    def turn_on(self):
        print("AC ON")

    def turn_off(self):
        print("AC OFF")


class TV(SmartDevice):
    def turn_on(self):
        print("TV ON")

    def turn_off(self):
        print("TV OFF")


for device in [Light(), Fan(), AC(), TV()]:
    device.turn_on()
    device.turn_off()\n