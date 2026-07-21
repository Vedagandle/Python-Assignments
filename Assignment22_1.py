#Wap that accepts a list of integers and uses pool.map() to calculate the sum of squares from 1 element to n elemnt in the list

import multiprocessing

def sumsquare(value):
    sum=0
    for i in range(1,value+1):
        sum=sum+(i**2)

    return sum

def main():
    data=[]
    result=[]
    a=int(input("Enter no of elemnts"))
    for i in range(a):
        no=int(input())
        data.append(no)

    pobj=multiprocessing.Pool()
    result=pobj.map(sumsquare,data)

    print("The sum of square is ",result)

    pobj.close()
    pobj.join()

if __name__=="__main__":
    main()