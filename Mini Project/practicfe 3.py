a = int(input())
if a % 2 == 0 and a > 2:
    x=a//2
    if x%2==0:
        print(x,x)
    else:
        print("x-1,x+1")
else:
    print("NO")
