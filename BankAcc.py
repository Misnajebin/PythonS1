class BankAccount:
    def  __init__(self,name,accno,acctype):
        self.name=name
        self.accno=accno
        self.acctype=acctype
        self.balance=0
    def setname(self,name):
        self.name=name
    def setaccno(self,accno):
        self.accno=accno
    def settype(self,acctype):
        self.acctype=acctype
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
   
    def getbalance(self):
        return self.balance
    def display(self):
        print("----------------------------")
        print("Name=",self.name)
        print("Account no=",self.accno)
        print("Account type=",self.acctype)
        print("Balance =",self.balance)
        print("----------------------------")

name =str(input("Enter Your Name :"))
accno =int(input("Enter Your Account No :"))
c =int(input("Enter Your Account Type (1.Savings / 2.Current):"))
if c==1:
    acctype="Savings"
else:
    acctype="Current"
bnk =BankAccount(name,accno,acctype)

while 1:
    print("---------------------------------------------")
    print("Bank Operations")
    print("1.Account Details")
    print("2.Cash Deposit")
    print("3.Cash Withdraw")
    print("4.Bank Balance")
    print("5.Exit")
    print("----------------------------------------------")
    c= int (input("Enter the choice :"))
    if c==1:
        bnk.display()
    elif c==2:
        a=int(input("Enter the amount to deposit:"))
        bnk.deposit(a)
    elif c==3:
        b=bnk.getbalance()
        if b<=0:
            print("Your Account has no sufficient balance!!")
        else:
            a=int(input("enter the amount to withdraw:"))
            if a>b:
                print("Sorry ,You don't have money!!")
            else:
                bnk.withdraw(b)
    elif c==4:
        print("Balance =",bnk.getbalance())
    elif c==5:
        break
    else:
        print("Enter a Valid Choice !!!!")
    
        
        
        
        
    
