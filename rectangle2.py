class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    

l=10
b=5
r=rectangle(l,b)
r2=rectangle(4,10)
print(r.area())
print(r2.breadth)


