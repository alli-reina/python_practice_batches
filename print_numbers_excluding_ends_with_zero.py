# Program: Print Numbers from 0 to 100, Excluding Numbers Ending in Zero
# This program prints all numbers from 0 to 100 except for those ending in zero

# Loop through numbers from 0 to 100
for i in range(0, 101):
    
# Print the number if it doesn't end in zero
    if i % 10 != 0:
        print(i)