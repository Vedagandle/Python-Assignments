#Wap that reads and displays the content of specified text file every minute
#Handle following condition:
#file does not exist
#file is empty
#permission is denied
#file cannot be opened

import sys
import os
import schedule
import time
import hashlib

def condition(directoryname):
    ret=os.path.exists(directoryname)

    if ret==False:
        print("File does not exist")
    else:
        print("File exists")
    
    fobj=open(directoryname,"r")
    for contents in fobj:
        print("The contents of file are ",contents+"\n")
    

def empty(directoryname):
    fobj=open(directoryname,"rb")

    hobj=hashlib.md5()

    buffer=fobj.read(1024)

    if(len(buffer)==0):
        print("The file is empty",buffer)

    fobj.close()

    return hobj.hexdigest()

def permissiondenied(directoryname):
    try:
        fobj=open(directoryname,"r")
        print("Permission granted")
        fobj.close()

    except PermissionError:
        print("Permission not granted")

def fileopened(directoryname):
    try:
        fobj=open(directoryname,"r")
        print("File opened")
        fobj.close()

    except:
        print("File cannot be opened")

def main():
    name=sys.argv[1]

    schedule.every(1).minute.do(condition,name)
    schedule.every(1).minute.do(empty,name)
    schedule.every(1).minute.do(permissiondenied,name)
    schedule.every(1).minute.do(fileopened,name)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__=="__main__":
    main()
  







