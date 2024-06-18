import os
import logging

from flask import Flask, render_template, request, jsonify
# Change the format of messages logged to Stackdriver
logging.basicConfig(format='%(message)s', level=logging.INFO)

app = Flask(__name__)

# -----------FLASK PAGES
@app.route("/",methods=['GET','POST'])
def index():

    return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))