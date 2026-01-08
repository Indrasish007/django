from abc import ABC,abstractmethod
class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("car startted")
        
    def stop(self):
        print("car stopped")
        
c=Car()
c.start()
c.stop()