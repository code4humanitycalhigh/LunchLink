from flask import Flask, render_template
from gsheets_api import get_sheets_data
import pandas as pd
from charts import pie1, pie2, bar1, bar2

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
    return render_template('analytics.html', pie1=pie1, pie2=pie2, bar1 = bar1, bar2=bar2)

if __name__ == '__main__':
    
    app.run(host="localhost", port=8080, debug=True)
