from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self,name):
        self.name = name


    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog bark")


Dog=Dog("pp")
Dog.sound()
