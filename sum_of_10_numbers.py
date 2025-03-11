# Program: Calculate the Sum of 10 Numbers
# This program asks the user to input 10 numbers and prints the sum of those numbers

# Initialize the total sum to 0
total_sum = 0

# Loop through 10 times to get the numbers from the user
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    total_sum += num
    
# Print the total sum