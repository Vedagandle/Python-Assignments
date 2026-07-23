#Wap which accepts filename from user and word from user to be searched, it checks weather 
# word is present or not

import os
filename=input("Enter file name")
word=input("Enter word to be searched")
ret=os.path.exists(filename)

def main():
    if ret==True:
        print("File is present")

    fobj=open(filename,"r")

    for line in fobj:
        if word in line:
            print("Word is present")
            break                      #it will exit the loop immediately and will not check on the next line
    else:
            print("Word is not present")

    fobj.close()

if __name__=="__main__":
    main()

    
