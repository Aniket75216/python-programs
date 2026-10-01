# Count total lines in a text file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))\n