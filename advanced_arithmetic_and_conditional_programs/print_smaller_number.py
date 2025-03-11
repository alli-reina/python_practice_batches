# Program: Print the Smaller Number
# This program asks the user to input two numbers and prints the smaller one
# If the numbers are equal, it prints "Equal"

# Ask the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compare the two numbers and print the smaller one or if they are equal
if num1 < num2:
    print("Smaller number:", num1)
elif num1 > num2:
    print("Smaller number:", num2)
else:
    print("The numbers are equal.")
