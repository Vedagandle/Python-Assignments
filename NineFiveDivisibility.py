def divisibility(Value1):
    if(Value1/3==0):
        print("Divisible by 3 and 5")
    elif (Value1/5==0):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")


def main():
    no1=16
    ret=divisibility(no1)

if __name__=="__main__":
    main()