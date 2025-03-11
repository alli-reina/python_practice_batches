# Program: Subtract the Remaining Numbers from the First Number
# This program asks the user to input 10 numbers and prints the result of the first number minus all of the remaining numbers

# Ask the user for the first number
num1 = int(input("Enter the first number: "))

# Loop to subtract all remaining numbers from num1
for i in range(9):  # Loop for the remaining 9 numbers
    num = int(input(f"Enter number {i + 2}: "))
    num1 -= num  # Subtract the entered number from num1

# Print the final result
print("Difference:", num1)