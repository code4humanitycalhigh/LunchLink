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
                                      
                                       "Dietary Restrictions",
                                       "Feedback"]) # O for Option
  #sorting
  #df = df.sort_values(by='Timestamp')

  

  return df
  

#print(get_sheets_data())
