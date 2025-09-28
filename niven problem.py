num=int(input("enter num:"))
sum=0
while num>0:
    d=num%10:
    sum+=d
    num//=10
if num%sum==0:
    print("niven sum")
else:
    print("not niven")