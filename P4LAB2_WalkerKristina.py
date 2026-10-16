# Kristina Walker
# October 16, 2026
# P4LAB2
# Program to display multiplication tables using loops

print()
print()

# if number is positive, display multiplication table
# if number is negative, tell user program "Sorry, this program does not accept negative values."
# if yes, run program again
# if no, end program

# Initialize a variable to control the while loop run_again = "yes"
run_again = "yes"

# While loop to keep running the program until the user enters "no"
while run_again != "no":

    # Display a message to the user
    print("This program will display the multiplication table for any integer you enter.")
    print()
    # Ask the user for an integer
    user_num = int(input("Enter an integer: "))

    # Check if the number is zero or higher
    if user_num >=0:
        # For loop to display multiplication table from 1 to 12
        for i in range(1, 13):
            print(f"{user_num} * {i} = {user_num * i}")

    else: # Message displayed if input is less than zero
        print("Sorry, this program does not accept negative values.")

    # Ask the user if they want to run the program again
    run_again = input("Do you want to run this program again? (yes/no): ")
    print()
    print()

# Loop has broken. User entered "no"
print("Program has ended.....")
