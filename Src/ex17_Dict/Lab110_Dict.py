my_dict={"name":"Suraj",
         "age":18,
         "height":70,
         "exp":3,
         "Role":"QA"}


print(my_dict)

print(my_dict["age"])
print(my_dict["height"])

my_dict["role"]="Manual Tester"
print(my_dict)

del my_dict["age"]
print(my_dict)

for key,value in my_dict.items():
    print(key,value)


print("age" in my_dict)
print("role" in my_dict)







