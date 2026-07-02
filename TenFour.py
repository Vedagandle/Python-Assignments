def even(value1):
    result=[]
    for i in range(1,value1+1,1):
        if i%2==0:
            print(i)

           

   
def main():
    
    a=int(input("Enter your no"))
    ret=even(a)

if __name__=="__main__":
    main()