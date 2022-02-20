ch="y"
while ch=="y" or ch=="Y":
    print("Press 1 to append the data")
    print("Press 2 to view the data")
    print("Press 3 to write the data")
    a= int(input("Enter Your Input:"))
    if a==1:
        f= open("reportfiletextfileclass12.txt", "a")
        b= int(input("Enter the number of data entry:"))
        for c in range(1,b+1):
            rollno=input("Enter the Roll No. :")
            name= input("Enter the Name :")
            marks= input("Enter the Marks :")
            d= rollno+","+name+","+marks+"\n"
            f.write(d)
            f.flush()
        f.close()
    if a==2:
        f= open("reportfiletextfileclass12.txt", "r")
        f.seek(0)
        e= f.read()
        print(e)
        f.close()
    if a==3:
        f= open("reportfiletextfileclass12.txt", "w")
        sn=int(input("How many record do you want to enter in the file:"))
        for i in range(1,sn+1):
            h= input("Enter Roll No. of student:")
            p= input("Enter Name of student:")
            y= input("Enter Marks of student:")
            t= input("Enter Grade of student:")
            g= h+","+p+","+y+","+t+"\n"
            f.write(g)
            f.flush()
        f.close()
        
    ch= input("Do you want to continue? Y or N: ")

            


        
        
        