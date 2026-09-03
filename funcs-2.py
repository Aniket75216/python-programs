# 1. Area of a Circle
def area_circle(r):
    return 3.14 * r * r

r = float(input("Enter radius: "))
print("Area =", area_circle(r))


# 2. Sum of First n Natural Numbers
def sum_n(n):
    return n * (n + 1) // 2

n = int(input("Enter n: "))
print("Sum =", sum_n(n))


# 3. Power of a Number
def power(base, exponent):
    return base ** exponent

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Result =", power(base, exponent))


# 4. Largest Element Without max()
def largest(numbers):
    large = numbers[0]
    for x in numbers:
        if x > large:
            large = x
    return large

numbers = [10, 25, 7, 45, 18]
print("Largest =", largest(numbers))


# 5. Count Vowels
def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count

text = input("Enter string: ")
print("Number of vowels =", count_vowels(text))


