def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]

n = int(input("Enter the number of terms"))
print(fibonacci(n))



month=set(["January","February","March","April","May","June"])
print(month)
month.discard("january")

days1={"mon","tue","wed","thu","fri","sat","sun"}
days2={"fri","sat","sun"}
print(days1&days2)


a={"devansh","bob","castle"}
b={"castle","dude","emyway"}
c=("fuson","gaurav","castle")

a.intersection_update(b,c)

print(a)

a={1,2,3,4,5,6,90}
b={1,2,3,4,10}
c=a^b
print(c)
TypeError()

days1={"mon","tue","wed","thu","fri","sat","sun"}
days2={"fri","sat","sun"}
days3={"tue","wed","thr","fri"}
print(days1>days2)
print(days3<days1)
print(days1>days3)



# Set Functions (Mutable, Unordered, No Duplicates)
#Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print("add:", my_set)  

my_set.remove(6)
print("remove:", my_set)  

my_set.discard(6)  
print("discard:", my_set)  

popped_item = my_set.pop()
print("pop:", my_set, "popped item:", popped_item) 

my_set.clear()
print("clear:", my_set)

my_set = {1, 2, 3}
other_set = {3, 4, 5}
union_set = my_set.union(other_set)
print("union:", union_set) 

intersection_set = my_set.intersection(other_set)
print("intersection:", intersection_set) 

difference_set = my_set.difference(other_set)
print("difference:", difference_set) 

sym_diff_set = my_set.symmetric_difference(other_set)
print("symmetric_difference:", sym_diff_set) 

print("issubset:", my_set.issubset({1, 2, 3, 4}))

print("issuperset:", my_set.issuperset({1, 2}))


print("isdisjoint:", my_set.isdisjoint({4, 5}))

set_copy = my_set.copy()
print("copy:", set_copy) 


thisdict={
    "brand":"Land Rover",
    "model":"Defender110",
    "yerar":1977
}
mydict=thisdict.copy()
print(mydict)

myfamily={
    "child1":{
        "name":"ayush",
        "year":2005
    },
    "child2":{
        "name":"ravikant",
        "year":2007
   },
}
print(myfamily["child2"]["name"])

car={
    "brand":"Land rover",
    "model":"defender",
    "year": 1977
}  
car.clear()
print(car)


class myclass:
    x=5
p1= myclass()
print(p1.x)

class computer:
    def config(self):
        print("15,12th,gen,500gb")
com1=computer()
com2=computer()
computer.config(com1)
computer.config(com2)
com1.config()


