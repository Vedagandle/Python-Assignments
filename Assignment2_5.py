def prime(no):
    if no<=1:
        return False
    
    for i in range(2,no):
        if no%i==0:
            return False
        else:
            return True
    
def main():
    value=int(input("Enter your no"))
    ret=prime(value)
    if ret==False:
        print("It is not a prime no")
    else:
        print(" a prime no")

if __name__=="__main__":
    main()

        