#write_pythong_program_to_print_natural_numbers
n=int(input("Enter a number: "))
for i in range(0,n+1):
    print(i)

#write_pythong_program_to_print_even_numbers
n = int(input("Enter a number: "))

print("Even numbers up to", n, "are:")

for i in range(2, n + 1, 2):
    print(i)

#write_pythong_program_to_print_odd_numbers
n = int(input("Enter a number: "))

print("Even numbers up to", n, "are:")

for i in range(1, n + 1, 2):
    print(i)

#write_pythong_program_to_print_1_2_4_8_16_32..n**2
n = int(input("Enter the value of n: "))

limit = n ** 2

for i in range(limit + 1):
    value = 2 ** i
    if value <= limit:
        print(value, end=" ")
    else:
        break
#Write a PYTHON program to sum the given sequence1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!
n = int(input("Enter the value of n: "))

sum = 1
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum of the series =", sum)

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

#Write a PYTHON program to produce following designA B C A B C A B C 
for i in range(3):
    for j in range(65, 68):
        print(chr(j), end=" ")
    print()

#9.  Write a PYTHON program to produce following design
#      A
#     A B
#    A B C
#      A B C D 
#      A B C D E
#      If user enters n value as 5
n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#. Write a PYTHON program to produce following design
#       A B C D E
#       A B C D
#       A B C
#       A B
#       A                      
#      (If user enters n value as 5)
n = int(input("Enter the value of n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#11. Write a PYTHON program to produce following  
#      design
#      1
#      1 2
#      1 2 3
#      1 2 3 4
#      1 2 3 4 5
#      If user enters n value as 5
n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#12. Write a PYTHON program to produce following design
#     1
#      2 2
#      3 3 3
#      4 4 4 4 
#      5 5 5 5 5
#      If user enters n value as 5    
n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()




