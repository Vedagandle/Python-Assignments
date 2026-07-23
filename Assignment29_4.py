#Wap which accepts filename from user through commandline
#compare contents of both files

import sys
import os

def main():
    filename1=(sys.argv[1])
    filename2=(sys.argv[2])
    ret=os.path.exists(filename1)
    ret1=os.path.exists(filename2)

    if ret==True and ret1==True :
        print("File is present")

        fobj=open(filename1,"r")
        fobj1=open(filename2,"r")

        for contents in fobj:
            print(contents)
        for line in fobj1:
            print(line)
        if contents==line:
            print("Sucess")
        else:
            print("Failure")

        fobj.close()
        fobj1.close()
    else:
        print("No such file")

if __name__=="__main__":
    main()
