#Thre threads named small,capital,digits
#all threads should accept string as their input
#small thread should count and display no of lowercase characters
#capital thread should count and display no of uppercase characters
#small thread should count and display no of digits characters
#each thread should display thread id and thread name

import threading

def small(value):
    count=0
    for i in value:
        if i.islower():
            count=count+1
    print("The count of lower case is ",count)

    print("Id of small thread is ",threading.get_ident())
    print("The name of this thread is ",threading.current_thread().name)

def capital(value):
    count=0
    for i in value:
        if i.isupper():
            count=count+1
    print("The count of upper case is ",count)

    print("Id of captial thread is ",threading.get_ident())
    print("The name of this thread is ",threading.current_thread().name)

def digit(value):
    count=0
    for i in value:
        if i.isdigit():
            count=count+1
    print("The count of digit is ",count)

    print("Id of digit thread is ",threading.get_ident())
    print("The name of this thread is ",threading.current_thread().name)

def main():
    a=input("Enter your string")

    t1obj=threading.Thread(target=small,args=(a,))
    t2obj=threading.Thread(target=capital,args=(a,))
    t3obj=threading.Thread(target=digit,args=(a,))

    t1obj.start()
    t2obj.start()
    t3obj.start()

    t1obj.join()
    t2obj.join()
    t3obj.join()

if __name__=="__main__":
    main()
