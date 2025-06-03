import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'h', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator !")
nr_letters = int(input("How many letters would you like in you password ? "))
nr_numbers = int(input(f"How many numbers would you like in you like? \n "))
nr_symbols = int(input(f"How many symbols would you like in you like? \n"))
# nr_symbols=int(input(f"How many numbers would you like in you like ? "))


# easy level
# password=" "

# for char in range(1,nr_letters+1):
#     password+=random.choice(letters)

# for char in range(1,nr_symbols+1):
#     password+=random.choice(symbols)

# for char in range(1,nr_numbers+1):
#     password+=random.choice(numbers)


# print(password)

# hard level

password_List = []


for char in range(1, nr_letters+1):
    password_List.append(random.choice(letters))

for char in range(1, nr_symbols+1):
    password_List += random.choice(symbols)

for char in range(1, nr_numbers+1):
    password_List += random.choice(numbers)


print(password_List)
random.shuffle(password_List)
print(password_List)


password = ""
for char in password_List:
    password += char

print(f"Your password is : {password}")










