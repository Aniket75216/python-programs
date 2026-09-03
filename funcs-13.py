# 33. map() - Squares
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * x, numbers))
print("Squares =", result)


# 34. map() - Cubes
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 3, numbers))
print("Cubes =", result)


# 35. map() - Add Corresponding Elements
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
result = list(map(lambda x, y: x + y, a, b))
print("Sum of corresponding elements =", result)


# 36. filter() - Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers =", result)


# 37. filter() - Prime Numbers
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 11, 13]
result = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers =", result)


# 38. filter() - Positive Numbers
numbers = [-5, 10, -2, 8, -1, 20]
result = list(filter(lambda x: x > 0, numbers))
print("Positive numbers =", result)


# 39. filter() - Numbers Greater Than 50
numbers = [20, 55, 70, 30, 90, 45]
result = list(filter(lambda x: x > 50, numbers))
print("Numbers greater than 50 =", result)


