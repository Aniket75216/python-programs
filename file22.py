# Merge contents of two text files

file1 = input("Enter first file: ")
file2 = input("Enter second file: ")
output_file = input("Enter output file: ")

with open(file1, "r") as first:
    text1 = first.read()

with open(file2, "r") as second:
    text2 = second.read()

with open(output_file, "w") as output:
    output.write(text1)
    output.write("\n")
    output.write(text2)

print("Files merged successfully.")\n