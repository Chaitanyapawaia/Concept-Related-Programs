def fact(i):
    h=1
    if i==1 or i==0:
        return 1
    else:
        for j in range (1,i+1):
            h= h*j
        return h
ca= 0
l= int(input("Enter a number:"))
for w in range(1, l+1):
    a=fact(w)/w
    if w%2 != 0:
        ca= ca+a
    else:
        ca= ca-a
print(ca)