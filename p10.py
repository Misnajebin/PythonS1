import math
a=int(input("Enter the coefficient of x^2:"))
b=int(input("Enter the coefficient of x:"))
c=int(input("Enter the constant:"))
d=(b**2)-(4*a*c)
if d<0:
    print("no solution")
elif d==0:
    result=-b/(2*a)
    print("solution is ",result)
else:
    res1=(-b+(math.sqrt(d)))/(2*a)
    res2=(-b-(math.sqrt(d)))/(2*a)
    print("solutions are ",res1,"and",res2)
