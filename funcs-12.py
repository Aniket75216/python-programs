# 27. Passing Functions as Arguments
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate_operation(operation, a, b):
    return operation(a, b)

print("Addition =", calculate_operation(add, 10, 5))
print("Subtraction =", calculate_operation(subtract, 10, 5))
print("Multiplication =", calculate_operation(multiply, 10, 5))
print("Division =", calculate_operation(divide, 10, 5))


# 28. Lambda - Square
square = lambda x: x * x
print("Square =", square(5))


# 29. Lambda - Cube
cube = lambda x: x ** 3
print("Cube =", cube(3))


# 30. Lambda - Even
even = lambda x: x % 2 == 0
print("Even =", even(10))


# 31. Lambda - Maximum of Two
maximum = lambda a, b: a if a > b else b
print("Maximum =", maximum(10, 20))


# 32. Lambda - Simple Interest
simple_interest = lambda p, r, t: (p * r * t) / 100
print("Simple Interest =", simple_interest(10000, 5, 2))


