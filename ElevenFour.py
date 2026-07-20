def reverse(value):
    reverse=""
    for i in range(value+1,-1,-1):
        print (i)
    
    return reverse

    



def main():
    number=int(input("Enter your number"))
    ret=reverse(number)
    print("Your number is",ret)



if __name__=="__main__":
    main()