class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,other):
        
        hr=self.__hour+other.__hour
        mint=self.__minute+other.__minute
        sec=self.__second+other.__second
         


        
        
h1,m1,s1=int(input("enter your time in hour,minute,second format:"))
h2,m2,s2=int(input("enter your time in hour,minute,second format:"))
t1=Time(h1,m1,s1)
t2=Time(h2,m2,s2)
