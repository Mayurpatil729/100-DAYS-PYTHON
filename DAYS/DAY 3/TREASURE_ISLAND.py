print('''*******************************************************************************
          |                   |                  |                     |                
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ". |
|___________________ | _._"  ,. .` ` `` ,  `"-._"-._   ". '__ | ___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________ |; `-.o`"=._; ." ` '`."\` . "-._ / _______________|_______
| | | o;    `"-.o`"=._``  '` ", __.--o; |
|___________________|_ | ;     (  # ) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___ | o; ._    "      `".o | o_.--"; o; ____/______/______/____
/ ______/______/______/_"=._o--._; | ;        ; ; / ______/______/______/_
____/______/______/______/__"=._o--._; o | o;     _._; o; ____/______/______/____
/ ______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/ ______/______/______/______/______/______/______/______/______/______/[Treasure island]
*****************************************************************************************
''')

print("Welcome to the treasure island ")
print("Your mission is to find the treasure : ")

choice1 = input(
    'You\'re at a crossroad, where do you want to go ? Type "left" or "right".===>').lower()

if choice1 == "left":
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim acros. ===>').lower()
    if choice2 == "wait":
        choice3 = input(
            "You arrive at the island unharmed. Ther is a house with 3 doors. one red, one yellow and one blue. which colour do you choose ? ===> ").lower()
        if choice3 == "red":
            print("\nIt's a room full or fire. Game over. ")
        elif choice3 == "yellow":
            print("\nYou found the treasure ! You win")
        elif choice3 == "blue":
            print("\nYou enter a room of beasts. Game over. ")
        else:
            print("\nYou choose a door that doesn't exist. Game over.")
    else:
        print("\nYou got attacked by angry trout. Game over")
else:
    print("\nYou fell into a hole. Game over.")
