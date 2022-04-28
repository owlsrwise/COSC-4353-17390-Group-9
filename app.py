from asyncio.windows_events import NULL
from flask import Flask, request, render_template , flash
import sqlite3
import fuelQuoteFormValidations
import validateProfile
from datetime import datetime
import init_db


app = Flask(__name__)

app.config['SECRET_KEY'] = 'FSJJSKFJ'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    init_db.init_db(conn)                       #module calling function init_db.py
    print ("Opened database successfully")
    conn.row_factory = sqlite3.Row
    return conn


# --------------Nicole--------------
@app.route('/', methods = ['GET', 'POST'])
def home1():
    if request.method =='POST':
          if(request.form.get('email')!= NULL and request.form.get('password')!= NULL) :
            email = request.form.get('email')
            password = request.form.get('password')
            
            conn= get_db_connection()
            c=conn.cursor()
            
            statement = f"SELECT * from userinfo WHERE email ='{email}' AND password = '{password}';"
            c.execute(statement)
            data = c.fetchone()
            if not data: 
                return render_template("index.html")
                

            else:
                
                return render_template('profile.html')   

    elif request.method == 'GET':
        return render_template('index.html')
    

@app.route('/home/',methods = ['GET','POST'])
def home():
    
     if request.method =='POST':
          if(request.form.get('email')!= NULL and request.form.get('password')!= NULL) :
            email = request.form.get('email')
            password = request.form.get('password')
            
            conn= get_db_connection()
            c=conn.cursor()
            
            statement = f"SELECT * from userinfo WHERE email ='{email}' AND password = '{password}';"
            c.execute(statement)
            data = c.fetchone()
            if not data: 
                return render_template("index.html")
                

            else:
                
                return render_template('profile.html')   

     elif request.method == 'GET':
        return render_template('index.html')

@app.route('/home/createacc/', methods=['GET', 'POST'])
def createacc():

    if request.method =='POST':
      if(request.form.get('email')!= NULL and request.form.get('password')!= NULL) :  
        fullname= request.form.get('fullname')
        print(fullname)
        email = request.form.get('email')
        print(email)
        password1= request.form.get('password1')
        print(password1)
        password2=request.form.get('password2')
        print(password2)
        if password1 == password2 :
         conn= get_db_connection()
         c=conn.cursor()
         statement = f"SELECT * from userinfo WHERE email ='{email}' AND password = '{password1}';"
         c.execute(statement)
         data = c.fetchone()
         if data: 
                return render_template("error.html")

         else:
            if not data:
                    conn.execute('INSERT INTO userinfo2 (fullname,email,password1,password2) VALUES(?,?,?,?)',(fullname,email,password1,password2))
                    conn.execute('INSERT INTO userinfo (email,password) VALUES(?,?)',(email,password1))
                    conn.commit()
                    conn.close() 
            return render_template('createprofile.html')   
        else:
            return render_template('error.html')
    elif request.method == 'GET':
        return render_template('createacc.html')
               #Run script (python -m flask run) and go to localhost:5000/home
        
            
    return render_template('createacc.html')        #Run script (python -m flask run) and go to localhost:5000/home/createacc

# -------------Manuel------------

@app.route('/home/profile/', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html') #Run script (python -m flask run) and go to localhost:5000/home/profile


@app.route('/home/createprofile/', methods=['GET', 'POST'])
def createProfile(): 
    custId='001'
    errorOccurred = ""
    errors = 0
    name = request.form.get("Full Name")
    if len(name) > 50 or len(name) <= 0:
        errorOccurred +=  print("Full name is needed with a max of 50 characters.")
        errors += 1
    address1 = request.form.get("Address 1")
    if len(address1) > 100 or len(address1) <= 0:
        errorOccurred += print("An address is needed with a max of 100 characters.")
        errors += 1
    address2 = request.form.get("Address 2")
    if len(address2) > 100:
        errorOccurred += print("Can only have a max of 100 characters.")
        errors += 1
    city = request.form.get("City")
    if len(city) > 100 or len(city) <= 0:
        errorOccurred += print("A city is needed with a max of 100 characters.")
        errors += 1
    state = request.form.get("State")
    if state == "":
        errorOccurred += print("A state is Needed, choose at least one.")
        errors += 1
    zipcode = request.form.get("Zipcode")
    if len(zipcode) > 9 or len(zipcode) < 5:
        errorOccurred += print("A zipcode is needed, must be between 5-9 characters.")
        errors += 1

    if validateProfile.validate(name, address1, address2, city, state, zipcode):           

            conn = get_db_connection()
            conn.execute('INSERT INTO createprofile (custId, name, address1, address2, city, state, zipcode) VALUES (?, ?, ?, ?, ?, ?, ?)',
                            (custId, name, address1, address2, city, state, zipcode))
            conn.commit()

            conn.close()
            print(errors, "Error", errorOccurred)
    if errors >= 1:
        return render_template('createprofile.html', error=errorOccurred)
            
    else: 
        errorOccurred = "Finished Profile"
        print(request.form)
        return render_template('profile.html', name=name, address1=address1, address2=address2, city=city, state=state, zipcode=zipcode) 
    
# --------------Molina---------------

#this function returns customer profile as a dict, to render in html quote form
def getProfileData (custId):
    conn = get_db_connection()
    cur = conn.cursor()
    query = f'SELECT * from createprofile WHERE custID={custId}'
    cur.execute(query)
    row = cur.fetchall()        #list with 1 dict (1 row for custID)
    return dict(row[0])

#this function returns a list of dicts where each dict is a row in the query result (history)
def getQuoteHistory (custId):
    conn = get_db_connection()
    cur = conn.cursor()
    query = f'select address1, address2, city, state, zipcode, date, gallons, fuel, quote FROM createprofile \
            INNER JOIN FuelQuoteData ON FuelQuoteData.custId = createprofile.custId \
            WHERE FuelQuoteData.custId={custId} \
            ORDER BY date DESC'
    cur.execute(query)
    queryResult = cur.fetchall()        
    quoteHistory = []
    for row in queryResult:
        quoteHistory.append(dict(row))     #cast each row in query list as a dict; append to history
    return quoteHistory

@app.route('/home/getquote/')       #Run script (python -m flask run) and go to localhost:5000//home/getquote
def getQuote():
    # populate profile data into top of quote form
    #custId = request.form['custId']    #custId extracted from profile 'Get Your Quote Today' button
    custId='001'
    profile = getProfileData(custId)
    quoteHistory = getQuoteHistory(custId)            
    return render_template('FuelQuoteForm.html', profile=profile, quoteHistory=quoteHistory)  

@app.route('/home/quoteresult/', methods = ['POST', 'GET'])     #send quote request to server
def quoteResult():
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
            quote='$19.50'             #hardcode quote data in lieu of pricing module
            
            # populate FuelQuoteData db table
            conn = get_db_connection()
            conn.execute('INSERT INTO FuelQuoteData (custId, date, gallons, fuel, quote) VALUES (?, ?, ?, ?, ?)',
                         (custId, date, gallons, fuel, quote))
            conn.commit()
            conn.close()
            
            # populate Quote History user view
            quoteHistory = getQuoteHistory(custId)            
            return render_template('FuelQuoteForm.html', form=form, quote=quote, profile=profile, quoteHistory=quoteHistory)    
        
        else:
            print("Incorrect data format, should be YYYY-MM-DD")
            return render_template('FuelQuoteForm.html')
    else:
        return render_template('FuelQuoteForm.html')        #return blank form
        


                 

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)

