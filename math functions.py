import math
def ceil(a):
    print("The ceil of the number is",math.ceil(a))
def sqrt(a):
    print("The sqrt of the number is",math.sqrt(a))
def exp(a):
    print("The exp of the number is",math.exp(a))
def fabs(a):
    print("The fabs of the number is",math.fabs(a))
def log10(a):
    print("The log10 of the number is",math.log10(a))
def sin(a):
    print("The sin of the number is",math.sin(a))
def cos(a):
    print("The cos of the number is",math.cos(a))
def tan(a):
    print("The tan of the number is",math.tan(a))
def degrees(a):
    print("The degrees of the number is",math.degrees(a))
def radians(a):
    print("The radians of the number is",math.radians(a))
def hcfandlcm():
    m=int(input("Enter a number:"))
    n=int(input("Enter a number:"))
    q=1
    if m>n:
        o=m
    else:
        o=n
    for p in range(1,o):
        if m%p==0 and n%p==0 :
            q=q*p
    print("HCF is",q, "And LCM is",(m*n)/q)

ch="yes"
while ch=="yes":
    a=float(input("Enter a number:"))
    ceil(a)
    sqrt(a)
    exp(a)
    fabs(a)
    log10(a)
    sin(a)
    cos(a)
    tan(a)
    degrees(a)
    radians(a)
    hcfandlcm()
    ch= input("Do you want to continue? yes or no : ")
        