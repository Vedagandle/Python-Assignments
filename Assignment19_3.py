#Wap which has filter,map,reduce.It contains list of numbers accepted from user.
# Filter should filter such numbers that are greater than or equal to 70 and less than or equal to 90
#Map funtion will increase each number by 10
#reduce will give product of all numbers in list



from functools import reduce

fil=lambda value:True if value>=70 and value<=90 else False
mapp=lambda value:value+10
pr=lambda x,y:x*y



def main():
    data=[]
    userelements=int(input("Enter no of elements"))
    for i in range(userelements):
        no=int(input())
        data.append(no)

    print("Input data is ",data)

    filteredData=list(filter(fil,data))
    print("Your filtered data is ",filteredData)

    mappedData=list(map(mapp,filteredData))
    print("Your mapped data is ",mappedData)

    reducedData=reduce(pr,mappedData)
    print("Your reduced data is ",reducedData)










if __name__=="__main__":
    main()