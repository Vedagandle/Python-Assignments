mapX=lambda no: no*no

def main():
    data=[2,3,4]
    print("Input data is",data)

    mappedData=list(map(mapX,data))
    print("Your mapped data is",mappedData)

if __name__=="__main__":
    main()