
from flask import Flask, request, render_template
import fuelQuoteFormValidations

app = Flask(__name__)

@app.route('/home/')
def home():
    return render_template('index.html')            #Run script (python -m flask run) and go to localhost:5000/home

@app.route('/home/createacc/')
def createacc():
    return render_template('createacc.html')        #Run script (python -m flask run) and go to localhost:5000/createacc

@app.route('/home/getquote/')
def getQuote():
    #return "Hello, Flask!"
    return render_template('FuelQuoteForm.html')    #Run script (python -m flask run) and go to localhost:5000/getquote

@app.route('/home/profile/')
def profile():
    return render_template('profile.html')          #Run script (python -m flask run) and go to localhost:5000/profile

@app.route('/home/createprofile/')
def createProfile():
    return render_template('createprofile.html')    #Run script (python -m flask run) and go to localhost:5000/createprofile

                 

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)