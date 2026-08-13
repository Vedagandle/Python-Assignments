#Wap that print lunch time every day at 1.00 pm
#print wrap up work every day at 6.00 pm
#both tasks should handled with different functions

import schedule
import time

def lunch():
    print("Lunch time : ")

def work():
    print("Wrap up your work")

def main():
    print("Automation started")

    schedule.every().day.at("13:00").do(lunch)
    schedule.every().day.at("18:00").do(work)

    while True:
        schedule.run_pending()
        time.sleep(10)


if __name__=="__main__":
     main()


        
    

