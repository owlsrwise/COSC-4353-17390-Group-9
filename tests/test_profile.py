import unittest
from app import *
from validateProfile import *

class ProfileTestCase(unittest.TestCase):

    #Validate that imports work
    def test_test(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html')
        self.assertEqual(response.status_code, 150) 
    
    #Validate Profile works
    def test_Profile(self):
        tester = app.test_client(self)
        response = tester.post('/',
            data=dict(name="Manuel Flores", address1="123 Fuel St.", address2="", city="Houston", state="TX", zipcode="77346"))
        self.assertTrue(b'Finished Profile' in response.data)
    #Validate name
    def test_FullNameNeeded(self):
            tester = app.test_client(self)
            response =tester.post('/',
                data=dict(name="", address1="123 Fuel St.", address2="", city="Houston", state="TX", zipcode="77346"),
                follow_redirects=True
            )
            self.assertTrue(b'name is needed' in response.data)
    #Validate adress 1
    def test_Address_1Needed(self):
            tester = app.test_client(self)
            response =tester.post('/',
                data=dict(name="Manuel Flores", address1="", address2="1234 Fuel St.", city="Houston", state="TX", zipcode="77346"),
                follow_redirects=True
        )
            self.assertTrue(b'address is needed' in response.data)
    #Validate adress 2
    def test_Address_2optional(self):
        tester = app.test_client(self)
        response =tester.post('/',
            data=dict(name="Manuel Flores", address1="123 Fuel St.", address2="1234 Fuel St.", city="Houston", state="TX", zipcode="77346"),
            follow_redirects=True
        )
        self.assertTrue(b'Finished Profile' in response.data)
    #Validate zipcode
    def test_zipcodeNeeded(self):
        tester = app.test_client(self)
        response =tester.post('/',
            data=dict(name="Manuel Flores", address1="123 Fuel St.", address2="", city="Houston", state="TX", zipcode="7734"),
            follow_redirects=True
        )
        self.assertTrue(b'zipcode is needed' in response.data)
    #Validate city
    def test_CityNeeded(self):
        tester = app.test_client(self)
        response =tester.post('/',
            data=dict(name="Manuel Flores", address1="123 Fuel St.", address2="1234 Fuel St.", city="", state="TX", zipcode="77346"),
            follow_redirects=True
        )
        self.assertTrue(b'city is needed' in response.data)

if __name__ == '__main__':
    unittest.main()