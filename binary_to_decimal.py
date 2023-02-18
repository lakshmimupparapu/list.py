a=int(input("Enter the number:"))
i=0
sum=0
while a>0:
    k=a%10
    if k==1:
        sum=sum+(2**i)
    a=a//10
    i=i+1
print(sum)