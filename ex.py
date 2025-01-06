true=1
i=0
std=[]
company=[]
while(true):    
    name=input("enter the student's name:")
    reg=input("enter the register number:")
    stream=input("enter the stream:")
    company=input("enter the company name:")
    data={"Name":name,"Regno":reg,"stream":stream,"companies":company}
    std[i]=data
    i+=1
    true=int(input("Do yopu want to continue!! 1/0 : "))
    
