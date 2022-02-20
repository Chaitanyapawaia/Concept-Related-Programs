line = input ( "Enter a line :") 
lowercount = uppercount = 0
digitcount = alphacount = spacecount= 0

for a in line :
    if a.islower(): 
        lowercount += 1 
    elif a.isupper():
        uppercount += 1 
    elif a.isdigit():
        digitcount += 1 
    elif a.isspace():
        spacecount+= 1
    if a.isalpha() : 
        alphacount += 1
    
print("Number of uppercase letters :" , uppercount) 
print("Number of lowercase letters :", lowercount) 
print("Number of alphabets :", alphacount) 
print("Number of digits :", digitcount)
print("Number of spaces :", spacecount)    
