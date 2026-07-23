#Wap which accepts file name from user and counts how many lines are present in files


import os      #os module has everything relate oop
def main():
        filename=input("Enter your filename")
        ret=os.path.exists(filename)
    
        if ret==True:
        

         print("File is present in current directory")
        count=0
        fobj=open(filename,"r")
        for line in fobj:
            count=count+1
            print("The no of lines are",count)

        else:
         print("No such file")

if __name__=="__main__":
    main()