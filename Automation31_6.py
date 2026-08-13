#Wap that schedules following msgs:
#Monday at 9:00 am: Start your weekly goals
#Wednesday at 5:00 pm: Review your weekly progress
#Friday at 6:00 pm : Weekly work completed

import time
import schedule

def mon():
    print("Start your weekly goals")

def wed():
    print("Review your weekly progress")

def fri():
    print("Weekly work completed")

def main():
    schedule.every().monday.at("09:00").do(mon)
    schedule.every().wednesday.at("17:00").do(wed)
    schedule.every().friday.at("18:00").do(fri)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__=="__main__":
    main()