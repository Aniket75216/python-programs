# Recursive functions module

import recursive_utils

number = int(input("Enter number: "))

print("Factorial:", recursive_utils.factorial(number))
print("Fibonacci:", recursive_utils.fibonacci(number))
print("Sum of digits:", recursive_utils.sum_digits(number))
print("Binary:", recursive_utils.binary(number))\n