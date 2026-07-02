def reverse(value):
    reverse=""
    for no in value:
        reverse=no+reverse
    
    return reverse

    



def main():
    number=input("Enter your number")
    ret=reverse(number)
    print("Your number is",ret)



if __name__=="__main__":
    main()