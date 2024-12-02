class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def getarea(self):
        return self.area
    def findArea(self):
        self.area=self.__length*self.__breadth
    def __lt__(self,other):
        if self.getarea() < other.getarea():
            return True
        else:
            return False
        
        
l1= int(input("enter the lenghth of the first rectangle:"))
l2=int(input("enter the lenghth of the second rectangle:"))
b1=int(input("enter the breadth of the first rectangle:"))
b2=int(input("enter the breadth of the second rectangle:"))
r1=Rectangle(l1,b1)
r2=Rectangle(l2,b2)
r1.findArea()
r2.findArea()
if r1<r2:
    print("The Second  Rectangle is Larger ")
else:
    print("The First Rectangle is Larger")
