# QUESTION 4
# Create a dictionary containing Patient ID, Patient Name,
# Age, Disease and Medical Charges.
# Convert it into a DataFrame and:
# 1. Display patients above 60 years.
# 2. Find average medical charge.
# 3. Find maximum medical charge.
# 4. Display patients whose medical charges are greater
#    than 50,000.
# ============================================================

patients = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Amit", "Sunita", "Rahul", "Meena", "Ravi"],
    "Age": [65, 45, 70, 30, 62],
    "Disease": ["Diabetes", "Fever", "Heart", "Cold", "Diabetes"],
    "Medical_Charges": [60000, 25000, 85000, 15000, 55000]
}

df = pd.DataFrame(patients)

print("\nQUESTION 4")
print(df)

print("\nPatients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage medical charge:")
print(df["Medical_Charges"].mean())

print("\nMaximum medical charge:")
print(df["Medical_Charges"].max())

print("\nPatients with medical charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])


# ============================================================
