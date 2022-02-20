def fact(r):
    s=1
    if r==1 or r==0:
        return 1
    else:
        for t in range (1,r+1):
            s= s*t
        return s
u= int(input("Enter a number:"))
v=str(fact(u))
x=0
for w in v:
    x=x+int(w)
print("The sum is",x)
