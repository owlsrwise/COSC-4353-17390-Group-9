def validate(name, address1, address2, city, state, zipcode):
    
    # verify all inputs are strings
    
    if not isinstance(name, str):
        return False

    if not isinstance(address1, str):
        return False 
    
    if not isinstance(address2, str):
        return False 
    
    if not isinstance(city, str):
        return False 
    
    if not isinstance(state, str):
        return False

    if not isinstance(zipcode, str):
        return False 

    return True
    

