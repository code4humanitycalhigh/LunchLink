import googleapiclient.discovery
from google.oauth2 import service_account
import json
import pandas as pd



def get_credentials():
    

    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    GOOGLE_PRIVATE_KEY = config.get('GOOGLE_PRIVATE_KEY')
    
    account_info = {
      "private_key": GOOGLE_PRIVATE_KEY,
      "client_email": config.get('GOOGLE_CLIENT_EMAIL'),
      "token_uri": "https://accounts.google.com/o/oauth2/token",
    }
    
    credentials = service_account.Credentials.from_service_account_info(account_info, scopes=scopes)
    return credentials


def get_service(service_name='sheets', api_version='v4'):
    credentials = get_credentials()
    service = googleapiclient.discovery.build(service_name, api_version, credentials=credentials)
    return service


with open('config.json') as config_file:
    config = json.load(config_file)

def upload_sheets_data():
  service = get_service()
  spreadsheet_id = config.get('GOOGLE_SPREADSHEET_ID')
  range_name = config.get('GOOGLE_CELL_RANGE')

  result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=range_name).execute()
  values = result.get('values', [])
  columns=values.pop(0)
  df = pd.DataFrame(values, columns = ["Timestamp","Q1","Q2","Q3","Feedback"])
  df.to_csv("form.csv",index=None)
  


