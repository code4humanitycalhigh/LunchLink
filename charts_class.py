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
            
            ) 
        ))
    fig.update_traces(
            hoverinfo='label+value',
            textinfo='label+percent',
            textfont_size=12,
            marker=dict(colors=colors, 
                        line=dict(color='rgba(36,37,45,255)', width=2))
    )
    fig.update_layout(plot_bgcolor='rgba(36,37,45,255)',paper_bgcolor='rgba(36,37,45,255)',
                    font_color="white",
                    title_font_color="white",
                    legend_title_font_color="white",
                    margin=dict(t=0.2, b=0.2, l=0.2, r=0.2))
    fig.show()
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    
    return div
def generate_bar(df, x_col, y_col_s, title, log=False):
    fig = px.bar(df, x=df.columns[x_col], y=df.columns[y_col_s:],
             barmode="overlay",log_y=log, title=title)
    fig.update_layout(
        plot_bgcolor='rgba(36,37,45,255)',
        paper_bgcolor='rgba(36,37,45,255)',
        font_color="white",
        title_font_color="white",
        legend_title_font_color="white",
    )
    fig.update_xaxes(
        ticks='inside',
        gridcolor='#39353d'
    )  
    fig.update_yaxes(
        ticks='inside',
        showline=True,
        linecolor='white',
        gridcolor='#39353d'
    )
    fig.update_traces(
        marker_line_width = 0,
    )
    fig.show()
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div
    