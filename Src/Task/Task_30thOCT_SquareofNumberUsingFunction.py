#Q - Create a function which will take a positive number from the user and perform square of the number?

#i/o = 3

#o/p = 9

def square():
    #Take input from user
    num = int(input("Enter a number: "))

#check if number is postitive
    if(num>0):
        result=num**2
        print("The square of number: ",result)

    else:
        print("invalid number")
#calling the function

square()

