#Write a PYTHON program to print the multiplication table
n = int(input("Enter a number: "))

print("Multiplication Table of", n)

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
#Write a PYTHON program to print the largest of n numbers
n = int(input("Enter how many numbers: "))

largest = float('-inf')

for i in range(n):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num

print("Largest number =", largest)
#Write a PYTHON program to print smallest of n numbers
n = int(input("Enter how many numbers: "))

smallest = float('inf')

for i in range(n):
    num = int(input("Enter a number: "))
    if num < smallest:
        smallest = num

print("Smallest number =", smallest)