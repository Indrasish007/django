class Grandfather:
    def land(self):
        print("Grandfather land")
        
class Father(Grandfather):
    def house(self):
        print("Father house")
        
class Son(Father):
    def car(self):
        print("son car")
    
s=Son()
s.land()
s.car()
s.house()