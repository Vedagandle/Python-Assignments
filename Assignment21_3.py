#multiple threads update shared variable
#use lock to avoid race conditions
#each thread shoul increment the shared counter multiple times
#display final value of counter after execution of all threads

import threading

counter = 0                 #shared variable
lock = threading.Lock()

def increment():
    global counter

    for i in range(1000):
        lock.acquire()                #locked so that only 1 thread can update
        counter = counter + 1
        lock.release()                #unlocked so that both threads can update

def main():

    t1obj = threading.Thread(target=increment)
    t2obj = threading.Thread(target=increment)

    t1obj.start()
    t2obj.start()

    t1obj.join()
    t2obj.join()

    print("Final value of counter is :", counter)

if __name__ == "__main__":
    main()