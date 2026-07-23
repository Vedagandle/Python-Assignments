#Wap which accepts a existing filenname from user through command line args
#creates a new file
#copy contents from existing file to new file

import os
import sys

def main():
    filename1=(sys.argv[1])
    filename2=(sys.argv[2])
    ret=os.path.exists(filename1)

    if ret==True:
        print("File is present")

        fobj1=open(filename1,"r")
        fobj2=open(filename2,"w")

        data=fobj1.read()
        fobj2.write(data)

        fobj1.close()
        fobj2.close()

        print("The data is copied")


    else:
        print("No such file")

if __name__=="__main__":
    main()
