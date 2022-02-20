a=open("Marks.txt",'a+')
for c in range (2):
    d= input('Enter the roll number:')
    e= input('Enter the name:')
    f= input('Enter the marks:')
    h='\n'
    a.write(d+','+e+','+f+h)
a.seek(0)
g=a.read()
print('The data is:')
print(g)
