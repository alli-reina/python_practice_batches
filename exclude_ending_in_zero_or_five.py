# Program: Print Numbers from 0 to 100, excluding those ending in 0 or 5
# This program prints all the numbers from 0 to 100, but skips the ones ending in 0 or 5

# Loop through the numbers from 0 to 100
for i in range(101):
    # Check if the number ends in 0 or 5
    if i % 10 == 0 or i % 10 == 5:
        continue  # Skip the number if it ends in 0 or 5
    print(i, end=" ")