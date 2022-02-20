def simpint(p,t=2,r= 0.10):
    print("The simple interest is", p*r*t/100)
def compint(p,t=2,r= 0.10,n=5):
    print(" The compound interest is", p*((1+(r/n))**(n*t)))
w="y" 
while w=="y" or w=="Y":
    print("Press 1 to calculate simple interest \n 2 to calculate compound interest ")
    q= int(input("Enter your choice:"))
    if q== 1:
        p= int(input("Enter the principle interest:"))
        r= float(input("Enter the rate of interest (default rate 0.10):"))
        t= int(input("Enter the time period (default time 2):"))
        print("With default values")
        simpint(p)
        print("With specified values")
        simpint(p,r,t)
    if q== 2:
        n= int(input("Enter the number of compound periods (default periods 5) :"))
        p= int(input("Enter the principle interest:"))
        r= float(input("Enter the rate of interest (default rate 0.10):"))
        t= int(input("Enter the time period (default time 2):"))
        print("With default values")
        compint(p)
        print("With specified values")
        compint(p,t,n,r)
    w= input("Do you want to continue press Y : ")

