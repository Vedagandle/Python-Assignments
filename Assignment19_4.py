#Wap which contains filter , map , reduce in it.
# Python application which contains one list of numbers, which are accepted from the user. 
# Filter should filter out numbers that are even. 
# Map should calculate the square of numbers.
#  Reduce will return addituion of numbers.
from functools import reduce
fil=lambda value:True if value%2==0 else False
mapp=lambda value:value**2
add=lambda x,y:x+y



def main():
    data=[]
    a=int(input("Enter no of elements you want in the list"))
    for i in range(a):
        no=int(input())
        data.append(no)

    print("Your input data is",data)

    filteredData=list(filter(fil,data))
    print("Your filtered data is ",filteredData)

    mappedData=list(map(mapp,filteredData))
    print("Your mapped data is ",mappedData)

    reducedData=reduce(add,mappedData)
    print("Your reduced data is ",reducedData)




if __name__=="__main__":
    main()