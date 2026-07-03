checkeven=lambda value1:True if value1%2==0  else False

def main():
    no=int(input("Enter number"))
    ret=checkeven(no)
    print("Even no",ret)
    
if __name__=="__main__":
    main()
