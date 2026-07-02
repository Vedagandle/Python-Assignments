def odd(value):
    for i in range(1,value+1,1):
        if i%2==1:
            print(i)

def main():
    print("enter your no")
    a=int(input())
    ret=odd(a)

if __name__=="__main__":
    main()

