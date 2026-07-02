def multi(value1):
    for no in range(1,11):
        mul=value1*no
        print("your multiplication is",mul)


def main():
    print("Enter your no")
    no=int(input())
    ret=multi(no)
    



if __name__=="__main__":
    main()