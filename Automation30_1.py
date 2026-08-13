#Wap that print jay ganesh every 2 sec

import schedule
import time
import datetime

def display():
    print("Jay Ganesh")

def main():
    print("Automation started")

    schedule.every(2).seconds.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()