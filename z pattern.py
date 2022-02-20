i= 2
j=6
for a in range(1,8,+1):
    for b in range(1,8):
        if (a==1)or (a==7):
            print ("#",end=" ")
        elif (a==i)and (b==j):
            print("#", end=" ")
            i=i+1
            j=j-1
        else:
            print(" ",end=" ")
    print()

        
        
    
        
