import datetime


target_time=datetime.datetime(2023, 8, 7, 18, 49, 15, 999999)

while(True):
    now = datetime.datetime.now()
    print(now)
    print(target_time)
    print(now==target_time)
    if(now>target_time):
        break