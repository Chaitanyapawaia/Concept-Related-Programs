list=eval(input("Enter a list : "))
ch= "y"
print("Press \n 1 to append \n 2 to find index \n 3 to extend \n 4 to insert \n 5 to pop \n 6 to remove \n 7 to clear \n 8 to count \n 9 to reverse \n 10 to sort ")
while ch== "y" or ch== "Y" :
    choice=int(input("Enter your choice : "))
    if choice== 1:
        a=int(input("Enter the element : "))
        list.append(a)
    if choice ==2:
        a=int(input("Enter the element : "))
        print(list.index(a))
    if choice == 3:
        list1=eval(input("Enter a list : "))
        list.extend(list1)
    if choice == 4:
        pos= int(input("Enter the position : "))
        item= int(input("Enter the element : ")) 
        list.insert(pos, item)
    if choice == 5:
        a=int(input("Enter the index : "))
        list.pop(a)
    if choice == 6:
        a=int(input("Enter the element : "))
        list.remove(a)
    if choice ==7:
        list.clear()
    if choice == 8:
        a=int(input("Enter the element : "))
        print(list.count(a))
    if choice == 9:
        list.reverse()
    if choice == 10:
        list.sort()
    print(list)
    ch=input("Press 'y' to continue : ")
    