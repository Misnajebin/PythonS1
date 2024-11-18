str2=input("Enter your string: ")
str1=str2.lower()
x=input("Enter your element to search:")
c=0
for i in str1:
    if x==i:
        c=c+1
print("Frequency of",  x ," is : ", c )
    
