class Father:
    def house(self):
        print("Father house")
        
class Mother:
    def gold(self):
        print("mother gold")
        
class Child(Father,Mother):
    pass

c=Child()
c.house()
c.gold()
    