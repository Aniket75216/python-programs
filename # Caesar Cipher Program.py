# Caesar Cipher Program

text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
choice = input("Type 'e' for Encrypt or 'd' for Decrypt: ")

result = ""

if choice.lower() == 'd':
    shift = -shift

for char in text:
    if char.isalpha():
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        result += char

if choice.lower() == 'e':
    print("Encrypted Message:", result)
elif choice.lower() == 'd':
    print("Decrypted Message:", result)
else:
    print("Invalid choice!")