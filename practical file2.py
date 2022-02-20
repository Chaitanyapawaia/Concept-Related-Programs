q=eval(input("Enter a list:"))
i=len(q)
r= i-1
u=0
while (u<=r):
    w=q[u]
    if w ==0:
        for e in range (u,r):
            q[e]=q[e+1]
        else:
            q[r]=0
            r=r-1
    if q[u]!= 0:
        u=u+1
print(q)

o= int(input("Enter your weight in kg:"))
p=int(input("Enter your height in centimetre:"))
a=(p/100)**2
s=o/a
if s< 18.5 :
    print("Your BMI is", s, "You are underweight")
if s> 25:
    print("Your BMI is", s, "You are overweight")
if s> 18.5 and s< 25 :
    print("Your BMI is", s, "You are normal")


d=int(input("Enter a number:"))
v=d
h=0
while d>0:
    g= d%10
    h=h*10+g
    d=d//10
if h==v:
    print("The number is a palindrome number")
if h!=v:
    print("The number in not a palindrome number")



j=int(input("Enter a number:"))
k= len(str(j))
c=j
z=0
while c>0 :
    b=c%10
    n=b**k
    z=z+n
    c=c//10
if z==j:
    print("The number is an armstrong number")
if z!=j:
    print("The number in not an armstrong number")


