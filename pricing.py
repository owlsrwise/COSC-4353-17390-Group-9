class pricing:
    def gettotal(locationfactor,ratehistory,gallonsrequestfactor):
    
        #Location Factor = 2% for Texas, 4% for out of state. ( 0.2 OR 0.4)
        #Rate History Factor = 1% if client requested fuel before, 0% if no history (you can query fuel quote table to check if there are any rows for the client)
        #Gallons Requested Factor = 2% if more than 1000 Gallons, 3% if less (0.2 OR 0.3)


     # company profit always at 10%    
     companyprofit = 0.1
     #current price always 1.50 for simplicity 
     currentprice = 1.50
     margin = currentprice * ( locationfactor - ratehistory + gallonsrequestfactor + companyprofit)

     suggestedPrice = currentprice + margin


     return suggestedPrice

    