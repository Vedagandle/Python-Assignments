def nat(no):
    sum=0
    for i in range(1,no+1):
        sum=sum+i
        
    return sum
    


def main():
    print("Enter your no")
    a=int(input())
    ret=nat(a)
    print("your value is",ret)
    


if __name__=="__main__":
    main()