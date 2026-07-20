#creates 2 threads sum and product
#return results to main thread and display them

import threading

sum_result=0
mul_result=0

def sum(value):
    global sum_result

    sum=0
    for i in value:
        sum=sum+i
    sum_result=sum

def product(value):
    global mul_result
    mul=1
    for i in value:
        mul=mul*i
    mul_result=mul

def main():
    data=[]
    a=int(input("Enter no of elemnts"))
    for i in range(a):
        no=int(input())
        data.append(no)

    t1obj=threading.Thread(target=sum, args=(data,))
    t2obj=threading.Thread(target=product, args=(data,))

    t1obj.start()
    t1obj.join()

    t2obj.start()
    t2obj.join()

    print("The sum is ",sum_result)
    print("The product is ",mul_result)

if __name__=="__main__":
    main()