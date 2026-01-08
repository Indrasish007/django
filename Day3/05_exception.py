try:
    x=int('abc')
except ValueError:
    print('invalid conversion')
    
except TypeError:
    print('invalid type')
    