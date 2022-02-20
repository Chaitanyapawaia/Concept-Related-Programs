a=0
b=1
d=int(input("Enter the number of element:"))
print(a,b,end=" ")
for i in range(d-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
