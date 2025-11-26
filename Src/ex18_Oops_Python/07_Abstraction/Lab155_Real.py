from abc import ABC, abstractmethod

class GearBox(ABC):
    @abstractmethod

    def setgear(self):
        pass

class engine:
    def start(self):
        pass
    def stop(self):
        pass

class car(GearBox, engine):
    def start(self):
        print("Starting")
    def stop(self):
        print("Stopping")

    def setgear(self):
        print("Setting Gear")

    def drive(self):
        self.setgear()
        self.start()
        self.stop()

tesla=car()
tesla.drive()