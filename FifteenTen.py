filterx=lambda no: no%2==0 

def main():
    data=[2,4,1]
    print("Your input data is",data)

    fd=list(filter(filterx,data))

    count=len(fd)

    print("Your count is",fd)
    print("Your count is",count)

if __name__=="__main__":
    main()
    
   