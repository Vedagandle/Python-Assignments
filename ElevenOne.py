def prime(value):
    for no in range(2,value):
        if value%no==0:
           return False

            

def main():
    a=int(input("Enter your no"))
    ret=prime(a)
    if ret==False:
        print("It is not a prime no")
    else:
        print("It is a prime number")

if __name__=="__main__":
    main()