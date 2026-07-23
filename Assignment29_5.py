#Wap which accepts a filename and one string from user and returns the count of accurences in that file

import sys
import os

def main():
    filename=(sys.argv[1])
    stringname=(sys.argv[2])
    ret=os.path.exists(filename)
   

    if ret==True:
        print("File is present and word is present")

        fobj=open(filename,"r")

        count=0
        for line in fobj:
            count=count+ line.count(stringname)  #it will check every line and count the word
        print("The occurence is ",count)

        fobj.close()

    else:
        print("No such file")

if __name__=="__main__":
    main()
