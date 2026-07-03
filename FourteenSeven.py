divisiblity=lambda value: True if value%5==0 else False

    
def main():
    no=int(input("Enter your number"))
    ret=divisiblity(no)
    print(ret)

if __name__=="__main__":
    main()