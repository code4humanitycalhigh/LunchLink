from flask import Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


if __name__ == '__main__':

 app.run(debug=False,port=8080,host="0.0.0.0")
 
import views