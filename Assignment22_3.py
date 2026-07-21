#For every no in the given list , count how many prime nos existe between 1 and N using pool.map()

import multiprocessing

def prime(value):
    count=0
    for no in range(2,value+1):
        factor=0

        for i in range(1,no+1):
            if no%i==0:
                factor=factor+1

        if factor==2:
         count=count+1

    return count
        
def main():
    data=[]
    result=[]
    a=int(input("Enter no of elemnts"))
    for i in range(a):
        no=int(input())
        data.append(no)

    print("Your input data is ",data)

    pobj=multiprocessing.Pool()
    result=pobj.map(prime,data)

    print("The prime nos are ",result)

    pobj.close()
    pobj.join()

if __name__=="__main__":
    main()