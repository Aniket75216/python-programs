# student package

from student.marks import total, percentage
from student.grade import grade
from student.attendance import eligible

marks = [80, 75, 85, 90, 78]

total_marks = total(marks)
percent = percentage(marks)

print("Total:", total_marks)
print("Percentage:", percent)
print("Grade:", grade(percent))
print("Attendance Eligible:", eligible(80))\n