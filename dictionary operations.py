dict1=eval(input("Enter a dictionary : "))
ch= "y"
print("Press \n 1 to find length \n 2 to clear \n 3 to get the value \n 4 to print all the items \n 5 to print all the keys \n 6 to print all the values \n 7 to update")
while ch== "y" or ch== "Y" :
    choice=int(input("Enter your choice : "))
    if choice== 1:
        print(len(dict1))
    if choice ==2:
        dict1.clear()
    if choice == 3:
        dict2=input("Enter a key : ")
        print(dict1.get(dict2))
    if choice== 4:
        print(dict1.items())
    if choice == 5:
        print(dict1.keys())
    if choice == 6:
        print(dict1.values())
    if choice ==7:
        dict3=eval(input("Enter to updated dictionary : "))
        dict1.update(dict3)
    print(dict1)
    ch=input("Press 'y' to continue : ")