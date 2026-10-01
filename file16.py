# Create an uppercase copy of a text file

source_file = input("Enter source file: ")
output_file = input("Enter output file: ")

with open(source_file, "r") as source:
    text = source.read()

with open(output_file, "w") as output:
    output.write(text.upper())

print("Uppercase file created successfully.")\n