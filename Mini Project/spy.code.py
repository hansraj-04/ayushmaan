n=int(input("Enter number: "))
s=0
p=1

while n:
    d=n%10
    s+=d
    p*=d
    n//=10

if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")

