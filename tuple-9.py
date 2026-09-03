#2. Search for a patient by ID
search_id = int(input("Enter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == search_id:
        print("\nPatient Found:")
        print("Patient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True
        break

if not found:
    print("Patient not found.")


# 3. Count total number of patients
print("\nTotal number of patients:", len(patients))


# 4. Display patients with a specific blood group
blood_group = input("\nEnter blood group to search: ")

print("\nPatients with blood group", blood_group, ":")

found = False

for patient in patients:
    if patient[3].upper() == blood_group.upper():
        print("Patient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        print("----------------------")
        found = True

if not found:
    print("No patient found with this blood group.")