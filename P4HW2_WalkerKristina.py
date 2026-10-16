# Kristina Walker
#October 22, 2026
# P4HW2 Assignment
# Salary calculation with loops

print() # Display for space
# Set up terminal text color formatting for "name". 
RED = "\033[91m" # ANSI code for red
RESET = "\033[0m" # ANSI code to reset color

# request employee info
name = input("Enter employee name or 'done' to finish: ")

# Create Accumulator variables for overtime pay, regular pay, gross pay, and employee count
overtime_pay_total = 0
regular_pay_total = 0       
gross_pay_total = 0
employee_count = 0

while name != 'done':
    # Add employee count plus one
    employee_count += 1 # employee_count = employee_count + 1
    # Ask for employee indo
    hours_worked = float(input("How many hours did " +name+ " work this week?  "))
    hourly_rate = float(input("What is " +name+ "'s hourly pay rate?  "))

    # Calculate pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (hourly_rate * 1.5)
        regular_pay = 40 * hourly_rate
        gross_pay = regular_pay + overtime_pay
    else:   
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * hourly_rate
        gross_pay = regular_pay
    
    # Add to accumulator variables
    overtime_pay_total += overtime_pay
    regular_pay_total += regular_pay
    gross_pay_total += gross_pay

    # Display results
    print()
    print(f"Employee Name: {RED}{name}{RESET}")
    print(f"{"Hours Worked":<15}{"Hourly Rate":<15}{"Overtime Hours":<18}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<15}")
    print(f"{'------------':<15}{'------------':<15}{'--------------':<18}{'------------':<15}{'-----------':<15}{'-------------':<15}")
    print(f"{hours_worked:<15.1f}{hourly_rate:<15.2f}{overtime_hours:<18.1f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}")
    print("-" * 91)
    print() # Display for space

    name = input("Enter employee name or 'done' to finish: ")

print("Total number of employees entered:", employee_count)
print("Total amount paid for overtime: $", format(overtime_pay_total, ',.2f'))
print("Total amount paid for regular pay: $", format(regular_pay_total, ',.2f'))
print("Total amount paid for gross pay: $", format(gross_pay_total, ',.2f'))
print()

# I know I'm so extra '_'.  I'm jsut so amazed by what programming can do.  I love it!