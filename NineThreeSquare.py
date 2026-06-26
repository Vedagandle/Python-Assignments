def square(Value1,):
    Ans=Value1*Value1
   
    return Ans
    


def main():
    print("Enter your no")
    no1=int(input())
    ret=square(no1)

    print("The squared no is", ret)




if __name__=="__main__":
    main()