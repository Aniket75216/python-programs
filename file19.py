# Calculate student attendance percentage

filename = "attendance.txt"

records = [
    "101,Amit,100,80",
    "102,Rahul,100,70",
    "103,Sneha,90,85"
]

with open(filename, "w") as file:
    for record in records:
        file.write(record + "\n")

with open(filename, "r") as file:
    for line in file:
        roll, name, total, attended = line.strip().split(",")

        percentage = (int(attended) / int(total)) * 100

        print(name, "Attendance:", percentage, "%")

        if percentage < 75:
            print("Below 75%")\n