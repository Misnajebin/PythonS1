class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def gethour(self):
        return self.__hour
    def getminute(self):
        return self.__minute
    def getsecond(self):
        return self.__second
    def __add__(self,other):      
        h=self.gethour()+other.gethour()
        m=self.getminute()+other.getminute()
        s=self.getsecond()+other.getsecond()
        if s>60:
           s-=60
           m+=1
        if m>60:
           m-=60
           h+=1
        if h>24:
           h-=24
        t3=Time(h,m,s)
        return t3
    def display(self):
        print ("hour=",self.__hour)
        print("minute=",self.__minute)
        print("seconds=",self.__second)
        
h1,m1,s1=map(int,input("enter your time in hour,minute,second format:").split())
h2,m2,s2=map(int,input("enter your time in hour,minute,second format:").split())
t1=Time(h1,m1,s1)
t2=Time(h2,m2,s2)
t3=t1+t2
t3.display()
