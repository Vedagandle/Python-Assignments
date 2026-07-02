def area(length,breadth):
    area=length*breadth
    return area


def main():
    no1=int(input("Enter your number"))
    no2=int(input("Enter your number"))
    ret=area(no1,no2)
    print("Your area is ",ret)

if __name__=="__main__":
    main()