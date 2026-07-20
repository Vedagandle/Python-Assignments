from MathsModule import *
def calculations(no1,no2):
    print("Addition is",add(no1,no2)) 
    print("Multiplication is",multi(no1,no2)) 
    print("subtraction is",sub(no1,no2)) 
    print("division is",div(no1,no2)) 

def main():

    value1=int(input("Enter your number"))
    value2=int(input("Enter your number"))
    ret=calculations(value1,value2)
    


if __name__=="__main__":
    main()