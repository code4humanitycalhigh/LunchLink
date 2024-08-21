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
        marker_line_width = 0,
        
    )
    
    #fig.show()
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div
    