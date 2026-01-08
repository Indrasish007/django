x=int(input("Enter a number : "))
y=int(input("Enter another number : "))
sum=x+y
print("Sum is : ",sum)
# old version
print("Sum of 2 numbers {} ".format(sum))
#inline if block
max=x if x>y else y
min=x if x<y else y
print("max = {}, min = {}".format(max, min) )
pi=3.14123
print(f"value of pi upto 2 decimal {pi:.2f}".format(pi))
#single line command

'''
multiline comment

conditon of if else

if(condition):
    indented block
elif(condition):
    indented block
else:
    indented block statement
'''

if(x>y):
    print("greater number {}".format(x))
elif(x<y):
    print("greater number {}".format(y))
else:
    print("{}={}".format(x,y))
    
## for loop
for i in range (1,11):
    print(i)
n=int(input("Enter a number : "))
total=0
for i in range(1,n+1):
    total=total+i
print(total)

#prime number 
number=int(input("Enter a number : "))
is_prime=True
if number<=1:
    is_prime=False
else:
    for i in range (2,number):
        if number % i == 0:
            is_prime=False
            break
print("prime"if is_prime else "Not prime")
        
    
#Next program using limit
'''
lim1=int(input("Enter the limit 1"))
lim2=int(input("Enter the limit 2"))
i=lim1
while (i<lim2):
    print("{}".format(i))
    i=i+1
print("Exit value of loop is {}".format(i))
'''

#how many digits in the number :

num = int(input("Enter the number : "))
total=0
while(num>0):
    total+=1
    num//=10
print(f"Digits total is {total}")   

##reverse a number

num=int(input("Enter the number : "))
rev=0
while num>0:
    rev=rev*10+num%10
    num//=10
print(f"The reverse of the number {rev}")