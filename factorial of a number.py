def fact(i):
    h=1
    if i==1 or i==0:
        return 1
    else:
        for j in range (1,i+1):
            h= h*j
        return h
l= int(input("Enter a number:"))
print(fact(l))
