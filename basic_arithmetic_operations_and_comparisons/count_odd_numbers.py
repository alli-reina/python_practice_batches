# Program: Count the Odd Numbers in 10 Inputs
# This program asks the user to input 10 numbers and counts how many of them are odd

odd_count = 0

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))

    if num % 2 != 0:
        odd_count += 1

print("Odd numbers:", odd_count)
