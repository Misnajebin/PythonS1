a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b:
    if a>c:
        print("largest is",a)
    else:
        print("largest is",c)
elif b>c:
    print ("largest is",b)
else:
    print("largest is",c)
