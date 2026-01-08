'''
1.swap 2 number using or not using 3rd var
2.check a no whether pos or not
3.check a nubmer even or odd
4.calculate a area of a circle and output will be upto 2 decimal places
5.calculate the volume of the rectangle
'''
## task 1.a
print("task 1 a")
a=2
b=3
print(f'before swapping a={a},b={b}')
a,b=b,a
print(f'after swapping a={a},b={b}')

##task 1 b
print("task 1 b")
a=2
b=3
c=a
a=b
b=c
print(f"after swapping using 3rd var a={a},b={b}")

##task 2
print("task2")
a=int(input("Enter a number : "))
if a<0:
    print("The number is neg ")
else:
    print("the number is pos")

##task 3
print("task 3")
a=int(input("Enter a number : "))
if a%2==0:
    print("The number is even ")
else:
    print("the number is odd")

##task 4
print("task 4")
r=int(input("Enter a radius : "))
pi=3.1412
area=pi*r*r
print(f"the area : {area:.2f}")

##task 5

print("task 5")
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
h=int(input("Enter the height : "))
area=l*b
print(f'area of rectangle {area:.2f}')

volume=l*b*h
print(f'volume of rectangle {volume}')