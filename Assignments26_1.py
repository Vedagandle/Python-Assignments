#Wap to implement a class named demo
#should contain 2 instance variables: no1,no2
#class should contain one class variable: value
#define a constructor init which accepts 2 parameters and initializes the instance variables
#Implement 2 instance methods: 
# fun()=display values of isntance variable no1,no2 and gun()=display values of isntance variable no1,no2
#create 2 objects of demo class:
#obj1=demo(11,21) and #obj2=demo(51,101)
#call instance methods

class demo:
    value=10   #class variables
    

    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2

    def fun(self):
        print("Inside fun")
        print(self.no1)
        print(self.no2)

    def gun(self):
        print("Inside gun")
        print(self.no1)
        print(self.no2)

dobj1=demo(11,21)
dobj2=demo(51,101)

dobj1.fun()
dobj2.fun()

dobj1.gun()
dobj2.gun()
