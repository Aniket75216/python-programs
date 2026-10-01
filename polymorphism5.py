# Notification polymorphism

class Notification:
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("Email notification sent")


class SMSNotification(Notification):
    def send(self):
        print("SMS notification sent")


class PushNotification(Notification):
    def send(self):
        print("Push notification sent")


for notification in [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]:
    notification.send()\n