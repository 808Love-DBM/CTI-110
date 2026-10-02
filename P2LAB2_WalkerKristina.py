# Kristina Walker
# September 19, 2026
# P2LAB2
# Using dictionaries

print()
print()
cars = {'Camero': 18.21, 'Prius': 52.36, 'Model s': 110, 'Silverado': 26}
#Get keys from the dictionary
car_keys = cars.keys()
print(car_keys)
print(*car_keys, sep = ', ')
print()
#Get a car from user
car_name = input("Enter a car: ")
print()
#Get mpg for the given car
car_mpg = cars [car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon. ")
print()
#Gets miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))
print()
#calculate 
gallons_needed = miles_driven/car_mpg
#Display results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")
print()
