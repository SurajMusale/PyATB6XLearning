# Create a Person class where we will have five attributes and five behaviors.
# Make sure that each type of function is used, and I want you to also create the print function,
# which will print all the instance variable values.



class Person:
    name=None
    height=None
    weight=None
    hobby=None
    shape=None
    def __init__(self, name, height, weight, hobby, shape):
        self.name = name
        self.height = height
        self.weight = weight
        self.hobby = hobby
        self.shape = shape
    def talk(self):
        print(self.name, self.height, self.weight, self.hobby, self.shape)
    def dance(self):
        print(self.name, self.height, self.weight, self.hobby, self.shape)
    def study(self):
        print(self.name, self.height, self.weight, self.hobby, self.shape)
    def eat(self):
        print(self.name, self.height, self.weight, self.hobby, self.shape)

    def __str__(self):
        return f"name={self.name}, height={self.height}, weight={self.weight}, hobby={self.hobby}, shape={self.shape}"


ref_var=Person("Real Estate",100,100,100,100)
ref_var.talk()
ref_var.talk()
ref_var.dance()
ref_var.study()
ref_var.eat()

print(ref_var)