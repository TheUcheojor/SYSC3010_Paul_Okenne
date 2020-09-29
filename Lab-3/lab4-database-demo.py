#!/usr/bin/env python3
import sqlite3

#connect to database file
dbconnect = sqlite3.connect("mydatabase.db")

dbconnect.row_factory = sqlite3.Row

#now we create a cursor to work with 
cursor = dbconnect.cursor()

#Create sensors datatable
cursor.execute('create table if not exists sensors(sensorID integer, type TEXT, zone TEXT ) ')

#all the rows
rows=[ [1,'door', 'kitchen'],[2,'temperature', 'kitchen'],[3,'door', 'garage'],[4,'door', 'garage'],[5,'temperature', 'garage'] ]

for row in rows:
    print('insert into sensors values('+str(row[0])+',"'+row[1]+'","'+row[2]+'")')
    cursor.execute('insert into sensors values('+str(row[0])+',"'+row[1]+'","'+row[2]+'")')
    dbconnect.commit()

dbconnect.close()