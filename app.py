from flask import Flask, render_template
from gsheets_api import upload_sheets_data
import pandas as pd

app = Flask(__name__)



@app.route('/', methods=['GET'])
def homepage():
    upload_sheets_data() #updates form.csv
    df=pd.read_csv("form.csv")
    
    return render_template('index.html',column_names=df.columns.values, row_data=list(df.values.tolist()),zip=zip)


if __name__ == '__main__':
    app.run(debug=True)