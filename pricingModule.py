class pricing:
    def getTotal(self, state, prevUser, gallons, fuelType):
    
        #Location Factor = 2% for Texas, 4% for out of state. ( 0.2 OR 0.4)
        #Rate History Factor = 1% if client requested fuel before, 0% if no history (you can query fuel quote table to check if there are any rows for the client)
        #Gallons Requested Factor = 2% if more than 1000 Gallons, 3% if less (0.2 OR 0.3)

        # company profit always at 10%    
        companyprofit = 0.1

        #assigns the Gallons Requested Factor
        if gallons >= 1000:
            gallonsrequestfactor = .02
        else:
            gallonsrequestfactor = .03 
        
        #assigns Location Factor
        if state == "TX":
            locationfactor = .02
        else:
            locationfactor = .04
        
        #assigns ratehistory
        if prevUser == 1:   #yes previous customer
            ratehistory = .01
        else:
            ratehistory = 0

        #calculates correct price based on fuel type chosen by user: 
        
        if fuelType == "regUnl":
            currentprice = 1.50
        elif fuelType == "premUnl":
            currentprice = 1.50 + .25   
        else:
            currentprice = 1.50 + .75   #diesel

        margin = currentprice * (locationfactor - ratehistory + gallonsrequestfactor + companyprofit)

        suggestedPrice = currentprice + margin   #per gallon


        return suggestedPrice