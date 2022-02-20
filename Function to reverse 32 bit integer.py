
def reverse(x):
        """
    :type x: int
    :rtype: int
        """
    if x<0:
        a=(int(str(x*(-1))[::-1]))*(-1)
    else:
        a=int(str(x)[::-1])
                
    if a<((2**31)*(-1)) or a>((2**31)-1):
        return 0
    else:
        return a     
        
print(reverse(1534236469))
