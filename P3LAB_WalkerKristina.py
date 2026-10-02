# Kristina Walker
# September 30, 2026
# Calculate coins and dollars needed
print()
print("-" * 20, "$Currency$", "-" * 20)
print()
# Get money input
money = float(input("Enter an amount of money: $"))
# Move decimal two places to the right
money_int = int(money * 100)
print()
# print(money_int)
# Determine how many dollars are needed
dollars = money_int // 100
# print(f"Dollars: {dollars}")
# Remove dollars from money_int
# Overwrite the old value for money_int
# With the new value tht does not include dollars
money_int = money_int - (dollars * 100)
# Determine how many quarters are needed
quarters = money_int // 25
# print(f"Quarters {quarters}")
# Remove quarters from money_int
money_int = money_int - (quarters * 25)
# Determine how many dimes are needed
dimes = money_int // 10
# print(f"Dimes {dimes}")
# Remove dimes from money_int
money_int = money_int - (dimes * 10)
# Determine how many nickles are needed
nickles = money_int // 5
# print(f"Nickles {nickles}")
# Remove nickles from money_int
# Determine how many pennies are needed
pennies = money_int // 1
#print(f"Pennies {pennies}")
print()
print("X" * 19, "End Results", "X" * 19) 
print()
# Only display coins if one or more is needed
# Define the function
def print_needed(coin, coin_name):
    if coin >= 1:
        if coin == 1:
            print(f"{coin} {coin_name}")
        if coin > 1:
            if coin_name == "penny":
                print(f"{coin} pennies")
            else:
               print(f"{coin} {coin_name}s")

# Call the function using the different dollars & coins
print_needed(dollars, "dollar")
print_needed(quarters, "quarter")
print_needed(dimes, "dime")
print_needed(nickles, "nickel")
print_needed(pennies, "penny")
print()




