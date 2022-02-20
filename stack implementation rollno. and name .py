def push(l,y):
    l.append(y)
    top= len(l)-1
    return(top)
def pop(l):
    if len(l)==0:
        print('Underflow')
        top = None
    else:
        val=l.pop()
        print('Popped element is {} '.format(val))
        if len(l)==0:
            top= None           
        else:
            top = len(l)-1
    return top
def dis(l):
    if len(l)==0:
        print('Underflow')
    else:
        print('Stack elements are : ')
        for i in range(top,-1,-1):
            print(l[i],end='\t')
        print()
l=[]
top= None
ch= 'y'
while ch=='y' or ch=='Y':
    print('Select Stack Opreation')
    print('1 Push')
    print('2 Pop')
    print('3 display')
    op=int(input("Enter your choice : "))
    if op == 1 :
        r=int(input("Enter the roll no. :"))
        n=input("Enter the name :")
        val= [r,n]
        top = push(l,val)
    elif op == 2 :
        top = pop(l)
    elif op == 3 :
        dis(l)
    else:
        print('Wrong Choice !!!!!!!')
    ch= input('Do you want to continue ? y/n ')
print('Thank You :)')