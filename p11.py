a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
if a<b:
    for i in range(a,0,-1):
        if (a%i==0 and b%i==0):
            print("GCD = ",i)
            break            
elif b<a:
    for i in range(b,0,-1):
        if (a%i==0 and b%i==0):
            print("GCD = ",i)
            break
else:
    print("GCD =",a)
            

