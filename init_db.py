#!/usr/bin/python
import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
print ("Opened database successfully")

#  Molina's tables 
cur.execute("DROP TABLE IF EXISTS FuelQuoteData")
cur.execute('''CREATE TABLE FuelQuoteData          
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    custId INTEGER NOT NULL,
    date DATE NOT NULL,
    gallons INTEGER NOT NULL,
    fuel TEXT NOT NULL,
    quote REAL NOT NULL)''')      # custID should match custID in profile table, based on login status 

cur.execute("DROP TABLE IF EXISTS FuelPrices")
cur.execute('''CREATE TABLE FuelPrices 
    (state TEXT PRIMARY KEY NOT NULL,
    diesel REAL NOT NULL,    
    regUnl REAL NOT NULL,
    premUnl REAL NOT NULL)''')    # state column will have either 'Texas' or 'other' 


#cur.execute("INSERT INTO FuelPrices (state, diesel, regUnl, premUnl) \
#    VALUES ('Texas', '4.00', '3.90', '4.20')")

conn.commit()
print ("Records created successfully")
conn.close()

# Manuel's Table

cur.execute("DROP TABLE IF EXISTS createprofile")
cur.execute("""CREATE TABLE createprofile (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            custId INTEGER NOT NULL,
            state TEXT NOT NULL,
            name TEXT PRIMARY KEY NOT NULL,
            address1 TEXT NOT NULL,
            address2 TEXT NOT NULL,
            city TEXT NOT NULL,
            zipcode INTEGER NOT NULL
            )""")


cur.execute("INSERT INTO FuelQuoteData (custId, name, address1, address2, city, zipcode) \
    VALUES ('001','Manuel Flores', '123 Fuel St.', '123 Fuel St.', 'Houston', 77346)")

conn.commit()
print ("Records created successfully")
conn.close()