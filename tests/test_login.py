import unittest
from login_func import checkpasswords
from login_func import is_validsize
from login_func import createacc

class test_validsize(unittest.TestCase):
   def test_emptypass(self):
       self.assertFalse(is_validsize(""))
   def test_emptypass2(self):
       self.assertFalse(is_validsize())

   def test_shortpass(self):
       self.assertFalse(is_validsize("pa"))

   def test_longpass(self):
       self.assertTrue(is_validsize("password"))

   def test_verylongpass(self):
       self.assertTrue("Thisisaveryverylongpassword2022")

class test_createacc(unittest.TestCase):
    def test_userempty(self):
        self.assertFalse(createacc())

    def test_shortuser1(self):
        self.assertFalse(createacc("p"))

    def test_shortuser2(self):
        self.assertFalse(createacc("pa"))

    def test_shortuser3(self):
        self.assertFalse(createacc("_a"))
    def test_longusername(self):
        self.assertFalse(createacc("thisismyusernamewhichislong1234"))

class test_passwords(unittest.TestCase):
    def test_passarediff1(self):
        self.assertFalse(checkpasswords("hi","bye"))
    def test_passareempty1(self):
        self.assertFalse(checkpasswords("","notempty"))
    def test_passwordmatch(self):
        self.assertTrue(checkpasswords("pinkpass","pinkpass"))
    def test_longpassword(self):
        self.assertTrue(checkpasswords("thisisthesamepassword","thisisthesamepassword"))
    def test_shortpassword(self):
        self.assertTrue(checkpasswords("tiny","tiny"))
    def test_smolpassmatch(self):
        self.assertTrue(checkpasswords("sm","sm"))

if __name__ == '__main__':
    unittest.main()
