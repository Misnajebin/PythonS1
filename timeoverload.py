class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,other):      
        h=self.__hour+other.__hour
        m=self.__minute+other.__minute
        s=self.__second+other.__second
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
        print ("hour=",self.h)
        print("minute=",self.m)
        print("seconds=",self.s)
        
h1,m1,s1=map(int,input("enter your time in hour,minute,second format:").split())
h2,m2,s2=map(int,input("enter your time in hour,minute,second format:").split())
t1=Time(h1,m1,s1)
t2=Time(h2,m2,s2)
t3=t1+t2
t3.display()
