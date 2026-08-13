#Wap taht executes after every 5 min
#write current date and time into file
#new entries should be appended without deleting old ones

import datetime
import time
import schedule
import os
import sys

filename=(sys.argv[1])
ret=os.path.exists(filename)


def display():
    fobj=open(filename,"a")

    data=str(datetime.datetime.now())
    print("The data is ",data)
    fobj.write(data)
    fobj.close()

def main():
    if ret==True:
        print("File is created")

    schedule.every(5).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()

