# 📌 Input a number from the user
num = int(input("Enter any number: "))

# Store original number in a temporary variable
temp = num

# Initialize variable to store the reversed number
rev = 0

# 🔁 Reverse the number using a while loop
while temp > 0:
    last_d = temp % 10             # Extract the last digit
    rev = rev * 10 + last_d        # Append digit to reversed number
    temp = temp // 10              # Remove last digit from temp

# ✅ Compare the original and reversed number
if num == rev:
    print(f"{num} is a Palindrome Number")
else:
    print(f"{num} is NOT a Palindrome Number")
