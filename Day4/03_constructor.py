##program of constructor
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student("Indra", 100)
s2=Student("Luffy",100)
s3=Student("Zoro",1000)

print(f'The name is {s1.name} and the marks is {s1.marks}')
print(f'The name is {s2.name} and the marks is {s2.marks}')
print(f'The name is {s3.name} and the marks is {s3.marks}')


