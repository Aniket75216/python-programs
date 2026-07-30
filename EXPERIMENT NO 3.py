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
