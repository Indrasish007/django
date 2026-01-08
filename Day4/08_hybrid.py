class A:
    def showA(self):
        print("class a")
        
class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

d=D()
d.showA()