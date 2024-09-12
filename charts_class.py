import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from datetime import date
from datetime import timedelta
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
from data_retrieval import week_data,get_5, pie_df,data_side #testing

def generate_pie(df,title, colors = None):
    fig=(go.Figure(
        data=go.Pie(
            labels=df[df.columns.values.tolist()[0]],
           
            title=title,
            titlefont={'size':100},
            values=df[df.columns.values.tolist()[1]],
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
    div = plotly.offline.plot(fig, include_plotlyjs=None, output_type='div', config={'displayModeBar': False})
    
    return div
def generate_bar(df, x_col, y_col_s, title, y_range,colors=None):
    df['category'] = [str(i) for i in df.index] 
    fig = px.bar(df, x='Name of Option', y='Average Rating out of 5',
            color = 'Name of Option',
            color_discrete_sequence=colors,
            #barmode="overlay",
             title=title)
    
    
    fig.update_layout(
        #showlegend=False,
        yaxis_range=y_range,
        plot_bgcolor='rgba(250,250,250,0)',
        paper_bgcolor='rgba(250,250,250,0)',
        font_color="black",
        title_font_color="black",
        legend_title_font_color="black",
    )
    fig.update_xaxes(
        ticks='inside',
        showticklabels=False,
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

    fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0.8,
            xanchor="right",
            x=1
    ))

    fig.update_layout(
        legend_title=None,
        title={
            'text': title,
            'y':1,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    
    #fig.show()
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div
    

def side_by_side_bar(O1,O2): #O1 and O2 do NOT represent the columns O1 and O2
    df_labels=pd.read_csv("data/labels.csv")
    
    [name1,name2]=[df_labels.loc[df_labels['FormOption'] == i, 'LunchItem'].values.tolist()[0] for i in [O1,O2]]
    df_raw=pd.read_csv("data/test_data.csv")
    
    df_colors=data_side()
    #print(df_colors["Name of Option"])
    
    avg1=df_colors.loc[df_colors['Name of Option'] == O1, "Average Rating out of 5"].values.tolist()[0]
    avg2=df_colors.loc[df_colors['Name of Option'] == O2, "Average Rating out of 5"].values.tolist()[0]

    [O1,O2] = [O1,O2] if avg1>avg2 else [O2,O1]
    #print(O1,O2)
    
    [name1,name2]=[df_labels.loc[df_labels['FormOption'] == i, 'LunchItem'].values.tolist()[0] for i in [O1,O2]]
    #[name1,name2]=[df_labels.loc[df_labels['FormOption'] == i, 'LunchItem'].values.tolist()[0] for i in [O1,O2]]
    #print(name1,name2)
    
    O1_list=df_raw[O1].values.tolist()
    O2_list=df_raw[O2].values.tolist()
    O1_V=[0,0,0,0,0]
    O2_V=[0,0,0,0,0]
    
    
    for i in O1_list:
        #print(i)
        if pd.isnull(i):
            pass
        else:
            O1_V[int(i-1)] += 1
    for i in O2_list:
        #print(i)
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
        #title= name1 + " Ratings vs "+name2+" Ratings"
    )
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
        title="Count",
        ticks='inside',
        showline=True,
        linecolor='white',
        gridcolor='white'
    )
    fig.update_traces(
        marker_line_width = 0
    )
    fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0.8,
            xanchor="right",
            x=1
    ))
    fig.update_layout(
        legend_title=None,
        title={
            
            'y':1,
            'x':0.25,
            'xanchor': 'center',
            'yanchor': 'top'})
    #fig.show()
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return fig

def generate_line(df):
    
    fig=px.line(
        data_frame = df,
        x = df.columns.values.tolist()[0],
        y = df.columns.values.tolist()[1],
        color_discrete_sequence=["#b4e4b4","#ff6c64"],
        orientation = "v",
        title= df.columns.values.tolist()[0] + " Ratings vs "+df.columns.values.tolist()[1]+" Ratings")
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

#bar_top = generate_bar(get_5("bottom"),0,1,'Average Rating for 5 Lowest Rated Food Options',[0,5])


#side_by_side_bar("O3","O10")


