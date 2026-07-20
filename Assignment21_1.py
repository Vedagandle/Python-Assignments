#create two threads named prime and non prime
#both should accept list of integers
#prime thread should display all prime nos
#non prime thread should display non prime nos

import threading

def prime(no):
    for value in no:
        count=0
    
        for i in range(1,value+1):
            if value%i==0:
                count=count+1

        if count==2:
             print("prime value is ",value)

def nonprime(no):
    for value in no:
        count = 0

        for i in range(1, value + 1):
            if value % i == 0:
                count = count + 1

        if count != 2:
            print("Non prime value is",value)

def main():
    data=[]
    a=int(input("Enter no of elemnts"))
    for i in range(a):
        no=int(input())
        data.append(no)

    t1obj=threading.Thread(target=prime, args=(data,))
    t2obj=threading.Thread(target=nonprime, args=(data,))

    t1obj.start()
    t1obj.join()

    t2obj.start()
    t2obj.join()

if __name__=="__main__":
    main()
    


