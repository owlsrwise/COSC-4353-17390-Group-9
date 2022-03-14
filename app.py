
from flask import Flask, request, render_template
import fuelQuoteFormValidations
import createProfile

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
    return render_template('FuelQuoteForm.html') 

@app.route('/home/quoteresult/', methods = ['POST', 'GET'])     #send quote request to server
def quoteResult():
    quoteData='$530.00'             #hardcode quote data in lieu of database
    form = request.form
    
    if request.method == 'POST':
        date = request.form['date']
        gallons = request.form['gallons']
        fuel = request.form['fuel']

        if fuelQuoteFormValidations.validate(date, gallons, fuel):
            return render_template('FuelQuoteForm.html', form=form, quoteData=quoteData)
    
            # add code here to send complete form data to DB 
            # add code here to populate quote history table (profile data and quote data from DB)
        
        else:
            print("Incorrect data format, should be YYYY-MM-DD")

    else:
        return render_template('FuelQuoteForm.html')        #return blank form
        


                 

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)