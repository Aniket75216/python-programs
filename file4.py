# Read a text file line by line

filename = input("Enter file name: ")

with open(filename, "r") as file:
    for line in file:
        print(line.strip())\n