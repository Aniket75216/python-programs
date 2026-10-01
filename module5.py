# Employee salary module

import salary_utils

basic = float(input("Enter basic salary: "))

gross = salary_utils.gross_salary(basic)
deduction = salary_utils.deductions(gross)
net = salary_utils.net_salary(gross, deduction)

print("Gross Salary:", gross)
print("Deductions:", deduction)
print("Net Salary:", net)\n