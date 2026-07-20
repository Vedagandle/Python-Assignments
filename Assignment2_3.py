#input=5    fact=120

def fact(no):
    sum=1
    for i in range(1,no+1):
        sum=sum*i
    
    return sum


def main():
    value=int(input("Enter your number"))
    ret=fact(value)
    print("Factorial is",ret)


if __name__=="__main__":
    main()