# #Q - Create a function which will take the 3 values from the user,
# which are length of the triangle.  side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene


#Declare the function

side1=int(input("enter side1: "))
side2=int(input("enter side2: "))
side3=int(input("enter side3: "))

def Triangle(side1,side2,side3):
    if side1>0 and side2>0 and side3>0:
        if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
            if side1==side2==side3:
                print("Traingle is Euilateral")
    elif side1==side2 or side3==side2 or side1==side3:
        print("Triangle is Isoceles")
    else:
        print("Scalene triangle")

Triangle(side1,side2,side3)


