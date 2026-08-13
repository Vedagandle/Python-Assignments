def name(value):
    return (len(value))


def main():
    a=input("Enter your name")
    ret=name(a)
    print("Length of your name is ",ret)

if __name__=="__main__":
    main()