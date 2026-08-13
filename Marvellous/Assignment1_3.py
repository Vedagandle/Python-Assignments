def add(no1,no2):
    sum=no1+no2
    return sum

def main():
    value1=int(input("Enter your number"))
    value2=int(input("Enter you number"))
    ret=add(value1,value2)
    print("Your addition is",ret)

if __name__=="__main__":
    main()