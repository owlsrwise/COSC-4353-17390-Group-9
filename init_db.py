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

#Nicole's table



cur.execute("DROP TABLE IF EXISTS userinfo")
cur.execute('''CREATE TABLE userinfo          
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    password TEXT)''') 


cur.execute("DROP TABLE IF EXISTS userinfo2")
cur.execute('''CREATE TABLE userinfo2          
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    email TEXT,
    password1 TEXT,
    password2 TEXT)''') 


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


conn.commit()
print ("Records created successfully")
conn.close()