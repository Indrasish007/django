add=lambda a,b:a+b
print(add(5,3))

# use lambda in one line
print((lambda x:x*x)(4))

#map is for apply function for each element
nums=[1,2,3,4]
square=list(map(lambda x:x*x,nums))
print(square)

#filter function ## filter values based on condition
even=list(filter(lambda x:x%2==0,nums))
print(even)

## reduce

from functools import reduce
result=reduce(lambda a,b:a+b,nums)
print(result)