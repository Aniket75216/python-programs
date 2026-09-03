# 17. Minimum, Maximum, Sum and Average
def calculate(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for x in numbers:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
        total += x

    average = total / len(numbers)
    return minimum, maximum, total, average

numbers = [10, 20, 5, 40, 30]
a, b, c, d = calculate(numbers)

print("Minimum =", a)
print("Maximum =", b)
print("Sum =", c)
print("Average =", d)


