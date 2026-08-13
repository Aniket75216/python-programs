patients = ["Ram", "Shyam", "Amit"]

patients.append("Ravi")      # Add Patient

name = input("Enter patient name to search: ")
if name in patients:
    print("Patient Found")
else:
    print("Patient Not Found")

patients.remove("Shyam")     # Delete Patient

print("Patients List:", patients)
print("Total Patients:", len(patients))