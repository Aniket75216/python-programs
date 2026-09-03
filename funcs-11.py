# 24. Recursive Binary Search
def binary_search(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)

arr = [10, 20, 30, 40, 50]
key = int(input("Enter element: "))

result = binary_search(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")


# 25. Decimal to Binary Using Recursion
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

n = int(input("Enter decimal number: "))

if n == 0:
    print("Binary = 0")
else:
    print("Binary =", decimal_to_binary(n))


# 26. Palindrome Using Recursion
def recursive_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return recursive_palindrome(text[1:-1])

text = input("Enter string: ")

if recursive_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")


