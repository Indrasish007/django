class College:
    def __init__(self):
        self._college='ABC college' #protected
    
class Student(College):
    def show(self):
        print(self.college)
        
s=Student()
s.show() 