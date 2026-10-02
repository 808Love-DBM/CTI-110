# Kristina Walker
# September 12, 2026
# Calculation of exponents, addition, and subtraction of numbers
# A Python program that calculates the exponent of a number, adds two numbers, and subtracts two numbers.   

print()
print()
print("---------Calculating Exponents---------")
print()
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent number: "))
result = base ** exponent
print(base, "raised to the power of", exponent, "is", result, '!!')
print()
# calculate addition and subtraction
print("---------Calculating Addition and Subtraction---------")
print()
num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter a integer to add: "))
num3 = int(input("Enter a integer to subtract: "))
print()
sum_result = num1 + num2
final_result = sum_result - num3

print(num1, "+", num2, "-", num3, "is equal to", final_result, '!!')
print()