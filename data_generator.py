import pandas as pd
import time, datetime
import random
from datetime import datetime, timedelta
import random



df = pd.read_csv("data/test_data.csv")
time = datetime.now()

def get_random(o):
  #totally random (weighted)
  lst=[1,2,3,4,5,""]
  if o in [1,2,3,6]:
    return random.choices(lst, weights=(10, 20, 40, 180, 200,100), k=1)[0]
  if o in [5,8,15,20,11,12]:
    return random.choices(lst, weights=(200,100,60,80,10,200), k=1)[0]
  else:
    return round(random.randint(1,5))

  

for i in range(100): # generates 100 rows
  date_time = time.strftime("%#m/%#d/%Y %H:%M:%S")
  
  lst=[date_time]

  for i in range(1,11):
    lst.append(get_random(i))
  lst.append("dietary_restriction")
  lst.append("feedback_example")
  
  df.loc[len(df)] = lst
  time += timedelta(minutes = 1)
  


df.to_csv("data/test_data.csv",index=None)


