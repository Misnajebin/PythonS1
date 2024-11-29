class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        self.area=self.length*self.breadth
    def perimeter(self):
        self.perimeter=2*(self.length+self.breadth)
    def display(self):
        print("LENGTH:",self.length)
        print("BREADTH:",self.breadth)
        print("AREA :",self.area)
        print("PERIMETER:",self.perimeter)
        print()
    def getarea(self):
        return self.area        
        
L1=int(input("enter your length of first rectangle:"))
L2=int(input("enter your length of second rectangle:"))
B1=int(input("enter your breadth of first rectangle:"))
B2=int(input("enter your breadth of second rectangle:"))
rect1=rectangle(L1,B1)
rect2=rectangle(L2,B2)
rect1.area()
rect1.perimeter()
rect2.area()
rect2.perimeter()
print("----RECTANGLE 1-----")
rect1.display()
print("----RECTANGLE 2-----")

rect2.display()
if(rect1.getarea() > rect2.getarea()):
        print("Rectangle 1 is greater")
elif(rect1.getarea()==rect2.getarea()):
    print("both are equal")
else:
    print("Rectangle 2 is greater")

     
