# Write a program to calcuclate even and odd
# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

user_input=int(input("Enter a number: "))

check_even_odd_function=lambda num:"Even" if num%2==0 else "Odd"
result=check_even_odd_function(user_input)
print(result)