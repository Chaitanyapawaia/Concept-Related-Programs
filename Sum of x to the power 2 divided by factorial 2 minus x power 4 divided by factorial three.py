def factorial(w):
    fac=1
    for q in range(w,0,-1):
        fac= fac*q
    return(fac)
n= int(input("Enter the value of n:"))
x= int(input("Enter the value of x:"))
summ= 1
power=2
for i in range(2,n+1):
    y= (x**power)/factorial(i)
    power=power + 2
    if i%2 != 0:
        summ=summ-y
    else:
        summ =summ+y
print("The final value is :",summ )
        