class person:
    name=None
    age=None
    phone=None
    occupation=None


    def __init__(self):
        self.name=input("what is your name?\n")
        self.age=input("what is your age?\n")
        self.phone=input("what is your phone?\n")
        self.occupation=input("what is your occupation?\n")

    def display_values(self):
        print("Name is:",self.name,"Age:",self.age,"Phone:",self.phone,"Occupation:",self.occupation)

Suraj=person()
Suraj.display_values()
