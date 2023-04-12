print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage_tip = int(
    input("What percentage tip would you like to give? 10,12,or 15 ?"))
people = int(input("How many people to split the bill? "))
bill_with_tip = percentage_tip/100*bill+bill
# bill_with_tip=bill*(1+percentage_tip/100)
print(bill_with_tip)
bill_per_person = bill//people
# print(bill_per_person)
final_amount = round(bill_per_person, 2)
# final_amount="{:.2f}".format(bill_per_person)
print(f"Each person should pay : ${final_amount}")


# tip_as_percent=percentage_tip/100
# total_tip_amount=bill*tip_as_percent
# total_bill=bill+total_tip_amount
# print(total_bill)
