from asyncio.windows_events import NULL
from flask import Flask, request, render_template , flash, redirect
import sqlite3
import fuelQuoteFormValidations
import validateProfile
from datetime import datetime
import init_db
import pricingModule
import re

custId = None               #customer id to be unique for each user
app = Flask(__name__)

app.config['SECRET_KEY'] = 'FSJJSKFJ'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    init_db.init_db(conn)                       #module calling function init_db.py
    print ("Opened database successfully")
    conn.row_factory = sqlite3.Row
    return conn


# --------------Nicole--------------
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'




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
                flash("Please enter a valid username and password")
                return render_template("index.html")
                

            else:       
                userRow = dict(data)
                global custId
                custId = userRow['id']          #takes autoincrement row id into custId
                profile = getProfileData(custId)
                return render_template('profile.html', profile=profile)   

    elif request.method == 'GET':
        return render_template('index.html')
    

@app.route('/home/',methods = ['GET','POST'])
def home():
    global custId
    custId = ''   # clears custId from form
    if request.method =='POST':
        if(request.form.get('email')!= NULL and request.form.get('password')!= NULL) :
            email = request.form.get('email')
            password = request.form.get('password')
            
            def checkemail(email):
               if( re.fullmatch(regex,email)):
                    return True
               else:
                    return False


            if (checkemail(email)== False):
               flash('the email address is invalid please enter a valid email address', category ='error1')      
            
            if len(email) < 1: 
                flash('please enter an email address', category = 'error1')
            if len(email) < 4:
               flash('email is too short please enter email address', category = 'error1')
            if len(email) == 0:
                flash('email cannot be left blank', category = 'error1')
            if len(password) < 4:
                flash('password is too short please enter password', category = 'error1')
            if len(password) == 0:
                flash('password left blank please enter password', category = 'error1')
            conn= get_db_connection()
            c=conn.cursor()
            
            statement = f"SELECT * from userinfo WHERE email ='{email}' AND password = '{password}';"
            c.execute(statement)
            data = c.fetchone()
            if not data: 
                return render_template("index.html")
                

            else:        
                userRow = dict(data)
                custId = userRow['id']
                statement = f"SELECT * from createprofile WHERE custId = '{custId}';"
                c.execute(statement)
                data = c.fetchone()
                profile = dict(data)
                return render_template('profile.html', profile=profile)   

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
        def checkemail(email):
               if( re.fullmatch(regex,email)):
                    return True
               else:
                    return False


        if (checkemail(email)== False):
            flash('the email address is invalid please enter a valid email address', category ='error')    
        if len(fullname) < 2: 
            flash('Name is not valid please enter a valid name', category ='error')
        if len(email) < 2:
            flash ('email is not valid please enter a valid email', category = 'error')
        if len(password1) < 3:
            flash('please enter a valid password. Password is too short', category = 'error')
        

        if password1 == password2 and len(password1) != 0 and checkemail(email) == True :
         conn= get_db_connection()
         c=conn.cursor()
         statement = f"SELECT * from userinfo WHERE email ='{email}' AND password = '{password1}';"
         c.execute(statement)
         data = c.fetchone()
         if data: 
                return render_template("createacc.html")

         else:
            if not data:
                    conn.execute('INSERT INTO userinfo2 (fullname,email,password1,password2) VALUES(?,?,?,?)',(fullname,email,password1,password2))
                    conn.execute('INSERT INTO userinfo (email,password) VALUES(?,?)',(email,password1))
                    conn.commit()
                    statement = f"SELECT * from userinfo WHERE email ='{email}' AND password = '{password1}';"
                    c.execute(statement)
                    row = c.fetchall()        
                    userRow = dict(row[0])
                    global custId
                    custId = userRow['id']
                    conn.close() 
            profile=getProfileData(custId)
            return render_template('createprofile.html', profile=profile)   
        else:
            return render_template('createacc.html')
    elif request.method == 'GET':
        return render_template('createacc.html')
               #Run script (python -m flask run) and go to localhost:5000/home
        
            
    return render_template('createacc.html')        #Run script (python -m flask run) and go to localhost:5000/home/createacc

# -------------Manuel------------

@app.route('/home/profile/', methods=['GET', 'POST'])
def profile():
    global custId
    statement = f"SELECT * from createprofile WHERE custId = '{custId}';"
    conn= get_db_connection()
    c=conn.cursor()
    c.execute(statement)
    data = c.fetchone()
    conn.close()
    profile = dict(data)
    return render_template('profile.html', profile=profile)
    


@app.route('/home/createprofile/', methods=['GET', 'POST'])
def createProfile(): 
    global custId
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
            cur=conn.cursor()
            #is this an update(existing) or insert(new) profile?
            query = f'SELECT * from createprofile WHERE custID={custId}'
            cur.execute(query)
            row = cur.fetchone()        #list with 1 dict (1 row for custID)
            if row is None: 
                cur.execute('INSERT INTO createprofile (custId, name, address1, address2, city, state, zipcode) VALUES (?, ?, ?, ?, ?, ?, ?)',
                            (custId, name, address1, address2, city, state, zipcode))
            else:
                query = f'UPDATE createprofile SET name="{name}", address1="{address1}", address2="{address2}", city="{city}", state="{state}", zipcode="{zipcode}" WHERE custID="{custId}"'
                cur.execute(query) 
                             
            conn.commit()
            conn.close()
            print(errors, "Error", errorOccurred)
    if errors >= 1:
        return render_template('createprofile.html', error=errorOccurred)
            
    else: 
        errorOccurred = "Finished Profile"
        statement = f"SELECT * from createprofile WHERE custId = '{custId}';"
        conn= get_db_connection()
        c=conn.cursor()
        c.execute(statement)
        data = c.fetchone()
        conn.close()
        profile = dict(data)
        return render_template('profile.html', profile=profile) 
    
# --------------Molina---------------

#this route provides user with current profile in order to update/save it
@app.route('/home/editprofile/', methods=['GET'])
def editProfile(): 
    global custId
    profile = getProfileData(custId)    #this will return blank creatprofile, or an existing user editprofile
    return render_template('createprofile.html', profile=profile)

#this function returns customer profile as a dict, either as new 'createprofile' or existing user 'editprofile'
def getProfileData (custId):
    conn = get_db_connection()
    cur = conn.cursor()
    query = f'SELECT * from createprofile WHERE custID={custId}'
    cur.execute(query)
    row = cur.fetchone()        #list with 1 dict (1 row for custID)
    if row is None:
        profile = {}        #create empty dict to display createprofile form
        profile['state'] = ''
        profile['name'] = ''
        profile['address1'] = ''
        profile['address2'] = ''
        profile['city'] = ''
        profile['zipcode'] = ''
    else:
        profile = dict(row)
    return profile

#this function returns a list of dicts where each dict is a row in the query result (history)
def getQuoteHistory (custId):
    conn = get_db_connection()
    cur = conn.cursor()
    query = f'SELECT address1, address2, city, state, zipcode, date, gallons, fuel, quote FROM FuelQuoteData \
        WHERE FuelQuoteData.custId={custId} \
        ORDER BY date DESC'
    cur.execute(query)
    queryResult = cur.fetchall()        
    quoteHistory = []
    for row in queryResult:
        quoteHistory.append(dict(row))     #cast each row in query list as a dict; append to history
    return quoteHistory

@app.route('/home/getquote/', methods = ['POST', 'GET'])       
def getQuote():
    # populate profile data into top of quote form
    global custId
    quote = {}
    profile = getProfileData(custId)
    quoteHistory = getQuoteHistory(custId)            
    return render_template('FuelQuoteForm.html', profile=profile, quoteHistory=quoteHistory, quote=quote, fuel='', buttonName="Get Quote", buttonRedirect="http://localhost:5000/home/quoteresult/")  

@app.route('/home/quoteresult/', methods = ['POST'])     #send quote request to pricing module
def quoteResult():               
    quote = {}              #quote = delivery date + gallons + fuel 
    quote['date'] = request.form['date']
    quote['gallons'] = request.form['gallons']
    quote['fuel'] = request.form['fuel']
    global custId
    profile = getProfileData(custId)

    if fuelQuoteFormValidations.validate(quote):
        # form data -> pricing module -> compare state to FuelPrices db table -> populate FuelQuoteData db table
        quoteHistory = getQuoteHistory(custId)    # populate Quote History user view
        if quoteHistory:
            prevUser = 1
        else:
            prevUser = 0
        
        state = profile['state']
        
        # pricing module here
        newPrice = pricingModule.pricing()          #instantiate pricing module class
        gallons = int(quote['gallons'])
        fuelType = quote['fuel']
        suggestedPrice = newPrice.getTotal(state, prevUser, gallons, fuelType)

        quote['totalCharge']= f'${suggestedPrice * gallons:.2f}'
        quote['suggestedPrice'] = f'${suggestedPrice:.2f}'

        return render_template('FuelQuoteForm.html', profile=profile, quoteHistory=quoteHistory, quote=quote, fuel=quote['fuel'], buttonName="New Quote", buttonRedirect="http://localhost:5000/home/getquote/")    
    
    else:
        print("Incorrect data format, should be YYYY-MM-DD")
        return render_template('FuelQuoteForm.html')
        
@app.route('/home/savequote/', methods = ['POST'])     #save quote to database and history table
def saveQuote():               
    quote = {}              #quote = delivery date + gallons + fuel + totalCharge
    quote['date'] = request.form['date']
    quote['gallons'] = request.form['gallons']
    quote['fuel'] = request.form['fuel']
    quote['totalCharge']= request.form['charge']        
    
    global custId
    profile = getProfileData(custId)

    if fuelQuoteFormValidations.validate(quote):
        
        # populate FuelQuoteData db table
        conn = get_db_connection()
        query = f"INSERT INTO FuelQuoteData \
            (custId, date, address1, address2, city, state, zipcode, gallons, fuel, quote) \
            VALUES ('{custId}', '{quote['date']}', '{profile['address1']}', '{profile['address2']}', '{profile['city']}', '{profile['state']}', \
                '{profile['zipcode']}', '{quote['gallons']}', '{quote['fuel']}', '{quote['totalCharge']}')"
                         
        conn.execute(query)
        conn.commit()
        conn.close()
        
        # send user back to get quote page, after save quote completed        
        return redirect("http://localhost:5000/home/getquote/")

    else:
        print("Incorrect data format, should be YYYY-MM-DD")
        return render_template('FuelQuoteForm.html')
    

                 

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)

