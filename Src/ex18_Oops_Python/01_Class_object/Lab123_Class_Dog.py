class Dog:
    # Atribute
    name=None
    breed=None
    Height=None
    Weight=None

    # Behaviour

    def Bark(self):
        print("Bark")
        print(self.name)

    def talk(self):
        print("I can Talk")

print("outside the class")
chow=Dog()
rancho=Dog()

#Dog -object
#chow,rancho-object refrence

