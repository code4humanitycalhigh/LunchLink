import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
from charts_class import generate_bar, generate_pie

#counting
df = pd.read_csv("data/form.csv")
q1_1 = df['Q1[1]'].tolist()
q1_2 = df['Q1[2]'].tolist()
q1_3 = df['Q1[3]'].tolist()

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