
from flask import Flask, request, render_template
import fuelQuoteFormValidations

app = Flask(__name__)

# --------------Nicole--------------

@app.route('/home/')
def home():
    return render_template('index.html')            #Run script (python -m flask run) and go to localhost:5000/home

@app.route('/home/createacc/')
def createacc():
    return render_template('createacc.html')        #Run script (python -m flask run) and go to localhost:5000/home/createacc

# -------------Manuel------------

@app.route('/home/profile/')
def profile():
    return render_template('profile.html')          #Run script (python -m flask run) and go to localhost:5000/home/profile

@app.route('/home/createprofile/')
def createProfile():
    return render_template('createprofile.html')    #Run script (python -m flask run) and go to localhost:5000/home/createprofile

    
# --------------Molina---------------

@app.route('/home/getquote/')
def getQuote():
    return render_template('FuelQuoteForm.html')    #Run script (python -m flask run) and go to localhost:5000//home/getquote

@app.route('/home/submitQuoteRequest', methods = ['POST'])     #send quote request to server
def quote():
    if request.method == 'POST':
        date = request.form['date']
        gallons = request.form['gallons']
        fuel = request.form['fuel']
      
        if fuelQuoteFormValidations.validate(date, gallons, fuel):
            return render_template('FuelQuoteForm.html', date=date, gallons=gallons, fuel=fuel)
            
            # add code here to send complete form data to DB per login data
            # add code here to populate quote history table (profile data and quote data from DB)
        
        else:
            print("Incorrect data format, should be YYYY-MM-DD")

    else:
        return render_template('FuelQuoteForm.html')



                 

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)