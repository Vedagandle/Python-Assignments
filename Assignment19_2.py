#Wap whic contains one lambda fun and accepts two paramters and return its multiplication
mul=lambda value,no:value*no

def main():
    n=int(input("Enter your number"))
    v=int(input("Enter your multiplier"))
    ret=mul(n,v)
    print("Multiplication is ",ret)


if __name__=="__main__":
    main()