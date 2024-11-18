def fact(n):
    for i in range (n-1,0,-1):
        n=n*i
    return n
a=int(input("Enter the number : "))
if a==0 or a==1:
    print("Facorial of",a,"is 1")
elif a>0:
    print("Factorial of ",a,"is",fact(a))
else:
    print("Cannot find the factorial of the given number")


