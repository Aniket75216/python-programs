# Online payment polymorphism

class Payment:
    def make_payment(self, amount):
        pass


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("UPI payment:", amount)


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Card payment:", amount)


class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Wallet payment:", amount)


def pay(payment, amount):
    payment.make_payment(amount)


for payment in [
    UPIPayment(),
    CardPayment(),
    WalletPayment()
]:
    pay(payment, 1000)\n