#create a task that executes every day at 9.00am and print namaskar

import datetime
import time
import schedule

def display():
    print("Namaskar")

def main():
    print("Automation started")

    schedule.every().day.at("09:00").do(display)  #09 because 24 hr format

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__=="__main__":
    main()