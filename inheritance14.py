# Camera and Phone multiple inheritance

class Camera:
    def take_photo(self):
        print("Photo taken")


class Phone:
    def make_call(self):
        print("Calling...")


class Smartphone(Camera, Phone):
    pass


phone = Smartphone()
phone.take_photo()
phone.make_call()\n