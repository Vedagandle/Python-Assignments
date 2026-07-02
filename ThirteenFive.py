def grade(value1):
    if value1>=75:
        print("Distinction")
    elif value1>=60:
        print("First Class")
    elif value1>=50:
        print("Second class")
    elif value1<50:
        print("Fail")

def main():
    number=int(input("Enter your 1 number"))
    ret=grade(number)

if __name__=="__main__":
    main()
 
