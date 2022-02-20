a='program'
if len(a)%2==0:
    z=len(a)/2
else:
    z=(len(a)//2)+1
for b in range (0,z):
    for c in range (0,len(a)):
        if c==b or c==(len(a)-1-b):
            print(a[c],end=' ')
        else:
            print(' ',end=' ')
    print()
