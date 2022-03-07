import datetime

# validate Delivery Date, Gallons Requested, Fuel Type form fields 
def validate(date_text, numGallons, fuelType):
    
    # verify all inputs are strings
    if not isinstance(date_text, str):
        return False

    if not isinstance(numGallons, str):
        return False

    if not isinstance(fuelType, str):
        return False 
    
    # date validations
    try:
        quoteDate = datetime.datetime.strptime(date_text, '%Y-%m-%d').date()
    except ValueError:
        return False 

    today = datetime.date.today()
    if quoteDate < today:
        return False

    # gallons validations
    if numGallons.isnumeric() != True:
        return False

    if int(numGallons) <= 0:
        return False


    # fuelType validations
    if fuelType not in ['regUnl', 'premUnl', 'diesel']:
        return False

    return True
    

