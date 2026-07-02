def addition(value1,value2):
    sum=value1+value2
    return sum

def multiplication(value1,value2):
    mult= value1*value2
    return mult 

def division(value1,value2):
    div=value1/value2
    return div


def main():
    number1=int(input("Enter your number"))
    number2=int(input("Enter your number"))
    ret=addition(number1,number2)
    print("Your addition are",ret)

    ret=multiplication(number1,number2)
    print("Your multiplication are",ret)

    ret=division(number1,number2)
    print("Your division are",ret)

if __name__=="__main__":
    main()