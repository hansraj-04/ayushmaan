'''for i in range (50,101):
    if i%2==0:
        print(i,end=" ")'''

a= int(input())
flag=0
for i in range(2,a):
    if a%i==0:
        flag+=1
if flag==0:
    print("prime")
else:
    print(" not prime") 