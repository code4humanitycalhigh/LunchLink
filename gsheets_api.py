import googleapiclient.discovery
from google.oauth2 import service_account
import json
import pandas as pd
pd.set_option('display.max_columns', None)
import datetime
from google.cloud import storage
import numpy as np
import google
import time
import os
import logging
from dotenv import load_dotenv
load_dotenv()


def googleauth_filter(record):
    # https://github.com/googleapis/google-auth-library-python/issues/927
    if record.exc_info and isinstance(record.exc_info[1], ValueError) \
        and traceback.extract_tb(record.exc_info[2])[-1].name == 'from_bytes':
        record.levelno = logging.INFO
        record.levelname = logging.getLevelName(logging.INFO)
        record.msg += ': ' + str(record.exc_info[1])
        record.exc_info = None
    return True
logging.getLogger('grpc._plugin_wrapping').addFilter(googleauth_filter)


def get_credentials():
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    GOOGLE_PRIVATE_KEY = os.getenv('GOOGLE_PRIVATE_KEY')
    
    account_info = {
      "private_key": GOOGLE_PRIVATE_KEY,
      "client_email": os.getenv('GOOGLE_CLIENT_EMAIL'),
      "token_uri": "https://accounts.google.com/o/oauth2/token",
    }

    
    
    credentials = service_account.Credentials.from_service_account_info(account_info, scopes=scopes)
    
    
    return credentials


def get_service(service_name='sheets', api_version='v4'):
    credentials = get_credentials()
    service = googleapiclient.discovery.build(service_name, api_version, credentials=credentials)
    return service




def get_sheets_data():
  service = get_service()
  spreadsheet_id = os.getenv('GOOGLE_SPREADSHEET_ID')
  range_name = os.getenv('GOOGLE_CELL_RANGE')

  result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=range_name).execute()
  values = result.get('values', [])
  #print(values)
  columns=values.pop(0)
  df = pd.DataFrame(values, columns = ["Timestamp",
                                       "O1", "O2", "O3", "O4", "O5", 
                                       "O6", "O7", "O8", "O9", "O10", 
                                       "O11", "O12", "O13", "O14", "O15", 
                                       "O16", "O17", "O18", "O19", "O20", 
                                       "O21", "O22", "O23", "O24", "O25",
                                       "Dietary Restrictions",
                                       "Feedback"]) # O for Option
  #sorting
  #df = df.sort_values(by='Timestamp')

  

  return df
  

  '''
  Legend:
  1 : Chicken Sandwhich
  2 : Cheeseburger
  3 : Cheese Pizza
  4 : Cheese Quesadilla
  5 : Chicken Nuggets
  6 : Penne Pasta
  7 : Chicken Quesadilla
  8 : Chile 
  9 : Burrito
  10 : Cheese Calzone
  11 : Spicy Chicken Sandwhich
  12 : Chicken & Waffle
  13 : Bosco Sticks
  14 : Fried Chicken
  '''

def get_menu(day, month, year,names=False):
    df_menu=pd.read_csv("data/menu.csv")
    str_format=str(month)+"/"+str(day)+"/"+str(year)
    
    #returns list len 2
    items=df_menu.loc[df_menu['Date'] == str_format, ['Item1','Item2']].values.tolist()[0]
    if names:
      try:
        return 'No options listed' if len(items) == 0 else items
      except:
        return 'error'
    
    df_labels=pd.read_csv('data/labels.csv')
    #a=items[0]
    #print('a: ',df_labels.loc[df_labels['LunchItem']=='Grilled Chicken Fajita Rice Bowl', 'FormOption'].values.tolist()[0])
    try:
        
        options=[df_labels.loc[df_labels['LunchItem'] == i, 'FormOption'].values.tolist()[0] for i in items]
        return options
    except:
        print("error: ",items)
       
    #return df_menu.loc[df_menu['Date'] == str_format, ['Item1','Item2']].values.tolist()[0]

def compare_two(avg1, avg2):
  percentage1=avg1/(avg1+avg2)
  percentage2=avg2/(avg1+avg2)
  return percentage1,percentage2


#counting
def charts_df():
  df = pd.read_csv("data/test_data.csv")#get_sheets_data()
  column_list=df.columns.values.tolist()
  avg_values=[]
  total_values=[]
  #print(column_list)
  for i in column_list[1:26]:
    value_list=df[i].values.tolist()
    avg=np.nanmean(value_list,axis=0)
    column_name="avg"+i[1:]
    avg_values.append(round(avg,2))
    total_values.append(np.count_nonzero(~np.isnan(value_list)))

  df_charts=pd.DataFrame(data={
    "Name of Option": column_list[1:26],
    "Average Rating out of 5": avg_values,
    "# of Ratings": total_values,
  })
  return df_charts

def option_data(O1, O2):
  df=charts_df()
  
  avg_list=[df.loc[df['Name of Option'] == i, 'Average Rating out of 5'].values.tolist()[0] 
            for i in [O1,O2]]
  total_ratings=[df.loc[df['Name of Option'] == i, '# of Ratings'].values.tolist()[0] 
            for i in [O1,O2]]
  return avg_list, total_ratings



    
  


