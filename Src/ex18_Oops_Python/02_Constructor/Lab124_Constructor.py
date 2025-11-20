print("Outside the class 1")
class MobilePhone:
    model=None  # Attribute

    def __init__(self):
        print("Mobile Phone")
    def talk(self): #Behaviour
        print("I can Talk")


iphone=MobilePhone() # create object ref for class
iphone.talk()  # calling method usinf object ref
print("outside the class 2")
