#Wap which accepts file name from user and display contents of file line by line

import os

def main():
    filename=input("Enter filenamne")
    ret=os.path.exists(filename)

    if ret==True:
        print("The file is present in current directory")

        fobj=open(filename,"r")

        for line in fobj:
            print(line)

        fobj.close()

    else:
        print("No such file")

if __name__=="__main__":
    main()
  



