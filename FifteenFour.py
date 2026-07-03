from functools import reduce

reduceX=lambda no1,no2:no1+no2

def main():
    data=[1,2,3]
    print("Your input data is",data)

    reducedData=reduce(reduceX,data)
    print("Your reduced data is ",reducedData)

if __name__=="__main__":
    main()