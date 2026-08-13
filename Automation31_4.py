#Wap that creates a new lof after every 5 min 
#the file should contain:
#log file created successfully 
#creation time

import schedule
import datetime
import time

def directoryscanner():
    

    fobj=open("Marvellous Log.txt","w")

    fobj.write("Log file created succesfully")
    fobj.write("The file was created at "+str(datetime.datetime.now()))  #+ because write can take 1 argument , we wanted to give 2 so we have concateneted

    fobj.close()

def main():
    print("Automation started")
    

    schedule.every(10).seconds.do(directoryscanner)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
