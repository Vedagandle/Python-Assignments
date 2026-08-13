def divisibility(no):
    if no%5==0:
        return True
    else:
        return False
    
    
def main():

    value=int(input("Enter your number"))
    ret=divisibility(value)
    if ret==True:
        print("True")
    else:
        print("False")
    

if __name__=="__main__":
    main()
