class Home:
    def __init__(self):
        self.public_var = "father"          # Public
        self._protected_var = "brother"     # Protected (by convention)
        self.__private_var = "baby"         # Private (name-mangled)

    def mom(self):
        print(self.__private_var)   # Accessing private variable inside class
        self.__wife()               # Accessing private method inside class

    def __wife(self):
        print("Private Wife")


object_ref = Home()

object_ref.mom()  # Allowed

# object_ref.__wife()      # ❌ Not allowed (private)
# object_ref.__private_var # ❌ Not allowed (private)

# print(object_ref._protected_var)  # ⚠️ Allowed but NOT recommended
