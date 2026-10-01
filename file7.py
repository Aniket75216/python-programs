# Count characters including spaces

filename = input("Enter file name: ")

with open(filename, "r") as file:
    text = file.read()

print("Total number of characters:", len(text))\n