#Wap that creates a new log file every minute
#Filename should contain current timestamp
#write following info into file:
#filename
#creation date
#creation time

import time
import datetime
import schedule
import sys
import os

def directoryscanner(directorypath):
    for Foldername,Subfolder,Filename in os.walk(directorypath):
        for fname in Filename:
            print(fname+"\n")

    timestamp=time.ctime()
    timestamp=timestamp.replace(":","_")

    logfilename="RajLog%s.log"%(timestamp)

    print("Logfile created")

    fobj=open(logfilename,"a")
    fobj.write("The creation date and time is "+timestamp+"\n")
    fobj.close()

def main():
    path=sys.argv[1]

    schedule.every(1).minute.do(directoryscanner,path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()


