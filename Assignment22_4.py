#Wap a program that calculates 1**5+2**5...n**5 using pool
#measure total execution time

import multiprocessing
import time

def cal(value):
    sum=0
    for i in range(1,value+1):
        sum=sum+i**5

    return sum

def main():
    data=[]
    result=[]

    a=int(input("Enter no of elemnts"))
    for i in range(a):
        no=int(input())
        data.append(no)

    start_time=time.perf_counter()

    pobj=multiprocessing.Pool()
    result=pobj.map(cal,data)

    print("Adiition is ",result)

    pobj.close()
    pobj.join()

    end_time=time.perf_counter()

    print("Total time is ",end_time-start_time)

if __name__=="__main__":
    main()
