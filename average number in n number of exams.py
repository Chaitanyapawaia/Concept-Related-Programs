num_subjects= int(input("How many subjects are you taking? "))
sum= 0
for index in range (num_subjects):
    prompt="Enter marks for subjects#" + str(index+1)+":"
    marks= int(input("Enter the marks: "))
    sum = (sum) + marks
average= sum/num_subjects
print("the average is",average)
