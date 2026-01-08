class Parent:
    def property(self):
        print("prent property")

class Son(Parent):
    pass

class Daughter(Parent):
    pass

s=Son()
d=Daughter()
s.property()
d.property()