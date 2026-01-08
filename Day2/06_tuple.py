t=(10,20,30,10,40,10)
# t[0]=100
print(t)
#slicing

print(t[1:3])
print(t[:2])
print(t.count(10))
print(t.index(10))

# list to tuple conversion

lst=[2,3,4,5]
tpl=tuple(lst)
print(tpl)
print(type(tpl))

# tuple to list conversion

t1=10,20,30
l1=list(t1)
print(l1,type(l1))