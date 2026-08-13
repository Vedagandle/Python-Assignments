#Create a function named displayMessage(message)
#schedule the function using 
#schedule.every(5).seconds.do(displayMessage,message)
#the message should be accepted from the user

import time
import schedule

def displayMessage(message):
   
    print(message)

def main():
    print("Automation started")

    msg= input("Enter your message")

    schedule.every(5).seconds.do(displayMessage,msg)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()