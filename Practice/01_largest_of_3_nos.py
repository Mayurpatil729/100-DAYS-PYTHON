n1=int(input("Enter the first Number : "))
n2=int(input("Enter the second Number : "))
n3=int(input("Enter the third Number : "))

if n1>=n2 and n1>=n3:
    print(f'{n1} is greater number')
elif n2>=n3 and n2>=n1:
    print(f'{n2} is greater number')
else:
    print(f'{n3} is greater number')
    