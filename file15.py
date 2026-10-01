# Remove single-line comments from a Python file

source_file = input("Enter Python source file: ")
output_file = input("Enter output file: ")

with open(source_file, "r") as source:
    lines = source.readlines()

with open(output_file, "w") as output:
    for line in lines:
        stripped = line.lstrip()

        if not stripped.startswith("#"):
            output.write(line)

print("Comments removed successfully.")\n