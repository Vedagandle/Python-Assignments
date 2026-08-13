#Wap that print current date and time after every 1 minute

import time
import datetime
import schedule

def display():
    print(datetime.datetime.now())

def main():
    print("Automation started")

    schedule.every(1).minute.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()