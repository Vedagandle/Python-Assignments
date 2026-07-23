#Wap which accepts file name from user and counts how many words are present in files

import os

def main():
    filename=input("Enter your filename")
    ret=os.path.exists(filename)

    if ret==True:
        print("The file is present is current directory")
        count=0
        fobj=open(filename,"r")
        for line in fobj:
            words=line.split()        #it will split line into words
            count=count+len(words)   #len because it will be stored in a list format

        fobj.close()
        print("The no of words are",count)
        
    else:
        print("There is no such file")

if __name__=="__main__":
    main()
