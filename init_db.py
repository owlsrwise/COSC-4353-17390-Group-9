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

# temporary profile table (pending Manuel's table)
cur.execute("DROP TABLE IF EXISTS DummyProfile")
cur.execute('''CREATE TABLE DummyProfile          
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    custId INTEGER NOT NULL,
    fullName TEXT NOT NULL,
    address1 TEXT NOT NULL,
    address2 TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zipcode INTEGER NOT NULL)''') 

# initial values to test database
cur.execute("INSERT INTO FuelQuoteData (custId, date, gallons, fuel, quote) \
    VALUES ('001','02/18/2022', 5, 'regUnl', '19.50')")

cur.execute("INSERT INTO FuelPrices (state, diesel, regUnl, premUnl) \
    VALUES ('Texas', '4.00', '3.90', '4.20')")

cur.execute("INSERT INTO DummyPRofile (custId, fullName, address1, address2, city, state, zipcode) \
    VALUES ('001', 'Molina Davis', '2300 Street', 'Apt 5', 'Houston', 'Texas', 77004)")
    
conn.commit()
print ("Records created successfully")
conn.close()
