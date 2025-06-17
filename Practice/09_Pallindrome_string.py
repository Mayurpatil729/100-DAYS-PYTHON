# 📌 Input a string from the user
text = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison
text = text.lower()

# Remove spaces and special characters if needed (optional)
cleaned = ''.join(char for char in text if char.isalnum())

# Initialize an empty string for the reversed version
reversed_text = ""

# 🔁 Reverse the string using a loop
for ch in text:
    reversed_text = ch + reversed_text  # Prepend each character

# ✅ Check if original and reversed strings are the same
if text == reversed_text:
    print("It's a Palindrome!")
else:
    print("It's NOT a Palindrome.")
    

cleaned_text="".join(char for char in text if char.isalnum())
