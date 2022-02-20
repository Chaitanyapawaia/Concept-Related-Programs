n= int(input("enter a number:"))
for a in range(2,n):
    if (n%a==0):
        print("The number is not a prime number")
        break
else:
    print("The number is a prime number")






z=int(input("enter a number:"))
for b in range(1,z+1):
    y=1
    for c in range(1,z-b+1):
        print(" ", end="")
    for d in range(1,(2*b)):
        if d%2==0:
            print(" ", end= "")
        else:
            print(b**y, end="")
            y=y+1
    print()




q=int(input("Enter a number:"))
w=int(input("Enter a number:"))
e=[]
for r in range(q+1,w):
    for t in range(2,r):
        if (r%t==0):
            break
    else:
        e.append(r)
print(e)



u=eval(input("Enter a list:"))
i=len(u)
for o in range(0,i-1):
    s=0
    for p in range(0, i-o-1):
        if u[p]> u[p+1]:
            u[p],u[p+1]=u[p+1], u[p]
        s=s+1
    print("After pass",o+1,u,"with processings",s)
print(u)





    

        
        
        






    
    
        
        
