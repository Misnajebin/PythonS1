a=int(input("enter first number"))
b=int(input("enter second number"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
c=int(input("enter the choice"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
else:
    print("invalid")
