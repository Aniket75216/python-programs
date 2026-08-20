# Program to implement Rail Fence Cipher Encryption

text = input("Enter the message: ")
rails = int(input("Enter the number of rails: "))

fence = ['' for _ in range(rails)]

rail = 0
direction = 1

for ch in text:
    fence[rail] += ch

    if rail == 0:
        direction = 1
    elif rail == rails - 1:
        direction = -1

    rail += direction

cipher = ""

for row in fence:
    cipher += row

print("Encrypted Message:", cipher)