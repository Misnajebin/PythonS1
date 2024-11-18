year=int(input("enter the year:"))
if(year%100==0):
    if(year%400==0):
        print(year,"is leap year")
elif(year%4==0):
    print(year,"is leap year")
else:
    print("not a leap year")
