from string import( ascii_lowercase, ascii_uppercase, digits, punctuation, whitespace)

def is_validsize (pass1: str = "") -> bool:
      Mins = 3
      Maxs = 20
      passsize = len(pass1)
      return Mins <= passsize <= Maxs
def createacc(user:str= "" )-> bool:
        
    try:
        if not user:
            return False
        newpass = user.strip()
        if not is_validsize(newpass):
                 return False
        
        return True
    except:
         return False
def checkpasswords(pass1: str , pass2 : str)-> bool:
      try: 
          if pass1 != pass2:
              return False
          return True
      except: 
          return False     
