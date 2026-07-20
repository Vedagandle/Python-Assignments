def chknum(no):
    if no%2==0:
        print("Even no")
    else:
        print("Odd no")

def main():
    value=int(input("Enter your number"))
    ret=chknum(value)

if __name__=="__main__":
    main()