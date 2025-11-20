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
        pass

    def __init__(self,namegiven,breedgiven): #Paramterized construtor
        print("Parameterized constructor")
        self.name=namegiven
        self.breed=breedgiven

chow=Dog(namegiven="chow",breedgiven="Chicken")
rancho=Dog(namegiven="rancho",breedgiven="Chicken")

chow.Bark()



