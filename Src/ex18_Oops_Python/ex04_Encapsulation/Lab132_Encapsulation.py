class car:  # paramter constructor

    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model


    def start_engine(self):
        print("Start a car with name: "+self.name)
        print("Make the car: "+self.make)
        print("Model the car: "+self.model)

Audi=car("Audi","Audi","Audi")
Audi.start_engine()