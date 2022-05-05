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
    assert not validate('2022-06-10', 86, 'regUnl')

def test_ifGallonsNumeric():
    assert not validate('2022-06-10', 'a', 'regUnl')
    assert not validate('2022-06-10', ' ', 'regUnl')
    assert not validate('2022-06-10', '', 'regUnl')
    assert not validate('2022-06-10', '-', 'regUnl')
    assert not validate('2022-06-10', None, 'regUnl')

def test_ifGallonsEqualsZero():
    assert not validate('2022-06-10', '0', 'regUnl')

def test_ifGallonsNotFloat():
    assert not validate('2022-06-10', '0.4', 'regUnl')

def test_ifGallonsLessthanZero():
    assert not validate('2022-06-10', '-1', 'regUnl')
    assert not validate('2022-06-10', '-1.3', 'regUnl')

# test erroneous values for just Fuel Type (other fields valid)
def test_fuel_notAstring():
    assert not validate('2022-06-10', '1', 57)

def test_ifFuelTypeNotInList():
    assert not validate('2022-06-10', '1', 'Reg')
    assert not validate('2022-06-10', '1', 'Prem')
    assert not validate('2022-06-10', '1', 'Diesel')
    assert not validate('2022-06-10', '1', ' ')
    assert not validate('2022-06-10', '1', '')
    assert not validate('2022-06-10', '1', '-')
    assert not validate('2022-06-10', '1', 'none')
    assert not validate('2022-06-10', '1', None)
    assert not validate('2022-06-10', '1', '5')

def test_all_fields_good():
    assert validate('2022-06-10', '1', 'regUnl')
