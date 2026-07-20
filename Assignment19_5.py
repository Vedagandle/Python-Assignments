#Wap which has filter,map,reduce in it.
#It should have list which accepts nos from user
#Filter should filter out prime nos
#map should multiply each number by 2
#reduce will return max number from all
from functools import reduce
def prime(no):
    for i in range(2,no):
        if no%i==0:
            return False
      
    return True
        
def mul(no):
  return no*2

def max(x,y):
    if x>y:
        return x
    else:
        return y

def main():
    data=[]
    n=int(input("Enter no of elemnts in list"))
    for i in range(n):
        no=int(input())
        data.append(no)

    print("Your input list is ",data)

    filteredDta=list(filter(prime,data))
    print("Ypur filtered data is ",filteredDta)

    mappedData=list(map(mul,filteredDta))
    print("Your mapped data is ",mappedData)

    reducedData=reduce(max,mappedData)
    print("Your reduced data is ",reducedData)


if __name__=="__main__":
    main()