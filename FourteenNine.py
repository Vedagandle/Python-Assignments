multiplication=lambda value1,value2:value1*value2

def main():
    no1=int(input("Enter your number"))
    no2=int(input("Enter your number"))
    ret=multiplication(no1,no2)
    print("Your multiplication is",ret)

if __name__=="__main__":
    main()