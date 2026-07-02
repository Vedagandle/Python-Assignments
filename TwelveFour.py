def ordernum(value):
    for i in range(1,value+1,1):
        print(i)



def main():
    number=int(input("Enter your number")) 
    ret=ordernum(number)

if __name__=="__main__":
    main()