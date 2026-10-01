# mathutils package

from mathutils.basic import add, subtract, multiply, divide
from mathutils.number import is_prime, is_armstrong, is_palindrome
from mathutils.statistics import mean, maximum, minimum

a = 10
b = 5
numbers = [10, 20, 30, 40, 50]

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
print("Prime:", is_prime(7))
print("Armstrong:", is_armstrong(153))
print("Palindrome:", is_palindrome(121))
print("Mean:", mean(numbers))
print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))\n