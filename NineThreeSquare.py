def square(Value1):
    value1=Value1*Value1
   
    return value1
    


def main():
    print("Enter your no")
    no1=int(input())
    ret=square(no1)

    print("The squared no is", ret)




if __name__=="__main__":
    main()