# Abstract authentication

from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Password authentication successful")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("OTP authentication successful")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Biometric authentication successful")


for auth in [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]:
    auth.authenticate()\n