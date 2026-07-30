#Write a PYTHON program to compute the cosine seriescos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))

sum = 1
fact = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    term = (x ** i) / fact
    sum += sign * term
    sign *= -1

print("cos(x) =", sum)

#Write a short PYTHON program to check weather the  square root of number is prime or  not.
import math

n = int(input("Enter a number: "))

root = int(math.sqrt(n))

prime = True

if root < 2:
    prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break

print("Square root =", root)

if prime:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")
