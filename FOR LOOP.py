#Write a PYTHON program to print the natural numbers up to n
n = int(input("Enter the value of n: "))

print("Natural numbers up to", n, "are:")

for i in range(1, n + 1):
    print(i, end=" ")

#Write a PYTHON program to print even numbers up to n
n = int(input("Enter the value of n: "))

print("Even numbers up to", n, "are:")

for i in range(2, n + 1, 2):
    print(i, end=" ")

#Write a PYTHON program to print odd numbers up to n
n = int(input("Enter the value of n: "))

print("Odd numbers up to", n, "are:")

for i in range(1, n + 1, 2):
    print(i, end=" ")

#Python Program to Print the Sum of Natural Numbers up to n
n = int(input("Enter the value of n: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum of natural numbers =", sum)    