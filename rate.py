# Prompt the user for input
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate per Hour: "))

# Compute gross pay
if hours <= 40:
    gross_pay = hours * rate
else:
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (1.5 * rate)
    gross_pay = regular_pay + overtime_pay

# Print the result
print("Gross Pay:", gross_pay)
