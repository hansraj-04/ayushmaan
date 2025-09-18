n=int(input("Enter number: "))
temp=n
digits=0
while temp:           
    digits+=1
    temp//=10

temp=n
sum=0
while temp:           
    d=temp%10
    sum+=d**digits
    temp//=10

if sum==n:
    print("Armstrong")
else:
    print("Not Armstrong")
