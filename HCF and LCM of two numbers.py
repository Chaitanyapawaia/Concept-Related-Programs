m=int(input("Enter a number:"))
n=int(input("Enter a number:"))
q=1
if m>n:
    o=m
else:
    o=n
for p in range(1,o):
    if m%p==0 and n%p==0 :
        q=q*p
print("HCF is",q, "And LCM is",(m*n)/q)
