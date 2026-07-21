#Wap to implement a class named circle
#should contain 3 instance variables: radius,area,circumference
#class should contain one class variable: PI=3.14
#define a constructor init that initializes all instance variables to 0.0
#Implement  instance methods: 
# accept()=accept radius of circle from user
# calculatearea()=calculate area and store it in Area variable
#calculatecir()=calulate the cir and store it in Circumference variable
#display()=values of radius,area,circumference
#create multiple objects of class

class circle:
    PI=3.14

    
    def __init__(self):
        self.radius=0.0
        self.area=0.0
        self.circumference=0.0

    #instance method
    def accept(self):
        self.radius=int(input("Enter your radius"))

    def calculatearea(self):
        self.area=circle.PI*self.radius*self.radius

    def circum(self):
        self.circumference=2*circle.PI*self.radius

    def display(self):
        print("Your radius is ",self.radius)
        print("Your area is ",self.area)
        print("Your circumfernce is ",self.circumference)

def main():
    obj=circle()

    obj.accept()
    obj.calculatearea()
    obj.circum()
    obj.display()

if __name__=="__main__":
    main()




