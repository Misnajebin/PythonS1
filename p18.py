x=int(input("enter the limit:"))
for i in range(1,x+1):
    for j in range(1,i):
        print("*",end=" ")
    print("")
for i in range(x+1,1,-1):
    for j in range(1,i):
        print("*",end=" ")
    print("")
