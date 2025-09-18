'''l1 = [5, 2, 9]
l2 = [8, 1, 4]

l1.sort()
l2.sort()

new_list = l1 + l2
new_list.sort()

print("Merged Sorted List:", new_list)

lst = list(map(int, input("Enter numbers: ").split()))

lst[0], lst[-1] = lst[-1], lst[0]

print("List after swapping:", lst)


my_list = [1,2,3,4,4,5]

unique_list=[]

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("List after deleting duplicates:",unique_list)

my_list = [1, 2, 3, 2, 3, 3, 4]

odd_list = []

for item in my_list:
    if my_list.count(item) % 2 != 0 and item not in odd_list:
        odd_list.append(item)

print("Elements occurring odd number of times:", odd_list)

my_list = [5, 1, 9, 2, 6, 3]

my_list.sort()

sum_min3 = my_list[0] + my_list[1] + my_list[2]

print("Sum of three minimum values:", sum_min3)

l=[18,19,30,25,43]
l1=[]
l2=[]
l3=[]
for i in l:
    if i%2==0:
        l1.append(l)
    else:
        l2.append(l )
l1.sort(reverse=True)
print(l1)
l2.sort()
print(l2)
l3=l1+l2
print(l3)'''

l=[1,3,5,6,7,9,10,2,4]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort(reverse=True)
odd.sort()
res=even+odd
print(res)
    