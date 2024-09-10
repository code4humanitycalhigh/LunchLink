import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from datetime import date
from datetime import timedelta
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np


def get_menu(day, month, year,names=False):
    df_menu=pd.read_csv("data/menu.csv")
    str_format=str(month)+"/"+str(day)+"/"+str(year)
    
    #returns list len 2

    print(str_format)
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

def compare_two(avg_list):
  avg1=avg_list[0]
  avg2=avg_list[1]
  percentage1=avg1/(avg1+avg2)
  percentage2=avg2/(avg1+avg2)
  return [percentage1,percentage2]


#counting
def data_side():
  df_data = pd.read_csv("data/test_data.csv")#get_sheets_data()
  column_list=df_data.columns.values.tolist()
  avg_values=[]
  total_values=[]
  #print(column_list)
  for i in column_list[1:26]:
    value_list=df_data[i].values.tolist()
    avg=np.nanmean(value_list,axis=0)
    column_name="avg"+i[1:]
    avg_values.append(round(avg,2))
    total_values.append(np.count_nonzero(~np.isnan(value_list)))

  df=pd.DataFrame(data={
    "Name of Option": column_list[1:26],
    "Average Rating out of 5": avg_values,
    "# of Ratings": total_values,
  })
  return df

def option_data(O1, O2):
  df=data_side()
  
  avg_list=[df.loc[df['Name of Option'] == i, 'Average Rating out of 5'].values.tolist()[0] 
            for i in [O1,O2]]
  total_ratings=[df.loc[df['Name of Option'] == i, '# of Ratings'].values.tolist()[0] 
            for i in [O1,O2]]
  return avg_list, total_ratings


#print(side_by_side_bar('O1','O2'))

def get_survey_data():
    df=pd.read_csv("data/test_data.csv")
    total_completions=[i.split(" ")[0] for i in df.Timestamp.values.tolist()]
    today = date.today() # or you can do today = date.today() for today's date
    this_week=[j.strftime('%#m/%#d/%Y') for j in [today - timedelta(days=i) for i in range(0,7)]]
    completions_this_week=[i for i in total_completions if i in this_week]
   
    total_ratings = df.count().sum()

    # returns all int
    return len(completions_this_week), len(total_completions), total_ratings.item(), 0 # 0 calls to nutrislice

    
def week_data():
    df_data=pd.read_csv("data/test_data.csv")
    total=[i.split(" ")[0] for i in df_data.Timestamp.values.tolist()]
    today = date.today() # or you can do today = date.today() for today's date
    this_week=[j.strftime('%#m/%#d/%Y') for j in [today - timedelta(days=i) for i in range(0,7)]][::-1]
    #print(this_week)
    week_totals=[0,0,0,0,0,0,0]
    for i in total:
        if i in this_week:
            week_totals[this_week.index(i)]+=1
    df=pd.DataFrame({
        'Day':this_week,
        'Surveys Completed':week_totals
    })
    return df

def get_5(par):
    df_labels=pd.read_csv("data/labels.csv")
    df=data_side().sort_values(by=['Average Rating out of 5'])
    if par == "top":
        df=df.tail(5)
    elif par == "bottom":
        df=df.head(5)
    else: 
       print('error')
    
    df=df.drop(columns=['# of Ratings'])
    df=df.reset_index(drop=True)


    options=[df_labels.loc[df_labels['FormOption'] == i, 'LunchItem'].values.tolist()[0] for i in df["Name of Option"].values.tolist()]
    df['Name of Option'] = options
    
    return df
 
def pie_df():
    df_data=pd.read_csv("data/test_data.csv").drop(columns=["Timestamp","Dietary Restrictions",
                                                            "Feedback"])
    ratings=[0,0,0,0,0] #1,2,3,4,5
    for i in df_data.columns.values.tolist():
        #print(i)
        for j in range(5):
            try:
                ratings[j]+=df_data[i].value_counts()[j+1].item()
            except:
               pass
    
    df = pd.DataFrame({
       'Rating':[1,2,3,4,5],
       'Count': ratings
    })


    return df
