import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from gsheets_api import get_sheets_data
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
from charts_class import generate_bar, generate_pie

def compare_two(avg1, avg2):
  percentage1=avg1/(avg1+avg2)
  percentage2=avg2/(avg1+avg2)
  return percentage1,percentage2


#counting
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

df_bar=pd.DataFrame(data={
  "Rating" : [1,2,3,4,5]

})
#print(df_charts)




'''
df1_values = [0,0,0]
df2_values = [0,0,0]

for i in q1_1:
  if i=="1st":
    df1_values[0]+=1
  elif i== "3rd":
    df2_values[0]+=1
for i in q1_2:
  if i=="1st":
    df1_values[1]+=1
  elif i== "3rd":
    df2_values[1]+=1
for i in q1_3:
  if i=="1st":
    df1_values[2]+=1
  elif i== "3rd":
    df2_values[2]+=1




df_Q1_1 = pd.DataFrame({
  "Option" : ["Chicken Sandwhich", "Cheeseburger", "Cheese Pizza"],
  "# of Preference Chosen" : df1_values
})

df_Q1_2 = pd.DataFrame({
  "Option" : ["Chicken Sandwhich", "Cheeseburger", "Cheese Pizza"],
  "# of Preference Chosen" : df2_values
})

colors = ["rgba(205,235,204,255)", "rgba(204, 230, 235, 1)","rgba(235, 209, 204, 1)"]

pie1=generate_pie(df_Q1_1, "First Preference Chosen for Each Option", colors)

pie2=generate_pie(df_Q1_2, "Last Preference Chosen for Each Option", colors)

bar1=generate_bar(df_Q1_1, 0,1, "First Preference Chosen for Each Option", colors)

bar2=generate_bar(df_Q1_2, 0,1, "Last Preference Chosen for Each Option", colors)
'''