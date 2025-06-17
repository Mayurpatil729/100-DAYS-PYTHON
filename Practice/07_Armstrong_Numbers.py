num = int(input("Enter any Number: "))
temp = num
sum = 0

# Step 1: Count the number of digits
digits = len(str(num))  # Or you can do this with a loop too

# Step 2: Calculate sum of each digit raised to 'digits' power
while temp > 0:
    last_d = temp % 10
    sum =sum + last_d ** digits
    temp = temp // 10

# Step 3: Check Armstrong condition
if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")
