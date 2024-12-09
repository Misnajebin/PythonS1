x=input("enter the word:")
y=input("ente the character to be counted:")
flag=0;
for i in x:
    if(i==y):
        flag=flag+1
print(f"{y} appears {flag} times")
