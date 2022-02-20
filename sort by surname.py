a=()
b=""
while b != 'no':
    b=input('enter a name or type "no":')
    if b=='no':
        break
    else:
        a=a+(b,)
c=[]
for d in a:
    for e in range (0,len(d)):
        if d[e]==" ":
            f=d[e+1:]
            c.append(f)
            break
z=[]    
n=len(c)
for i in range (n):
    for j in range (n-i-1):
        if c[j]>c[j+1]:
            c[j],c[j+1]=c[j+1],c[j]

for g in c:
    for h in a:
        if g in h:
            z.append(h)
z=tuple(z)
print(z)
