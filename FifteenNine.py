from functools import reduce

reducex= lambda no1,no2: no1*no2

def main():
    data=[1,2,4]
    print("Your input data is",data)

    reducedData=reduce(reducex,data)
    print("Your reduced data is",reducedData)

if __name__=="__main__":
    main()
   