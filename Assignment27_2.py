#Wap to implement a class named Bankaccount
#class should contain 2 instance variables: name, balance
#class should contain 1 class variable: ROI initilaized to 10.5
#define constructor init that accepts name and initial amount
#implement instance method:
#display()=acc holder name and current balance
#withdraw()=accepts amt from user and subtracts it from balance..(only if succficient bal)
#calinterest()=returns interst=amt*roi/100

class BankAccount:
    ROI=10.5

    def __init__(self,name,amount):
        self.name=name
        self.amount=int(amount)

    def display(self):
        print("Account holder name is ",self.name)
        print("Current balance is ",self.amount)
       

    def withdraw(self):
        self.amt=int(input("Enter your amount"))
        if self.amt<=self.amount:
            self.amtt=self.amount-self.amt
            print("Your current balance is",self.amtt)
        else:
            print("Insuffiecient balance")
    
    def calinterest(self):
        self.interest=(self.amount*BankAccount.ROI)/100
        return self.interest

def main():
    accname=input("Enter your name")
    balance=input("Enter your amount")

    bobj=BankAccount(accname,balance)
    bobj.display()
    bobj.withdraw()
    bobj.calinterest()

if __name__=="__main__":
    main()
        