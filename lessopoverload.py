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
        
        
l1,b1= map(int,input("enter the lenghth and breadth of the first rectangle:").split())
l2,b2= map(int,input("enter the lenghth and breadth of the Second rectangle:").split())

r1=Rectangle(l1,b1)
r2=Rectangle(l2,b2)
r1.findArea()
r2.findArea()
if r1<r2:
    print("The Second  Rectangle is Larger")
elif r2<r1:
    print("The First Rectangle is Larger")
else:
    print("Two Rectangles are Same")
    
