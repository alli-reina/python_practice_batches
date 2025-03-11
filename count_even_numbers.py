# Program: Count the Even Numbers
# This program asks the user to input 10 numbers and prints how many of them are even numbers

# Initialize the even number count to 0
even_count = 0

# Ask the user to input 10 numbers
for i in range(10):  # Loop to input 10 numbers
    num = int(input(f"Enter number {i + 1}: "))
    
# Check if the number is even
# Print the total number of even numbers