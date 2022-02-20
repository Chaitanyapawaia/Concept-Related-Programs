a= int(input('Enter the day number between 2 to 365:'))
b= input('Enter the day on 1:')
c=a%7
f=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
g=f*2
h=g.index(b)
i=int(h)+c
print(g[i])
