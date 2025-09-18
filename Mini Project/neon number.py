n=int(input("enter number:"))
sq = n*n
sum = 0

while sq:
    d=sq%10
    sum+=d
    sq//=10

if sum==n:
    print("Neon")
else:
    print("Not Neon")
