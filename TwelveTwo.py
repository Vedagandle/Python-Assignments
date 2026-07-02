def fact(value):
    for i in range(1,value+1,1):
        if value%i==0:
            print(i)



def main():
    no=int(input("Enter your number"))
    ret=fact(no)

if __name__=="__main__":
    main()