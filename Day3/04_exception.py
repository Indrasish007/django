try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("can not divide by zero")
finally :
    print('code run successfully')