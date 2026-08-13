#Wap that accepts message and time interval from user
#schedule program after evry time accpets from user

import time
import schedule
import datetime

def message():
    msg=input("Enter your message")
    return msg
def interval():
    inter=int(input("Enter your interval time"))
    return inter

def display(msg):
    print(msg)

def main():
    
    print("Automation started")

    msg=message()
    inter=interval()

    schedule.every(inter).minutes.do(display,msg)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()


