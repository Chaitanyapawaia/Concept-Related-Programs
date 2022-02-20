def numbers():
    a=int(input('enter the number:'))
    b=int(input('enter the number:'))
    add(a,b)
    sub(a,b)
    multi(a,b)
    divi(a,b)
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def multi(a,b):
    print(a*b)
def divi(a,b):
    try: 
        result = a/b
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
numbers() 