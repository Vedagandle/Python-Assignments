def pos(no):
    if no > 0:
        print("Positive number")
    elif no<0:
        print("Negative number")
    else:
        print("Zero")

def main():
    value=int(input("Enter your number"))
    ret=pos(value)

if __name__=="__main__":
    main()
