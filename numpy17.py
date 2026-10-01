# Display students scoring above class average
import numpy as np

marks = np.array([55, 72, 81, 65, 90, 76, 68, 84, 59, 95,
                  70, 88, 62, 79, 91, 73, 67, 86, 58, 80])

average = np.mean(marks)

print("Class average:", average)
print("Above average:", marks[marks > average])
