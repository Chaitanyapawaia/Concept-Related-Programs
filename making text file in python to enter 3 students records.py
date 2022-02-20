a=open("Marks.txt",'w+')
b=int(input('Enter the number of students: '))
for c in range (b):
    d= input('Enter the roll number:')
    e= input('Enter the name:')
    f= input('Enter the marks:')
    h='\n'
    a.write(d+','+e+','+f+h)
a.seek(0)
g=a.read()
print('The data is:')
print(g)
