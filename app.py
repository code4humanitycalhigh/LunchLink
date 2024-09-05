from flask import Flask, render_template, request, jsonify
from gsheets_api import get_sheets_data
import pandas as pd
import charts
#from charts import pie1, pie2, bar1, bar2

app = Flask(__name__)




@app.route('/', methods=['GET'])
def homepage():
     #updates form.csv
    df=get_sheets_data()
    return render_template('home.html',column_names=df.columns.values, row_data=list(df.values.tolist()),zip=zip)

@app.route('/log', methods=['GET'])
def log():
    return render_template('log.html')

@app.route('/calendar', methods=['GET'])
def calendar():
    return render_template('calendar.html')

@app.route('/analytics', methods=['GET'])
def analytics():
    return render_template('analytics.html')#, pie1=pie1, pie2=pie2, bar1 = bar1, bar2=bar2)

@app.route('/calendar_retrieval', methods=['POST']) 
def calendar_retrieval(): 
    data = request.get_json() # retrieve the data sent from JavaScript 
    # process the data using Python code 
    day=data['day']
    month=data['month']
    year=['year']
    
    #print(str(data['day'])+" "+ str(data['month'])+" "+str(data['year']))
    return jsonify(result=str(data['day'])+" "+ str(data['month'])+" "+str(data['year'])) # return the result to JavaScript

if __name__ == '__main__':
    
    app.run(host="localhost", port=8080, debug=True)
