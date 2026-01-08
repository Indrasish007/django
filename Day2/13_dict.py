student={
    'name':'John',
    'age':23,
    'course':'python'
    
}

for key in student:
    print(key)
for value in student.values():
    print(value)
for key,value in student.items():
    print(key,":",value)

#dictionary method

print(student.keys())
print(student.values())
print(student.items())