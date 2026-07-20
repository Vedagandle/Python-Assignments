def display(no):
    for i in range(no,0,-1):
        print(i)

def main():
    value=int(input("Enter your no"))
    ret=display(value)

if __name__=="__main__":
    main()