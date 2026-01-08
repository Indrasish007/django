s={1,2,3,4,1,2}
print(s,type(s))
for i in s :
    print(i)
s.add(5)
print(s)
s.update([6,7,8])
print(s)
s.remove(2)
print(s)
s.discard(3)
print(s)
s.pop()#remove random  element
print(s)