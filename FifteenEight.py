filterX=lambda no:no if no%3==0 and no%5==0 else ""
 
    
def main():
    data=[3,15,5,6,7]
    print("Your inout data is",data)

    filteredData=list(filter(filterX,data))
    print("Your filtered data is",filteredData)

if __name__=="__main__":
    main()