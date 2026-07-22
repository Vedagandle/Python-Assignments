#Wap to implement a class named Numbers
#class should contain 1 instance variables: Value
#define constructor init that accepts number from user and initializes value
#implement instance method:
#chkprime()
#chkperfect()
#factors()
#sumfactors()

class numbers:

    def __init__(self,value):
        self.value=value

    def prime(self):
        count=0
        for i in range(1,self.value+1,1):
            if i%self.value==0:
                count=count+1

        if count==2:
            print("Prime number")
        else:
            print("Not a prime number")
    
    def chkperfect(self):
        sum=0
        for i in range(1,self.value+1,1):
            if self.value%i==0:
                sum=sum+i 
        if sum==self.value:
                print("It is a perfect number")
        else:
                print("Not a perfect number")
    
    
    def factors(self):
        for i in range(1,self.value+1,1):
            if self.value%i==0:
                print("Factors are ",i)

    def sumfactors(self):
        sum=0
        for i in range(1,self.value+1,1):
            if self.value%i==0:
                sum=sum+i
        print("The sum is ",sum)

def main():
    no=int(input("Enter your number"))

    nobj=numbers(no)
    nobj.prime()
    nobj.chkperfect()
    nobj.factors()
    nobj.sumfactors()

if __name__=="__main__":
    main()




        



