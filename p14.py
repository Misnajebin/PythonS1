n=int(input("Enter the number of terms(min 3) : "))
a=1
b=1
c=a+b
i=3
print(a,b,c,end=" ")
while i<n:
    a,b=b,c
    c=a+b
    print(c,end=" ")
    i=i+1
