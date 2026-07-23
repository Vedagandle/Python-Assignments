#Wap which accepts the filename from user , opens the file and and display all contents from the file

import os

def main():
    filename=input("Enter your filename")
    ret=os.path.exists(filename)

    if ret==True:
        print("The file is present")

        fobj=open(filename,"r")

        for contents in fobj:
            print(contents)

        fobj.close()

    
    else:
        print("No such file")

if __name__=="__main__":
    main()


