def reversestr(c,d):
    if(d==1):
        return(c[0])
    else:
        return(( c[d-1])+reversestr(c,d-1))
def reversenum (a):
    w=0
    while a> 0 :
        q= a%10
        a= a//10
        w= w*10+ q
    return w
qw= "y"
while qw=="y" or qw== "Y":
    wer= int(input("Press 1 for string and 2 for number : "))
    if wer== 1:
        c=input('Enter a string:')
        d=len(c)
        print(reversestr(c,d))
    if wer== 2:
        y=int(input('Enter a number :'))
        print(reversenum(y))
    qw= input("Press 'Y' to continue : ")