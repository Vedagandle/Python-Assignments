#Wap that counts how many odd nos exist between 1 and N using pool.map()
#process id, input number , count of odd no

import multiprocessing
import os

def oddno(value):
    count=0
    for i in range(1,value+1,1):
        if i%2!=0:
            count=count+1
    return (os.getpid(),value,count)

def main():
     data=[]
     result=[]
     a=int(input("Enter no of elemnts"))
     for i in range(a):
        no=int(input())
        data.append(no)

     pobj=multiprocessing.Pool()
     result=pobj.map(oddno,data)
     pobj.close()
     pobj.join()

     for pid,no,count in result:
        print("Your pid is ",pid)
        print("Your input number is ",no)
        print("Your odd no count is ",count)
       
  

  
if __name__=="__main__":
    main()