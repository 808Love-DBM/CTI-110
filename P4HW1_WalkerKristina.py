# Kristina Walker
# October 19, 2026
# P4HW1
# This program collects scores using loops, validates them, drops the lowest score, and calculates a letter grade.

print()

# Ask user for the total number of graded scores they want to enter.
num_scores = int(input("How many graded scores do you want to enter?  "))
print()

# List to store valid scores
grades = []

# Collect and validate each score 
for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}:  "))

    # Input validation loops: score must be between 0 and 100
    while score < 0 or score > 100:
        print("\nInvalid score entered!!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))

    grades.append(score)

# Process scores and drop the lowest grade
lowest_grade = min(grades)
modified_grades = grades.copy()
modified_grades.remove(lowest_grade)
average_grade = sum(modified_grades) / len(modified_grades)

# Determine the letter grade
if average_grade >= 90:
    letter_grade = "A"
elif average_grade >= 80:
    letter_grade = "B"  
elif average_grade >= 70:
    letter_grade = "C"  
elif average_grade >= 60:
    letter_grade = "D"
else: 
    letter_grade = "F"

# Display the results
print("\n" + "-" * 19 + "Results" + "-" * 20)
print(f"{'Lowest Score':<18}: {lowest_grade}")
print(f"{'Modified List':<18}: {modified_grades}")
print(f"{'Average Score':<18}: {average_grade:.2f}")
print(f"{'Letter Grade':<18}: {letter_grade}")  
print("-" * 46)
print()
