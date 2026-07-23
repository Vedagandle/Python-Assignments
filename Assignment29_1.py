#Wap which accepts the filename from user and checks if it is present is current directory or not

import os

def main():
    filename=input("Enter your filename")
    ret=os.path.exists(filename)

    if ret==True:
        print("The file is present in current directory")
       
    else:
        print("Not present in the current directory")

if __name__=="__main__":
    main()