#find maximum between three number

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

# 5 > 3 and 5 >2 ->  5
# num1 > num2 and num1 > num3 -> num1
# num2 > num1 nad num2 > num3 -> num2
# num3 - max

if num1 >= num2 and num1 >= num3:
    print("Max", num1)
elif num2 >= num3 and num2 >= num1:
    print("Max", num2)
else:
    print("Max", num3)