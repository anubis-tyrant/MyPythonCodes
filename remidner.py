import datetime
import calendar
import time

week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
week_num=datetime.date.today().weekday()

while True:
    if week_days[week_num]=="Monday":
        print("you have Chemitry and Physics classes today")
        time.sleep(7200)
    elif week_days[week_num]=="Tuesday":
        print("You have Biology and Mathematics today")
        time.sleep(7200)
    elif week_days[week_num]=="Wednesday":
        print("Its Sports day, Don't forget your shoes")
        time.sleep(7200)
    elif week_days[week_num]=="Thursday":
        print("You have Chemistry and Physics class again")
        time.sleep(7200)
    elif week_days[week_num]=="Friday":
        print("You have Computer Science and Mathermatics today")
        time.sleep(7200)
    elif week_days[week_num]=="Saturday":
        print("Its a holiday but make sure to complete your homeworks given to you yesterday")
        time.sleep(7200)
    elif week_days[week_num]=="Sunday":
        print("Its Sunday, Have a nice day :)")
        time.sleep(7200)
