def prime(value):
    for i in range(1,value+1,1):
        if i%11==0:
            
            print("11 is a prime no")
        elif 1%11==11:
          
            print("11 is a prime no")

def main():
    a=int(input("Enter your no"))
    ret=prime(a)

if __name__=="__main__":
    main()