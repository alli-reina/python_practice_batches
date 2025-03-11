# Program: Count the Odd Numbers in 10 Inputs
# This program asks the user to input 10 numbers and counts how many of them are odd

# Initialize the count of odd numbers to 0
odd_count = 0

# Loop through 10 times to get the numbers from the user
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))

    # Check if the number is odd
    if num % 2 != 0:
        odd_count += 1

# Print the total count of odd numbers