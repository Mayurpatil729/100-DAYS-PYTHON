# Write a Python program that takes a positive integer n as input and calculates the sum of the squares of the numbers from 1 to n.


num = int(input("Enter any Number: "))  # e.g., 3

sum = 0
square = 0

for i in range(1, num + 1):  # Loops from 1 to num (inclusive)
    square = i ** 2          # Square of current number
    sum = sum + square       # Add square to the total sum

print(sum)                   # Print final sum


