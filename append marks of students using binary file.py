import pickle
will='Yes'
while will=='yes' or will=='Yes':
    a= input("Enter 1 to append or 2 to read 3 to write and 4 to update the file : ")
    if a=='1':
        f= open("reportfilebinaryfileclass12.log", "ab")
        b= int(input("Enter rollno. of student :"))
        c= input("Enter name of student :")
        d= int(input("Enter marks of student :"))
        e= input("Enter grade of student :")
        qw= [b,c,d,e]
        pickle.dump(qw,f) 
        f.close()
    if a=='2':
        f= open("reportfilebinaryfileclass12.log", "rb")
        try :
            while True :
                stud= pickle.load(f)
                print(stud[0], stud[1], stud[2], stud[3] )
        except EOFError:
            f.close()
    if a=='3':
        f= open("reportfilebinaryfileclass12.log", "wb")
        sn=int(input("How many record do you want to enter in the file:"))
        for i in range(1,sn+1):
            h= int(input("Enter Roll No. of student:"))
            p= input("Enter Name of student:")
            y= int(input("Enter Marks of student:"))
            t= input("Enter Grade of student:")
            g= [h,p,y,t]
            pickle.dump(g,f)
        f.close()
    if a=='4':
        f= open("reportfilebinaryfileclass12.log", "rb+")
        o= int(input("Enter rollno. of student whose marks need to be updated:"))
        m= int(input("Enter updated marks of student :"))
        try :
            while True :
                p= f.tell()
                stud= pickle.load(f) 
                if stud[0]== o:
                    stud[2]= m
                    f.seek(p)
                    pickle.dump(stud,f)
        except EOFError:
            f.close() 
    will= input("Do You Want To Continue? Press Yes or No:")