#Wap using multiprocessing.pool() to calculate sum of odd nos from 1 to n for every no in list
#process id, input number , sum of even no

import multiprocessing
import os

def even(value):
    sum=0
    for i in range(1,value+1,2):
        sum=sum+i
    return (os.getpid(),value,sum)

def main():
    
    data=[]
    result=[]
    a=int(input("Enter no of elemnts"))
    for i in range(a):
        no=int(input())
        data.append(no)

    pobj=multiprocessing.Pool()
    result=pobj.map(even,data)
    pobj.close()
    pobj.join()

    
    for pid,no,sum in result:
        print("Your pid is ",pid)
        print("Your input number is ",no)
        print("Your addition is ",sum)
       
  

  
if __name__=="__main__":
    main()

    