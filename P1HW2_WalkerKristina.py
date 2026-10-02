# Kristina Walker
# September 11, 2026
# Travel Budget
# This program calculates the total cost of a trip based on user input for various expenses.
print() #I'm putting these for space
print()
# Display introduction message
print("This program calculates and displays travel expenses ")
print()

# Ask the user to enter their budget
budget = float(input("Enter your budget: "))

# Ask user to enter their travel destination
destination = input("Enter your travel destination: ")   

# Ask user the amount they will spend on gas
gas_expense = float(input("How much do you think you will spend on gas?: "))
# Ask user for hotel expenses
hotel_expense = float(input("Approximately, how much will you need for accommodation/hotel?: "))
# Ask user for food expenses
food_expense = float(input("Last, how much do you think you will spend on food?: "))
print()
print() # I'm putting these for space

# Add expenses
total_expenses = gas_expense + hotel_expense + food_expense

# Subtract expenses from budget
remaining_budget = budget - total_expenses


# Display results
print("---------------Travel Expenses---------------")
print(f"location:       {destination}")
print(f"InitialBudget:  {budget:.2f}")
print(f"Fuel:           {gas_expense:.2f}")
print(f"Accomodations:  {hotel_expense:.2f}")
print(f"Food:           {food_expense:.2f}")
print("---------------------------------------------")
print()
print(f"Remaining Budget: {remaining_budget:.2f}")
print()
print() # I'm putting these for space













