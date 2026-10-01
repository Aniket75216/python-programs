# QUESTION 14
# Dataset: patients.csv
# Columns:
# Patient_ID, Name, Age, Gender, Disease, Medical_Expense
#
# Read the CSV file and:
# 1. Display patients above 60 years.
# 2. Calculate average medical expense.
# 3. Find patient with highest medical expense.
# 4. Count patients for each disease.
# 5. Display patients whose medical expense exceeds 50,000.
# ============================================================

df = pd.read_csv("patients.csv")

print("\nQUESTION 14")

print("\nPatients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage medical expense:")
print(df["Medical_Expense"].mean())

print("\nPatient with highest medical expense:")
print(df.loc[df["Medical_Expense"].idxmax()])

print("\nNumber of patients for each disease:")
print(df["Disease"].value_counts())

print("\nPatients with medical expense greater than 50000:")
print(df[df["Medical_Expense"] > 50000])


# ============================================================
