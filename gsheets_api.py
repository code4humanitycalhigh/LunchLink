import googleapiclient.discovery
from google.oauth2 import service_account
import json
import pandas as pd
import datetime
import time
import os
from dotenv import load_dotenv
load_dotenv()



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




def upload_sheets_data():
  service = get_service()
  spreadsheet_id = os.getenv('GOOGLE_SPREADSHEET_ID')
  range_name = os.getenv('GOOGLE_CELL_RANGE')

  result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=range_name).execute()
  values = result.get('values', [])
  #print(values)
  columns=values.pop(0)
  df = pd.DataFrame(values, columns = ["Timestamp",
                                       "Q1[1]","Q1[2]","Q1[3]",
                                       "Q2[4]","Q2[5]","Q2[6]",
                                       "Q3[7]","Q3[8]","Q3[3]",
                                       "Q4[9]","Q4[10]","Q4[11]",
                                       "Q5[12]","Q5[13]","Q5[14]",
                                       "Feedback"])
  #sorting
  df = df.sort_values(by='Timestamp')

  df.to_csv("data/form.csv",index=None)

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
  


