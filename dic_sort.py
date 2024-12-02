n=int(input("Enter the size of the dictionary :"))
d ={}
i=0
while i<n:
    key=str(input("Enter the key : "))
    value = int(input("Enter corresponding value :"))
    d[key]=value
    i=i+1

k = list(d.keys())
k.sort()
print("The dictionary in  ascending order :")
for i in k:
    print(k," : ",d[i])
    
    
