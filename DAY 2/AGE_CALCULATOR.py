age = input("What is your current age ? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining*365
weeks_remaining = years_remaining*12
months_remaining = years_remaining*12

# print(months_remaining)
print("You have {} days, {} weeks, and {} months left.".format(
    days_remaining, weeks_remaining, months_remaining))


print(
    f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
