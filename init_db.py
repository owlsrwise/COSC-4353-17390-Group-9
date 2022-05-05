#!/usr/bin/python
import sqlite3

def init_db(conn):
    cur = conn.cursor()

    # Nicole's tables
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='userinfo'")
    if cur.fetchone()==None: 
        cur.execute('''CREATE TABLE userinfo          
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            password TEXT)''') 

    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='userinfo2'")
    if cur.fetchone()==None:
        cur.execute('''CREATE TABLE userinfo2          
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            email TEXT,
            password1 TEXT,
            password2 TEXT)''') 

    #  Molina's tables 
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='FuelQuoteData'")
    if cur.fetchone()==None:
        cur.execute('''CREATE TABLE FuelQuoteData          
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            custId INTEGER NOT NULL,
            date DATE NOT NULL,
            state TEXT NOT NULL,
            address1 TEXT NOT NULL,
            address2 TEXT NOT NULL,
            city TEXT NOT NULL,
            zipcode INTEGER NOT NULL,
            gallons INTEGER NOT NULL,
            fuel TEXT NOT NULL,
            quote REAL NOT NULL)''')       

    # Manuel's Table
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='createprofile'")
    if cur.fetchone()==None:
        cur.execute('''CREATE TABLE createprofile (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    custId INTEGER NOT NULL,
                    state TEXT NOT NULL,
                    name TEXT NOT NULL,
                    address1 TEXT NOT NULL,
                    address2 TEXT NOT NULL,
                    city TEXT NOT NULL,
                    zipcode INTEGER NOT NULL
                    )''')


    conn.commit()
    