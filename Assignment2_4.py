def addno(no):
    sum=0
    for i in range(1,no):
        if no%i==0:
            sum=sum+i

    return sum


def main():
    value=int(input("Enter your number"))
    ret=addno(value)
    print("Addition is ",ret)

if __name__=="__main__":
    main()