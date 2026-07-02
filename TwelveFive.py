def ordernum(value):
  
    for i in range(value,0,-1):
       
        print(i)



def main():
    number=int(input("Enter your number")) 
    ret=ordernum(number)

if __name__=="__main__":
    main()