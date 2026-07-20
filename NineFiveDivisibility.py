def divisibility(Value1):
    if(Value1%3==0 and Value1%5==0):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible")



def main():
    no1=int(input("Enter your number"))
    ret=divisibility(no1)

if __name__=="__main__":
    main()