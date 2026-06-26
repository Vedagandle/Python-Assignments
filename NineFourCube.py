def cube(Value1):
    ans=Value1*Value1*Value1
    return ans


def main():
    print("Enter your number")
    no1=int(input())
    ret=cube(no1)
    print("The cube of ypur no is",ret )


if __name__=="__main__":
    main()