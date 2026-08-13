#Wap that accepts directory name from user and counts no of files isnide every five minutes
#Write result into :
#directorycountlog.txt
#each entry should contain directory path,no of files,date and time

import os
import schedule
import time
import datetime
import sys

def directoryscanner(directorypath):
    print("Inside function")
    for Foldername,Subfolder,Filename in os.walk(directorypath):
        count=0
        for fname in Filename:
            count=count+1
        


        fobj=open("DirectoryCountLog.txt","a")
        fobj.write(Foldername)
        fobj.write("No of files are"+str(count))
        fobj.write("Entry done at "+str(datetime.datetime.now()))

        fobj.close()
def main():

    path=sys.argv[1]

    schedule.every(10).seconds.do(directoryscanner,path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()


    


