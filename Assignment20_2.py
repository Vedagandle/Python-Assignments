#Both threads should accept one integer as parameter
#The evenfactor thread should:identify all even factors, cal and display sum of even factors
#The oddfactor thread should:identify all odd factors, cal and display sum of odd factors
#main thread should display message that exit from main

import threading

def evenfactor(no):
    sum=0
    for i in range(1,no+1):
       if no%i==0 and i%2==0:
           print(i)
           sum=sum+i
    print(sum) 

def oddfactor(no):
    sum=0
    for i in range(1,no+1):
       if no%i==0 and i%2!=0:
           print(i)
           sum=sum+i
    print(sum)


def main():
    a=int(input("Enter your number"))

    t1obj=threading.Thread(target=evenfactor,args=(a,))
    t2obj=threading.Thread(target=oddfactor,args=(a,))

    t1obj.start()
    t2obj.start()

    t1obj.join()
    t2obj.join()

    print("Exit from main")

if __name__=="__main__":
    main()

    
