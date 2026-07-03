filterX=lambda no: no%2==0
        
    
def main():
    data=[1,3,4,6]
    print("Your input data is",data)

    filteredData=list(filter(filterX,data))
    print("Your filtered Data is",filteredData)

if __name__=="__main__":
    main()