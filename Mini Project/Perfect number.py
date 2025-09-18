n=int(input("Enter number: "))
s=0
i=1

while i<= n//2:
    if n%i==0:
        s+=i
    i+=1

if s==n and n!=0:
    print(n,"is a Perfect Number")
else:
    print(n,"is Not a Perfect Number")
