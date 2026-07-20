def star(no):
    for i in range(no):
        print("*" ,end=" ")

def main():
    value=int(input("Enter your number ypu want to print the no of starts "))
    ret=star(value)

if __name__=="__main__":
    main()
