import csv
f= open('reportfiletcsvfileclass12.csv', 'a+', newline='')
writer = csv.writer(f)
will='Yes'
while will=='yes' or will=='Yes':
    a= input("Enter 1 to append or 2 to read the file:")
    if a=='1':
        qw=int(input("How many record do you want to enter in the file:"))
        for i in range(1,qw+1):
            a= input("Enter Roll No. of student:")
            b= input("Enter Name of student:")
            c= input("Enter Marks of student:")
            d= input("Enter Grade of student:")
            g= [a,b,c,d]
            writer.writerow(g)
            f.flush()
    if a=='2':
        f.seek(0)
        reader = csv.reader(f)
        for row in reader:
            print(row)
    will= input("Do You Want To Continue? Press Yes or No:")         
f.close()
    
    
   