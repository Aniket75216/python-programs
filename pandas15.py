# QUESTION 15
# Dataset: weather.csv
# Columns:
# Date, City, Temperature, Humidity, Rainfall
#
# Read the CSV file and:
# 1. Find maximum temperature.
# 2. Find minimum temperature.
# 3. Calculate average temperature.
# 4. Display records where temperature is above 35°C.
# 5. Calculate city-wise average temperature.
# ============================================================

df = pd.read_csv("weather.csv")

print("\nQUESTION 15")

print("\nMaximum Temperature:")
print(df["Temperature"].max())

print("\nMinimum Temperature:")
print(df["Temperature"].min())

print("\nAverage Temperature:")
print(df["Temperature"].mean())

print("\nRecords where temperature is above 35°C:")
print(df[df["Temperature"] > 35])

print("\nCity-wise average temperature:")
print(df.groupby("City")["Temperature"].mean())


# ============================================================
# END OF PANDAS PRACTICAL PROGRAMS
# ============================================================
