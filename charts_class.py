import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
def generate_pie(df,title, colors = None):
    fig=(go.Figure(
        data=go.Pie(
            labels=df['Option'],
            title=title,
            titlefont={'size':100},
            values=df["# of Preference Chosen"],
            hole=0.5,
            #opacity = 0.5,
            
            ) 
        ))
    fig.update_traces(
            hoverinfo='label+value',
            textinfo='label+percent',
            textfont_size=12,
            marker=dict(colors=colors, 
                        line=dict(color='white', width=5))
    )
    fig.update_layout(plot_bgcolor='rgba(250,250,250,0)',paper_bgcolor='rgba(250,250,250,0)',
                    font_color="black",
                    title_font_color="black",
                    legend_title_font_color="black",
                    margin=dict(t=0.2, b=0.2, l=0.2, r=0.2))
    #fig.show()
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    
    return div
def generate_bar(df, x_col, y_col_s, title, colors=None):
    df['category'] = [str(i) for i in df.index] 
    fig = px.bar(df, x=df.columns[x_col], y=df.columns[y_col_s:],
            color = 'category',
            color_discrete_sequence=colors,
            #barmode="overlay",
             title=title)
    fig.update_layout(
        plot_bgcolor='rgba(250,250,250,0)',
        paper_bgcolor='rgba(250,250,250,0)',
        font_color="black",
        title_font_color="black",
        legend_title_font_color="black",
    )
    fig.update_xaxes(
        ticks='inside',
        gridcolor='white'
    )  
    fig.update_yaxes(
        ticks='inside',
        showline=True,
        linecolor='white',
        gridcolor='white'
    )
    fig.update_traces(
        marker_line_width = 0
    )
    
    #fig.show()
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div
    

def side_by_side_bar(O1,O2): #O1 and O2 do NOT represent the columns O1 and O2
    df_labels=pd.read_csv("data/labels.csv")
    
    [name1,name2]=[df_labels.loc[df_labels['FormOption'] == i, 'LunchItem'].values.tolist()[0] for i in [O1,O2]]
    df_raw=pd.read_csv("data/test_data.csv")

    O1_list=df_raw[O1].values.tolist()
    O2_list=df_raw[O2].values.tolist()
    O1_V=[0,0,0,0,0]
    O2_V=[0,0,0,0,0]
    
    
    for i in O1_list:
        if pd.isnull(i):
            pass
        else:
            O1_V[int(i-1)] += 1
    for i in O2_list:
        if pd.isnull(i):
            pass
        else:
            O2_V[int(i-1)] += 1

    df=pd.DataFrame(data={
    "Rating" : [1,2,3,4,5],
    name1 : O1_V,
    name2 : O2_V,
    })
    fig=px.bar(
        data_frame = df,
        x = "Rating",
        y = [name1,name2],
        color_discrete_sequence=["#b4e4b4","#ff6c64"],
        orientation = "v",
        barmode = 'group',
        title= name1 + " Ratings vs "+name2+" Ratings")
    fig.update_layout(
        plot_bgcolor='rgba(250,250,250,0)',
        paper_bgcolor='rgba(250,250,250,0)',
        font_color="black",
        title_font_color="black",
        legend_title_font_color="black",
    )
    fig.update_xaxes(
        ticks='inside',
        gridcolor='white'
    )  
    fig.update_yaxes(
        ticks='inside',
        showline=True,
        linecolor='white',
        gridcolor='white'
    )
    fig.update_traces(
        marker_line_width = 0
    )
    #fig.show()
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div

#side_by_side_bar("O1","O5") #pizza and hot dog

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


#bar = side_by_side_bar(option1, option2)