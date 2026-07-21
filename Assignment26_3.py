#Wap to implement a class named Arithmatic
#should contain 2 instance variables: value1 and value2
#define a constructor init that initializes all instance variables to 0
#Implement  instance methods: 
# accept()=accept value1 and value2 from user
# addition()=returns addition of value1 anf value2
#subtraction()=returns sub of value1 anf value2
#multiplication()=returns mul of value1 anf value2
#division()=returns div of value1 anf value2
#create multiple objects of class

class Arithmatic:
    

    def __init__(self):
        self.value1=0
        self.value2=0

    def accept(self):
        self.value1=int(input("Enter your 1 no"))
        self.value2=int(input("Enter your 2 no"))

    def add(self):
        addition=self.value1+self.value2
        print("Addition is ",addition)
    
    def sub(self):
        subtraction=self.value1-self.value2
        print("Subtraction is ",subtraction)

    def mul(self):
        multiplication=self.value1*self.value2
        print("Multiplication is ",multiplication)
        
    def div(self):
        division=self.value1/self.value2
        print("Division is ",division)

def main():

    aobj=Arithmatic()
    aobj.accept()
    aobj.add()
    aobj.sub()
    aobj.mul()
    aobj.div()

if __name__=="__main__":
    main()


