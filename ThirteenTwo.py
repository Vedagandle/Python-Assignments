def areaofcircle(radius,pi):
    area=pi*radius*radius
    return area

def main():
    number1=int(input("Enter your radius"))
    number2=float(input("Enter the pi value"))
    ret=areaofcircle(number1,number2)
    print("Area of radius is",ret)

if __name__=="__main__":
    main()
