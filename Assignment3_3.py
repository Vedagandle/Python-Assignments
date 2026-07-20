def maximun(value):
    max=value[0]
    for i in value:
       if i<max:
        max=i

    return max




def main():
    data=[]
    no=int(input("Enter no of elements"))
    for i in range(no):
        n=int(input())
        data.append(n)

    ret=maximun(data)
    print("Minimum value is ",ret)

if __name__=="__main__":
    main()