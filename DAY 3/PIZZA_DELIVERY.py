print("Welcome to the python pizza deliveries! ")
size=input("What size pizza do you want ? S ,")
add_pepperani=input("Do you want pepperani ?")
extra_cheese=input("Do you want extra cheese ")

bill=0

if size=="S":
    bill+=15
elif size=="M":
    bill+=20
else :
    bill+=25

if add_pepperani=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
    
if extra_cheese=="Y":
    bill+=1
    
print(f"Your final bill is ${bill}")
    















