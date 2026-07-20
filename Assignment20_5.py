#create 2 threads thread1 and thread2
#thread1 should display no from 1-50
#thread2 should display no from 50-1
#thread2 starts the execution only after thread1 completes its execution

import threading

def forward():
    for i in range(1,51,1):
        print(i)

def reverse():
    for i in range(51,0,-1):
        print(i)

def main():
    t1obj=threading.Thread(target=forward)
    t2obj=threading.Thread(target=reverse)

    t1obj.start()
    t1obj.join()

    t2obj.start()
    t2obj.join()

if __name__=="__main__":
    main()
