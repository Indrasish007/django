##Frozen set is mutable

fset=frozenset([1,2,3])
# fset.add(4)
print(fset,type(fset))

#list to shape
num=[1,2,2,3,4,5,4,6]
s=set(num)
print(s)

#tuple to set
tup=1,2,3,4
s1=set(tup)
print(s1)
