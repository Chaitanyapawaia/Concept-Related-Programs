info = eval(input("Enter the dictionary:"))
inp=input("Enter value to be searched for :")
for a in info:
    if info[a].upper() == inp.upper(): 
        print("The key of given value is", a) 
        break
else:
    print("Given value does not exist in dictionary")
    