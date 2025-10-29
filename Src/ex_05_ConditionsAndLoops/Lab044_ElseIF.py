# find the no is even or odd

num=int(input("enter num").strip())
if num>0:
    if(num%2==0):
        print("num is even")
    else:
        print("num is odd")
else:
        print("num is negative")

if num >= 0:
    print("Even" if num % 2 == 0 else "Odd")
else:
    print("Negative Number")

# You can write short one-liner conditions using ternary operator: