#create 2 threads min and max
#min thread should return minimun no
#max thread shoul return max number
#it should accept list from user


import threading

def max(value):
    max=value[0]
    for i in value:
       if i>max:
            max=i
    print("Maximun number is ",max)

def min(value):
    min=value[0]
    for i in value:
        if i<min:
            min=i
    print("Minimum data is ",min)

def main():
    data=[]
    a=int(input("Enter no of elemnts"))
    for i in range(a):
        no=int(input())
        data.append(no)

    t1obj=threading.Thread(target=max,args=(data,))
    t2obj=threading.Thread(target=min,args=(data,))

    t1obj.start()
    t1obj.join()

    t2obj.start()
    t2obj.join()

if __name__=="__main__":
    main()