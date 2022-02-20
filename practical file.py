
'''  Write a python program for the following:
    1        1
    12      21
    123    321
    1234  4321
    1234554321
'''
n= int ( input("enter a number:"))
for i in range (1,n+1):
    for j in range (1,i+1):
        print(j, end=" ")
    for m in range(1,n-j+1):
        print(" ", end=' ')
    for q in range(1,n-j+1):
        print(" ", end=' ')
    for l in range (i,0,-1):
            print(l, end=" ")
    print()


'''Write a python program for the following:
    22
    4444
    666666
    88888888
'''
a= int ( input("enter a number:"))
for b in range (2,a+1,2):
    for c in range (1,b+1):
        print(b, end=' ')
    print()


'''Write a python program to find the average of given numbers of marks'''

num_subjects= int(input("How many subjects are you taking? "))
sum= 0
for index in range (num_subjects):
    prompt="Enter marks for subjects#" + str(index+1)+":"
    marks= int(input("Enter the marks: "))
    sum = (sum) + marks
average= sum/num_subjects
print("the average is",average)


'''Write a python program tp print digits in words from 1 to 9'''

num={1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine" }
digit= int(input("Enter a Digit:"))
print(num[digit])

'''Write a python program to find if an year is a leap year or not and after how many years will it come'''

z=int(input("enter the year="))
y=int(input("enter the current year="))
if(z%4==0):
    u=z-y
    if u==-u :
        print(' The leap year has aldredy passed')
    else:
        print("Yes! It's a leap year and it will come after", u, "years")
else:
    print("NO! It's not a leap year")

    

''' Write a python program to print the fibonacci series '''

f= int(input("Enter a Digit:"))
v=0
r=1
mn=0
ab=0
print( "The fibonacci series is: 0, 1", end=",")
for t in range (3,f+1):
    ab= v+r
    v=r
    r=ab
    print(ab, end=",")
print()

'''Write a python program for the following series:
1-2/2!+4/3!.........
'''

def fact(ty):
    qw=1
    for er in range (1,ty+1):
        qw= qw*er
    return(qw)

ui= int(input("Enter a Digit:"))
op ,sd= 0,1
for fg in range(1, ui):
    op=(2*fg)/ fact(fg+1)
    if (fg%2 !=0):
        op=-op
    sd= sd+op
print("The sum is:",sd)

''' Write a python program to sort a list using insertion sort'''

hjgf= eval(input("enter a list:"))
klnm= len(hjgf)
for zx in range (1,klnm):
    key= hjgf[zx]
    cv=zx-1
    while cv>=0 and key<hjgf[cv]:
        hjgf[cv+1]=hjgf[cv]
        cv=cv-1
    else:
        hjgf[cv+1]= key
print("the list is ",hjgf)


'''Write a python program to recieve a tuple index and print its value'''

qe=eval(input("enter a tuple:"))
bn=int(input("Enter index:"))
print( "the value is:", qe[bn])

'''Write a python program for the following:
       ###########
       #         #
       #         #
       #         #
       #         #
       #         #
       ###########
'''

fde= int(input("Enter a Digit:"))
for den in range (1,fde+1):
    for less in range (1,fde+1):
        if (den==1)or (den==fde) or (less==1) or (less==fde):
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()

