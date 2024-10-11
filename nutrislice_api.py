import urllib.request, json 
import datetime
import calendar
from data_retrieval import get_menu
import pandas as pd
global lst 
lst=[]

def add_data(date, primary, secondary):
  menu = pd.read_csv("data/menu.csv")
  y,m,d = date.split("-")
  date = str(int(m)) + "/" + str(int(d)) + "/" + str(int(y))
  if date in menu["date"].values.tolist():
    #print(date," exists.")
    
    # get rid of original date for organization purposes
    i = menu[(menu["date"] == date)].index

    
    menu = menu.drop(i)
  
  for i in [" - Secondary", " (Secondary)", " - Scratch"]:
    if i in primary:
      
      primary = primary[:primary.index(i)]
    if i in secondary:
      secondary = secondary[:secondary.index(i)]
  lst.append(primary)
  lst.append(secondary)
  # reformat date
  

  menu.loc[-1] = [date, primary, secondary]
  menu = menu.sort_values(by="date",key=lambda x: np.argsort(index_natsorted(df["date"])))
  menu.to_csv("data/menu.csv", index = None)


def monthly_menu_update(year,month):
  num_days = calendar.monthrange(2024, 10)[1]
  days = [datetime.date(year, month, day).strftime('%Y-%m-%d') for day in range(1, num_days+1)]

  for day in days:
    day_url = day.replace("-","/")
    with urllib.request.urlopen(f"https://srvusd.api.nutrislice.com/menu/api/weeks/school/california-high-school/menu-type/lunch/{day_url}?format=json") as url:
      data = json.load(url)
      for i in data["days"]:
        if i["date"] == day:
          try:
            primary = i["menu_items"][0]["food"]["name"]
            secondary = i["menu_items"][1]["food"]["name"]
            add_data(i["date"], primary, secondary)
          except Exception as e:
            #print(e)
            print("no menu published for: ", i["date"])
#monthly_menu_update(2024,10)
'''
lst=list(set(lst)) #remove duplicates
print(lst)
print(len(lst))
'''
