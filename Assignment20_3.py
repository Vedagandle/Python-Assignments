#Create threads evenlist and odd list
#both should accept list of integers as input
#evenlist should: extract even elements from list, cal and siplay their sum
#oddlist should: extract odd elements from list, cal and siplay their sum
#thread should run concurrently

import threading

def evenlist(value):
    sum=0
    for i in value:
       if i%2==0:
           print(i)
           sum=sum+i
    print("Even sum is",sum)

def oddlist(value):
    sum=0
    for i in value:
       if i%2!=0:
           print(i)
           sum=sum+i
    print("odd sume is",sum)

def main():
    data=[]
    a=int(input("Enter no of elemnts"))
    for i in range(a):
        no=int(input())
        data.append(no)

    print("Your input data is ",data)

    t1obj=threading.Thread(target=evenlist,args=(data,))
    t2obj=threading.Thread(target=oddlist,args=(data,))

    t1obj.start()
    t2obj.start()

    t1obj.join()
    t2obj.join()

if __name__=="__main__":
    main()
