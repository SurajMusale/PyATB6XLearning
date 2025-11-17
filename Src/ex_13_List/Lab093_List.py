my_list=[1,2,3]
my_list[0]="Suraj"
my_list[1]="Learn"
my_list[1]="Python"


for item in my_list:
    print(item)

for i in range(1,5):
    print(i)

my_list=[1,2,3]
#Indexing
print("Element at index 0",my_list[0])
print("Element at index 1",my_list[1])
print("Element at index 2",my_list[2])


#Append- append object to end of list

my_list.append(4)
print(my_list)

my_list.append(5)
print(my_list)


# Extend()--Append a new list

my_list.extend([6,7])
print(my_list)

# Insert()--insert data in list

my_list.insert(1,"Suraj")
print(my_list)

my_list.insert(0,"0")
print(my_list)

my_list[1]="Python"
print(my_list)

my_list.remove("Python")
print(my_list)


my_copy_list=my_list.copy()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Suraj")
print(my_copy_list)
print(my_list)


