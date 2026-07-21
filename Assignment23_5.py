#Wap that calculates factorials using pool.map()
#process id, input number , factorial no

import multiprocessing
import os

def factorial(value):
    fact=1
    for i in range(1,value+1,1):
        fact=fact*i
    return (os.getpid(),value,fact)

def main():
     data=[]
     result=[]
     a=int(input("Enter no of elemnts"))
     for i in range(a):
        no=int(input())
        data.append(no)

     pobj=multiprocessing.Pool()
     result=pobj.map(factorial,data)
     pobj.close()
     pobj.join()

     for pid,no,fact in result:
        print("Your pid is ",pid)
        print("Your input number is ",no)
        print("Your factorial is ",fact)
       
  

  
if __name__=="__main__":
    main()