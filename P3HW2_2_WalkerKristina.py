# Kristina Walker
# October 5, 2026
# P3HW2 Assignment
# Use if/elf statement to collect a calculation of hourly salary for a given number of hours worked and hourly pay rate.

import streamlit as st

# Make a title on our UI
# Directly paste the emoji character

st.title("💰Weekly Paycheck Calcutator💰")

# Get employee name
employee_name = st.text_input("Enter employee name")


# Get number of hours worked
hours_worked = st.number_input("Enter hours worked for one week:")

# Get regular pay rate
reg_pay_rate = st.number_input("Enter base pay rate: ")

# If statement for HAVING OVERTIME
if hours_worked > 40:
    OT_hours = hours_worked - 40
    OT_pay = OT_hours * (reg_pay_rate * 1.5)
    reg_pay = reg_pay_rate * 40
    gross_pay = OT_pay + reg_pay
# If hours worked are less than or equal to 40
else:
    OT_hours = 0
    OT_pay = 0
    reg_pay = hours_worked * reg_pay_rate
    gross_pay = reg_pay
    
# Display results
st.write(f"Employee Name: {employee_name}")
st.write()
st.write(f"Hours Worked: {hours_worked}")
st.write(f"Pay Rate: ${reg_pay_rate:.2f}")
st.write(f"Overtime Hours: {OT_hours}")
st.write(f"Overtime Pay: ${OT_pay:.2f}")
st.write(f"RegHour Pay: ${reg_pay:.2f}")
st.write(f"Gross Pay: ${gross_pay:.2f}")
st.write()


