n=int(input("enter number:"))
while n>9:
    s=0
    while n:
        d=n%10
        s+=d
        n//=10
    n=s
if n==1:
    print("magic number")
else:
    print("not magic number")