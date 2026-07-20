def nodigit(no):
    sum=0
    for i in str(no):
        sum=sum+1

    return sum



def main():
    value=int(input("Enter your number"))
    ret=nodigit(value)
    print("The value is ",ret)


if __name__=="__main__":
    main()