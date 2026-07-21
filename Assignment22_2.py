#Wap that calculates factorials of multiple nos simultaneously ysing Pool.map()
#display: procees id, input number, factorial

import multiprocessing
import os
def factorial(value):
    fact=1
    for i in range(1,value+1):
        fact=fact*i

    return fact

def main():
    data=[]
    result=[]
    a=int(input("Enter no of elemnts"))
    for i in range(a):
        no=int(input())
        data.append(no)
    
    print("Your input numbers are ",data)

    pobj=multiprocessing.Pool()
    result=pobj.map(factorial,data)

    print("The factrials are ",result)

    pobj.close()
    pobj.join()

    print("The process id is ",os.getpid())

if __name__=="__main__":
    main()


