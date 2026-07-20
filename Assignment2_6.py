def ppattern(no):
    for i in range(no):          #i=rows
        for j in range(i,no):    #j=column
            print("*",end=" ")
        print()


def main():
    value=int(input("Enter your no"))
    ret=ppattern(value)


if __name__=="__main__":
    main()