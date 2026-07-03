max=lambda value1,value2:value1 if value1>value2 else value2

    

def main():
    no1=int(input("Enter your 1 no"))
    no2=int(input("Enter your 2 number"))
    ret=max(no1,no2)
    print("Max value is",ret)


if __name__=="__main__":
    main()