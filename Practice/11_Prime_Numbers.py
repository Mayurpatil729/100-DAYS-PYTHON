# 📌 Input a number from the user
num = int(input("Enter a number: "))

# 📌 Prime numbers are greater than 1
if num > 1:
    # Assume it's prime unless proven otherwise
    is_prime = True

    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # ✅ Result
    if is_prime:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is NOT a Prime Number")
else:
    print(f"{num} is NOT a Prime Number (must be greater than 1)")
