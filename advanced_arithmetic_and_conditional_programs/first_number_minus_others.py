# Program: Subtract the Remaining Numbers from the First Number
# This program asks the user to input 10 numbers and prints the result of the first number minus all of the remaining numbers

num1 = int(input("Enter the first number: "))

for i in range(9):
    num = int(input(f"Enter number {i + 2}: "))
    num1 -= num

print("Difference:", num1)
