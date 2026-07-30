#Write a PYTHON program to print sum of odd numbers up to n
n = int(input("Enter the value of n: "))

sum = 0

for i in range(1, n + 1, 2):
    sum = sum + i

print("Sum of odd numbers =", sum)
#Write a PYTHON program to print sum of even numbers up to n
n = int(input("Enter the value of n: "))

sum = 0

for i in range(2, n + 1, 2):
    sum = sum + i

print("Sum of even numbers =", sum)
#Write a PYTHON program to print natural numbers up to n in reverse order.
n = int(input("Enter the value of n: "))

print("Natural numbers in reverse order:")

for i in range(n, 0, -1):
    print(i, end=" ")
#Write a PYTHON program to print Fibonacci series up to n
n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
#Write a PYTHON program  find a factorial of given number
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)