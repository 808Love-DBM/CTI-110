# Kristina Walker
# September 28, 2026
# P3HW1 Assignment
# This program asks users to enter their test grades for 6 different modules and it gives their result from lowest to highest, as well as the average of all their grades.
# We will be using Branching to find the average
print() #I'm putting these for space
print() #I'm putting these for space
# Ask the user to enter their grades for 6 different modules
module1 = float(input("Enter your grade for module 1: "))
module2 = float(input("Enter your grade for module 2: "))
module3 = float(input("Enter your grade for module 3: "))
module4 = float(input("Enter your grade for module 4: "))
module5 = float(input("Enter your grade for module 5: "))
module6 = float(input("Enter your grade for module 6: "))
print() #I'm putting these for space
# Add the grades to a list
grades = [module1, module2, module3, module4, module5, module6]
# find the lowest grade
lowest_grade = min(grades)
# find the highest grade
highest_grade = max(grades)
# find sum of the grades
total_grades = sum(grades)
# calculate the average
average_grade = sum(grades) / len(grades)
# Display the results
print("---------------Grade Summary---------------")
print() #I'm putting these for space
print(f"{'Lowest Grade:':<20}{lowest_grade}")
print(f"{'Highest Grade:':<20}{highest_grade}")
print(f"{'Sum of Grades:':<20}{total_grades}")
print(f"{'Average Grade:':<20}{average_grade:.2f}")
print() #I'm putting these for space

# Determine the letter grade based on the average_grade
if average_grade >= 90:
    letter_grade = "A"
if average_grade >= 80 and average_grade <= 89:
    letter_grade = "B"
if average_grade >= 70 and average_grade <= 79:
    letter_grade = "C"
if average_grade >= 60 and average_grade <= 69:
    letter_grade = "D"
if average_grade <= 60:
    letter_grade = "F"
print("--------------Final Results----------------")
# Display letter grade to user
print()
print(f"Your letter grade is: {letter_grade}")