#Wap which contains one lambda fun and returns power of two
two=lambda value: value **2  

def main():
    no=int(input("Enter your number"))
    ret=two(no)
    print("The power of two of your number is ",ret)


if __name__=="__main__":
    main()