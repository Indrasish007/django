a={1,2,3}
b={2,3,4}
print(a|b)#pipeline operator . this is called union
print(a&b)#intersect operator . this is called intersection
#union function
print(a.union(b))
print(a.intersection(b))
print( a-b)
print(a.difference(b))
print(b-a)
print(b.difference(b))

