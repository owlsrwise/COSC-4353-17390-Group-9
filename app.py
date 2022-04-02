from flask import Flask, request, render_template, flash
import sqlite3
import fuelQuoteFormValidations
import createProfile

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row          #this allows query results to return as dicts
    return conn

#this function returns customer profile as a dict, to render in html quote form
def getProfileData (custId):
    conn = get_db_connection()
    cur = conn.cursor()
    query = f'SELECT * from DummyProfile WHERE custID={custId}'
    cur.execute(query)
    row = cur.fetchall()        #list with 1 dict (1 row for custID)
    return dict(row[0])

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
    return render_template('profile.html') #Run script (python -m flask run) and go to localhost:5000/home/profile


@app.route('/home/createprofile/')
def createProfile(): 
    errorOccurred = ""
    errors = 0
    name = request.form.get("name")
    if len(name) > 50 or len(name) <= 0:
        errorOccurred +=  print("Full name is needed with a max of 50 characters.")
        errors += 1
    address1 = request.form.get("address1")
    if len(address1) > 100 or len(address1) <= 0:
        errorOccurred += print("An address is needed with a max of 100 characters.")
        errors += 1
    address2 = request.form.get("address2")
    if len(address2) > 100:
        errorOccurred += print("Can only have a max of 100 characters.")
        errors += 1
    city = request.form.get("city")
    if len(city) > 100 or len(city) <= 0:
        errorOccurred += print("A city is needed with a max of 100 characters.")
        errors += 1
    state = request.form.get("state")
    if state == "":
        errorOccurred += print("A state is Needed, choose at least one.")
        errors += 1
    zipcode = request.form.get("zipcode")
    if len(zipcode) > 9 or len(zipcode) < 5:
        errorOccurred += print("A zipcode is needed, must be between 5-9 characters.")
        errors += 1
    print(errors, "Error", errorOccurred)
    if errors >= 1:
        return render_template('profile.html', error=errorOccurred,
            name=name, address1=address1, address2=address2, city=city, zipcode=zipcode)
    else: 
        errorOccurred = "Finished Profile"
        print(request.form)
        return render_template('createprofile.html', error=errorOccurred) #Run script (python -m flask run) and go to localhost:5000/home/createprofile
    
# --------------Molina---------------

@app.route('/home/getquote/')       #Run script (python -m flask run) and go to localhost:5000//home/getquote
def getQuote():
    # populate profile data into top of quote form
    #custId = request.form['custId']    #custId from post form sent by Manuel
    custId='001'
    profile = getProfileData(custId)
    return render_template('FuelQuoteForm.html', profile=profile) 

@app.route('/home/quoteresult/', methods = ['POST', 'GET'])     #send quote request to server
def quoteResult():
    quote='$19.50'             #hardcode quote data in lieu of pricing module
    custId='001'               #hardcode quote data in lieu of profile data
    form = request.form
    
    if request.method == 'POST':
        date = request.form['date']
        gallons = request.form['gallons']
        fuel = request.form['fuel']
        profile = getProfileData(custId)
        
        if fuelQuoteFormValidations.validate(date, gallons, fuel):           
            # form data -> pricing module -> compare state to FuelPrices db table -> populate FuelQuoteData db table
            # pricing module here
            
            # populate FuelQuoteData db table
            conn = get_db_connection()
            conn.execute('INSERT INTO FuelQuoteData (custId, date, gallons, fuel, quote) VALUES (?, ?, ?, ?, ?)',
                         (custId, date, gallons, fuel, quote))
            conn.commit()
            
            # populate Quote History user view
            

            conn.close()
            return render_template('FuelQuoteForm.html', form=form, quote=quote, profile=profile)    
        
        else:
            print("Incorrect data format, should be YYYY-MM-DD")

    else:
        return render_template('FuelQuoteForm.html')        #return blank form
        


                 

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)