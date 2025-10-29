# wri a program to take user age
#let him know if user can go the club

#21


#logic building formula

#step 1
#input- int
#output- sring(result)-go to club or not

#step2
#rough logic
"""
age<21-->print cant go
age>21-->print can go


"""
#step 3 write a logic

age=int(input("enter age"))
if age>21:
    print("yes ..can go to club")
else:
        print("yes ..cannot go to club")

# Step 4.  Check for the edge cases.
# We should consider edge cases such as:
# Negative ages or extremely high values -> program will break.
# Non-numeric input - ABC
# Age which is valid. > 130

# Step 5.  Optimize the code.
# Handle all the edges.


