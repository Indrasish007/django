#task 1 : signal 
color=input("Enter a color red , green or yellow : ")
if color == 'red' or color=='Red' :
    print("Stop the car")
elif color == 'yellow' or color =='Yellow':
    print("Forward slowly")
elif color== 'green' or color=='Green':
    print("Onwards to onigashima")
else :
    print("Enter valid input")

#task 2: 
marks=int(input("Enter the marks : "))
if marks>=90:
    print("A")
elif marks>=80 and marks<90:
    print("B")
elif marks>=70 and marks<80:
    print("C")
elif marks>=60 and marks<70:
    print("D")
elif marks>=0 and marks<60:
    print("F")
else:
    print("Enter valid")
    
#task 3:
age=int(input("Enter you age : "))
if age>=18:
    print("You can vote ")
else:
    print("You can't vote")
    
##task 4

num1=int(input("Enter the number : "))
num=num1
rev=0
while num>0:
    rev=rev*10+num%10
    num//=10
# print(f"The reverse of the number {rev}")
# print(f"num1 is {num1}")
if rev==num1:
    print (num1, rev)
    print("palindrome")
else:
    print (num1, rev)
    print("not pali")
    
##task 5
#string palindrome
n=input("Enter a string  : ")
rev=n[: : -1]
print(rev)
if n==rev:
    print("palindrome")
else:
    print("Not pali")

