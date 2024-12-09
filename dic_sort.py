n=int(input("Enter the size of the dictionary :"))
i=0
d={}
for i in range(i,n):
    key=str(input("Enter the key : "))
    value = int(input("Enter corresponding value :"))
    d[key]=value
    
k = list(d.keys())
k.sort()
print("The dictionary in  ascending order :")
for i in k:
    print(i," : ",d[i])
    
    
