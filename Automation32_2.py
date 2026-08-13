#Wap that monitors size of file every 30 sec
#write foloolwinf details into file filesizelog.txt:
#file path
#file size in bytes
#date and time

import os
import time
import datetime
import schedule
import sys

def directoryscanner(directorypath):
    ret=os.path.exists(directorypath)
    if ret==False:
        print("No such directory is present with the specified name")

    for Foldername,Subfolder,Filename in os.walk(directorypath):
        for fname in Filename:
            fname = os.path.join(Foldername,fname)

        fobj=open("Filesizelog.txt","a")
        fobj.write("The directory path is"+directorypath)
        fobj.write(f"File name {fname} : {os.path.getsize(fname)} bytes")
        fobj.write("The current date and time is"+str(datetime.datetime.now())+"\n")

    fobj.close()
        

    print("Log file created")

    
def main():
    path=sys.argv[1]

    schedule.every(30).seconds.do(directoryscanner,path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()