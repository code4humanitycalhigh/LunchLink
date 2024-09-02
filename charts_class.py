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
    df_menu=pd.read_csv("data/menu.csv")
    name1=df_menu[O1].values[0]
    name2=df_menu[O2].values[0]
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
    fig.show()
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div

#side_by_side_bar("O1","O5") #pizza and hot dog