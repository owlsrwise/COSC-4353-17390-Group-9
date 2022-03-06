from fuelQuoteFormValidations import *


# test erroneous values for Delivery Date, Gallons Requested, Fuel Type

def test_todaysDate():
    assert not validate('2022-03-06', '-1', '0')

def test_previousDate():
    assert not validate('2019-03-06', '-1', '0')

def test_ifgallonsnumeric():
    assert not validate('2022-03-06', '-1', '0')

def test_ifgallonslessthanzero():
    assert not validate('2022-03-06', '-1', '0')

#validate('00-00-0000', 0.1, 0)

#validate('00-00-0000', 0.1, 0)


