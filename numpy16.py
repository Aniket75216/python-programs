# Calculate statistics of student marks
import numpy as np

marks = np.array([75, 82, 68, 90, 55, 88, 72, 95, 64, 78])

print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Average:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))
