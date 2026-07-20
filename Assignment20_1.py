#Has two seperate threads named even and odd
#Even thread should display first 10 even numbers
#Odd thread should display first 10 odd numbers
#both threads should execute independently using threading module

import threading

def even():
    for i in range(2,21,2):
        print(i)


def odd():
    for i in range(1,20,2):
        print(i)


def main():

    t1obj=threading.Thread(target=even)
    t2obj=threading.Thread(target=odd)

    t1obj.start()
    t2obj.start()

    t1obj.join()
    t2obj.join()

if __name__=="__main__":
    main()