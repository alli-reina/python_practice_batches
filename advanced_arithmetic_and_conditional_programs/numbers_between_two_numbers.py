# Program: Print All Numbers Between Two Numbers
# This program asks the user to input two numbers and prints all the numbers between them (exclusive)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i, end=" ")
elif num1 > num2:
    for i in range(num2 + 1, num1):
        print(i, end=" ")
else:
    print("The numbers are the same, no numbers in between.")
