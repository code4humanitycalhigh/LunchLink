from flask import Flask, render_template, request, jsonify
from gsheets_api import get_sheets_data
import pandas as pd
import plotly.express as px
#from charts import df_charts
from charts_class import side_by_side_bar, option_data, compare_two, get_menu, get_survey_data
#from charts import pie1, pie2, bar1, bar2

app = Flask(__name__)




@app.route('/', methods=['GET'])
def homepage():
     #updates form.csv
    df=get_sheets_data()
    week_comp, total_comp, total_rat, api_calls = get_survey_data()

    return render_template('home.html', wc=week_comp, tc=total_comp, tr=total_rat, ac=api_calls)

@app.route('/log', methods=['GET'])
def log():
    return render_template('log.html')

@app.route('/calendar', methods=['GET'])
def calendar():
    return render_template('calendar2.html')

@app.route('/analytics', methods=['GET'])
def analytics():
    return render_template('analytics.html')#, pie1=pie1, pie2=pie2, bar1 = bar1, bar2=bar2)

@app.route('/calendar_retrieval', methods=['POST']) 
def calendar_retrieval(): 
    data = request.get_json() 
    
    
    day=data['day']
    month=data['month']
    year=data['year']

    [option1,option2]=get_menu(day,month,year) #charts_class.py
    avg_list, ratings_list=option_data(option1,option2) #charts_class.py
    avg_list=[i for i in avg_list]
    bar = side_by_side_bar(option1, option2)
    percentage_list=[str(round(i*100))+"%" for i in compare_two(avg_list)]
    [name1,name2]=get_menu(day,month,year, True)
    #print(bar)
    
    return jsonify(option_list=[name1,name2], avg_list=avg_list, 
                   total_ratings=ratings_list, percentages=percentage_list,
                   ) # return the result to JavaScript

@app.route('/bar_retrieval', methods=['GET','POST'])
def bar_retrieval():
    
    data = request.get_json() 
    
    
    day=data['day']
    month=data['month']
    year=data['year']

    [option1,option2]=get_menu(day,month,year) #charts_class.py
    bar = side_by_side_bar(option1, option2)
    
    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop')
    #bar.show()
    return bar.to_json()
    




if __name__ == '__main__':
    
    app.run(host="localhost", port=8080, debug=True)
