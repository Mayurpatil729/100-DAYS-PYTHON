num=int(input("Enter the Number :"))

sum=0
while num>0:
    last_d=num%10
    sum=last_d+sum
    num=num//10
    
print(sum)


