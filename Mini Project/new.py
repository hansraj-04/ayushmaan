
'''rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print("*" * i)
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print("*" * i)
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("" * (rows - i) + "*" * i)

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

n= int(input("enter the number of square:"))
for i in range(n):
    for j in range(n):
        print(" ",end="*")
    print()

rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print(" " * (rows-i) +"*" *i)

n= int(input("enter the number of square:"))
for i in range(n):
    for j in range(n):
        print(" ",end="*")
    print()

num = int(input("enter the number:"))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

a= int(input("enter the number:"))
b= int(input("enter the number:"))
c= int(input("enter the number:"))

if a>b and a>c:
    print("a is the greatest")
elif b>c and b>a:
    print("b is the greatest")


else:

    print("cis the greatest")'''

