def reverse(c,d):
    if(d==1):
        return(c[0])
    else:
        return(( c[d-1])+reverse(c,d-1))
c=input('Enter a string:')
d=len(c)
print(reverse(c,d))
