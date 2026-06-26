def Greater(Value1,Value2):
    if(Value1>Value2):
        print("The greater value is ", Value1)
    else:
        print("The greater value is ", Value2)


def main():
    print("Enter your number")
    no1=int(input())
    print("Enter your number")
    no2=int(input())
    
    ret=Greater(no1,no2)



if __name__=="__main__":
    main()

