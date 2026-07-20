def addlist(value):
    sum=0
    for i in value:
        sum=sum+i
    return sum
  


def main():
    data=[]
    no=int(input("Enter 6 numbers"))
    for i in range(no):
        n=int(input())
        data.append(n)

    ret=addlist(data)
    print("Adiition is ",ret)


if __name__=="__main__":
    main()