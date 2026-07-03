from functools import reduce

reduceX=lambda no1,no2:no1 if no1<no2 else no2
 
def main():
    data=[3,5,7]
    print("Your data is",data)

    reducedData=reduce(reduceX,data)
    print("Min no is ",reducedData)

if __name__=="__main__":
    main()   

