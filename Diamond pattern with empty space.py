a= int(input("Enter a number:"))
for b in range (1,a+1):
    for c in range (1,a-b+1):
        print(" ", end='')
    for d in range (1,2*b):
        if d==1 or d==2*b-1 :
            print("$", end='')
        else:
            print(" ", end='')
    print()
for e in range (a-1,0,-1):
    for f in range (1,a-e+1):
        print(" ", end='')
    for g in range (1,2*e):
        if g==1 or g==2*e-1 :
            print("$", end='')
        else:
            print(" ", end='')
    print()












        
            
    
