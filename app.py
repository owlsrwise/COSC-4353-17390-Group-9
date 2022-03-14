
from flask import Flask, request, render_template , flash
import fuelQuoteFormValidations

app = Flask(__name__)

app.config['SECRET_KEY'] = 'FSJJSKFJ'

   

# --------------Nicole--------------
@app.route('/', methods = ['GET', 'POST'])
def home1():
     data = request.form
     print(data)
     return render_template('index.html')
@app.route('/home/',methods = ['GET','POST'])
def home():
    
    return render_template('index.html')            #Run script (python -m flask run) and go to localhost:5000/home

@app.route('/home/createacc/', methods=['GET', 'POST'])
def createacc():
    if request.method =='POST':
        fullname= request.form.get('fullname')
        print(fullname)
        email = request.form.get('email')
        print(email)
        password1= request.form.get('password1')
        print(password1)
        password2=request.form.get('password2')
        print(password2)

        if len(fullname)<=2:
            flash('Username must be at least 4 characters',category='error')
        elif len(email)<=2:
            flash('email must be greater than 2 character',category='error')
        elif len(password1) < 4:
            flash('Password must be at least 4 characters',category = 'error')
        elif password1 != password2:
            flash('Passwords do not match ',category='error')
        
        else:
            flash('Account Created! go to profile ',category='success')
            
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