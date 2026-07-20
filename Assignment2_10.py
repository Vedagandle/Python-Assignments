def addno(value):
    sum=0
    for no in value:
        sum=sum+int(no)

    return sum



def main():
    no=input("Enter your number")
    ret=addno(no)
    print("Addition is ",ret)


if __name__=="__main__":
    main()