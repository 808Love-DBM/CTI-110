# Kristina Walker
# October 3, 2026
# P3HW2 Assignment
# A calculation of hourly salary for a given number of hours worked and hourly pay rate.
print() # Display for space
# request employee info
name = input("Enter employee name: ")
hours_worked = float(input("Enter number of hours worked: "))
hourly_rate = float(input("Enter hourly pay rate: "))
# Evaluate overtime pay
if hours_worked > 40:
    # calculate overtime hours
    overtime_hours = hours_worked - 40
    # calculate overtime pay
    overtime_pay = overtime_hours * (hourly_rate * 1.5)
    # calculate salary regular hours
    regular_pay = 40 * hourly_rate
    # calcutate gross pay
    gross_pay = regular_pay + overtime_pay
else: 
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * hourly_rate
    gross_pay = regular_pay
# Display results
print("-" * 35)
print("Employee Name:", name)
print() # Display for space
print(f"{"Hours Worked":<15}{"Hourly Rate":<15}{"Overtime Hours":<18}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<15}")
print(f"{'------------':<15}{'------------':<15}{'--------------':<18}{'------------':<15}{'-----------':<15}{'-------------':<15}")

print(f"{hours_worked:<15}{hourly_rate:<15}{overtime_hours:<18}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}")
print() # Display for space