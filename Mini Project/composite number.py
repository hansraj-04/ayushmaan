n = int(input("Enter number:"))

if n<=1:
    print(n,"is neither Prime nor Composite")
else:
    flag=0
    i=2
    while i<=n//2:   
        if n%i==0:
            flag=1
            break
        i+=1

    if flag==1:
        print(n, "is a Composite Number")
    else:
        print(n, "is a Prime Number")