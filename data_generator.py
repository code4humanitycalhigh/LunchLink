import pandas as pd
import time, datetime
import random
from datetime import datetime, timedelta




df = pd.read_csv("form.csv")
time = datetime.now()

def get_random():
  #totally random
  option_list=["1st","2nd","3rd"]
  if range(1,11)[random.randint(0,9)] % 2==0:
    return "3rd"
  if range(1,11)[random.randint(0,9)] % 3==0:
    return "1st"
  if range(1,11)[random.randint(0,9)] % 6==0:
    return "2nd"

for i in range(100): # generates 100 rows
  date_time = time.strftime("%#m/%#d/%Y %H:%M:%S")
  
  lst=[date_time]

  for i in range(15):
    lst.append(get_random())

  lst.append("feedback_example")
  
  df.loc[len(df)] = lst
  time += timedelta(minutes = 1)


df.to_csv("form.csv",index=None)

