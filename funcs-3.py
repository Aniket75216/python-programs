# 6. Reverse a String
def reverse_string(text):
    return text[::-1]

text = input("Enter string: ")
print("Reverse =", reverse_string(text))


# 7. Palindrome
def palindrome(value):
    value = str(value)
    return value == value[::-1]

value = input("Enter string or number: ")
print("Palindrome" if palindrome(value) else "Not Palindrome")


# 8. Average of List
def average(numbers):
    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]
print("Average =", average(numbers))


# 9. Count Occurrences
def count_element(numbers, element):
    count = 0
    for x in numbers:
        if x == element:
            count += 1
    return count

numbers = [10, 20, 10, 30, 10, 40]
element = int(input("Enter element: "))
print("Occurrences =", count_element(numbers, element))


# 10. Unique Elements
def unique_elements(numbers):
    result = []
    for x in numbers:
        if x not in result:
            result.append(x)
    return result

numbers = [10, 20, 10, 30, 20, 40]
print("Unique elements =", unique_elements(numbers))


