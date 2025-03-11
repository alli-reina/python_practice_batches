# Program: Print the Quotient of Two Numbers
# This program asks the user for two numbers and prints the quotient of the division (with decimal)
# If the second number is zero, it prints an error message

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the second number is zero to avoid division by zero error
if num2 == 0:
    print("Error: Cannot divide by zero.")
else:
    # Calculate and print the quotient of the two numbers
    quotient = num1 / num2
    print("Quotient:", quotient)
