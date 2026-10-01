# Append student information to an existing file

filename = input("Enter file name: ")

with open(filename, "a") as file:
    file.write("\nAdditional Student Information")
    file.write("\nPhone: 9876543210")

print("Information appended successfully.")\n