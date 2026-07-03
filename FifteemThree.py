filterX=lambda no:no%2==1
    
    
def main():
    data=[1,3,2,4,6]
    print("Your input data is",data)
     
    filteredData=list(filter(filterX,data))
    print("Your filtered data is",filteredData)

if __name__=="__main__":
    main()