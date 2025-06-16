num=int(input("Enter the Number : "))

rev=0
while num>0:
    last_d=num%10
    rev=rev*10+last_d
    num=num//10


print("The reverse of the number is : ",rev)