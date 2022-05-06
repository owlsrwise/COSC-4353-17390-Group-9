from fuelQuoteFormValidations import *

# test erroneous values for just Delivery Date (other fields valid)
def test_date_notAstring():
    quote={}
    quote['date']=48
    quote['gallons']='1'
    quote['fuel']='regUnl'
    assert not validate(quote)

def test_previousDate():
    quote={}
    quote['date']='2019-03-06'
    quote['gallons']='1'
    quote['fuel']='regUnl'
    assert not validate(quote)

def test_DateFormat():
    quote={}
    quote['gallons']='1'
    quote['fuel']='regUnl'
    assert not validate(quote)
    quote['date']='06-10-2022'
    assert not validate(quote)
    quote['date']='06/06/2022'
    assert not validate(quote)
    quote['date']='06.06.2022'
    assert not validate(quote)

# test erroneous values for just Gallons Requested (other fields valid)
def test_gallons_notAstring():
    quote={}
    quote['date']='2022-06-10'
    quote['gallons']=86
    quote['fuel']='regUnl'    
    assert not validate(quote)

def test_ifGallonsNumeric():
    quote={}
    quote['date']='2022-06-10'
    quote['fuel']='regUnl'
    assert not validate(quote)
    quote['gallons']='a'
    assert not validate(quote)
    quote['gallons']=' '
    assert not validate(quote)
    quote['gallons']=''
    assert not validate(quote)
    quote['gallons']='-'
    assert not validate(quote)
    

def test_ifGallonsEqualsZero():
    quote={}
    quote['date']='2022-06-10'
    quote['gallons']='0'
    quote['fuel']='regUnl'
    assert not validate(quote)

def test_ifGallonsNotFloat():
    quote={}
    quote['date']='2022-06-10'
    quote['gallons']='0.4'
    quote['fuel']='regUnl'
    assert not validate(quote)

def test_ifGallonsLessthanZero():
    quote={}
    quote['date']='2022-06-10'
    quote['fuel']='regUnl'
    assert not validate(quote)
    quote['gallons']='-1'
    assert not validate(quote)
    quote['gallons']='-1.3'
    assert not validate(quote)

# test erroneous values for just Fuel Type (other fields valid)
def test_fuel_notAstring():
    quote={}
    quote['date']='2022-06-10'
    quote['gallons']='1'
    quote['fuel']=57
    assert not validate(quote)

def test_ifFuelTypeNotInList():
    quote={}
    quote['date']='2022-06-10'
    quote['gallons']='1'
    assert not validate(quote)
    quote['fuel']='Reg'
    assert not validate(quote)
    quote['fuel']='Prem'
    assert not validate(quote)
    quote['fuel']='Diesel'
    assert not validate(quote)
    quote['fuel']=' '
    assert not validate(quote)
    quote['fuel']=''
    assert not validate(quote)
    quote['fuel']='-'
    assert not validate(quote)
    quote['fuel']='none'
    assert not validate(quote)
    quote['fuel']='5'
    assert not validate(quote)

def test_all_fields_good():
    quote={}
    quote['date']='2022-06-10'
    quote['gallons']='1'
    quote['fuel']='regUnl'
    assert validate(quote)
