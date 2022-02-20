a= eval(input("enter a list:"))
b= len(a)
for zx in range (1,b):
    key= a[zx]
    cv=zx-1
    while cv>=0 and key<a[cv]:
        a[cv+1]=a[cv]
        cv=cv-1
    else:
        a[cv+1]= key
print("the list is ",a)
