#Wap that scans directory every minute
#the task should display:
#directory name
#no of file
#no of subdirectories
#date and time of scanning

import os
import time
import schedule
import datetime
import sys

def dierctoryScanner(directorypath):
    for Foldername,Subfolder,Filename in os.walk(directorypath):
        
        print("The directory name is ",Foldername)

        countfile=0
        for fname in Filename:
            countfile=countfile+1
        print ("The no of files are ",countfile)

        countdirectory=0
        for ffolder in Subfolder:
            countdirectory=countdirectory+1
        print  ("No of subdirectories are",countdirectory)

        print("Date and time of scanning is ",datetime.datetime.now())

def main():
    print("Automation started")

    path=sys.argv[1]

    schedule.every(1).minute.do(dierctoryScanner,path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()





    

    
