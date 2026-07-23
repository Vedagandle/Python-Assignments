#Wap while aaccepts two filenames from user
#First file is a existing
#2 file is new one
#copy contents from 1 file into 2 file

import os
filename1=input("Enter file name")
filename2=input("Enter file name")
ret1=os.path.exists(filename1)
ret2=os.path.exists(filename2)

def main():
    if ret1==True:
        print("File is present")
        fobj=open(filename1,"r")

        fobj1=open(filename2,"w")

        data=fobj.read()
        fobj1.write(data)

        fobj.close()
        fobj1.close()
        print("The data is copied")

    else:
        print("No file present")

if __name__=="__main__":
    main()

