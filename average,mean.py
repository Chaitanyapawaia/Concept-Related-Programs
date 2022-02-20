a= int(input("Enter a the number of subjects:"))
f=int(input("enter the Maximunm marks:"))
d=0
for b in range (1,a+1):
    c= int(input("Enter your marks in subject number:"))
    d=d+c
e=d/(a*f)
print("The percentage is",e*100)



g=eval(input("enter a list:"))
i=0
for h in g:
    i=i+h
j=i/len(g)
print("The mean is",j)


import random
k= random.randint(1,100)
for m in range (1,6):
    print("Its your",m, "try")
    l= int(input("Enter a number between 1 to 100:"))
    if k==l:
        print("congrats you won")
        break
    else:
         print("Better luck next time")
else:
    print("Better luck next time","The number was",k)
         


n=eval(input("Enter a list:"))
o= len(n)
q=n[0]
for p in range (1,o):
    r=n[p]
    if p==o-1:
        n[0]=r
        n[p]=q
    else:
        n[p]=q
        q=r
print(n)


t=eval(input("Enter a list:"))
u=len(t)-1
while u>0:
    for v in range (0,u):
        t[v],t[v+1]=t[v+1],t[v]
    u=u-1
print(t)

x=eval(input("Enter a list:"))
z=len(x)
for y in range(0,z):
    if x[y]>10:
        x[y]=10
print(x)


qw=eval(input("Enter a list:"))
er=eval(input("Enter a list:"))
ty=[]
for ui in range (0, len(qw)):
    op=qw[ui]+er[ui]
    ty.append(op)
print(ty


for asd in range (0,9):
    for df in range (1,9-asd-1):
        print(" ",end="")
    for gh in range (1,2*asd):
        if asd%2!=0:
            print("&",end="")
        else:
             print(" ",end="")
    print()
    
