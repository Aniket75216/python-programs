# QUESTION 10
# Create a Pandas Series using a dictionary where patient IDs
# are the index and patient ages are the values.
# Perform:
# 1. Find average age.
# 2. Find oldest patient.
# 3. Find youngest patient.
# 4. Display patients above 60 years.
# ============================================================

patient_ages = {
    101: 65,
    102: 45,
    103: 70,
    104: 30,
    105: 62
}

series = pd.Series(patient_ages)

print("\nQUESTION 10")
print(series)

print("\nAverage Age:")
print(series.mean())

print("\nOldest Patient:")
print(series.idxmax(), series.max())

print("\nYoungest Patient:")
print(series.idxmin(), series.min())

print("\nPatients above 60 years:")
print(series[series > 60])


# ============================================================
