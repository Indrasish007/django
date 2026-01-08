t=(1,"python",10.2,"a",True)
print(t)
tpl=(1,2,(3,4),5,6)
print(tpl[2])
print(tpl[2][1])

# tuple unpacking

t1=(10,20,30,40)
a,b,c=t1
print(a,b,c)

t2=((2,3),(5,7))
for row in t2:
    for i in row:
        print(i)
for j in range(len(t1)-1,-1,-1):
    print(t1[j])