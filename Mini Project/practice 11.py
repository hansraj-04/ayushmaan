n=int(input("enter the number:"))
sum=0
while n!=0:
    d=n%10
    sum=sum+d
    n=n//10
print(sum)

n=int(input("enter number:"))
count=0
while n!=0:
    count+=1
    n=n//10
print(count)

n=int(input("enter number:"))
rev=0
sign=1

if n<0:
    sign=-1
    n=-n

while n!=0:
    digit = n%10
    rev = rev*10+digit
    n = n//10

print("reverse:", sign*rev)
