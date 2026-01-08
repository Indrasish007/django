student={
    'name':'John',
    'age':23,
    'course':'python'
    
}
print(student,type(student))
print(student['name'])
student['city ']='Kolkata'
print(student)
student['age']=34
print(student)

student.pop('course')
print(student)

#delete key

del student['city']
student.clear()
print(student)

