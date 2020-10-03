#!/usr/bin/env python3
import sqlite3

#connect to database file
dbconnect = sqlite3.connect("mydatabase.db")
dbconnect.row_factory = sqlite3.Row

#now we create a cursor to work with 
cursor = dbconnect.cursor()


def printResult(results, message):

    print(message+':\n')
    # print(results[0]['id'])
    for result in results:
        print( str(result['sensorID'])+'---'+result['type']+'---'+result['zone'] )
    print('\n')


#Create sensors datatable
cursor.execute('create table if not exists sensors(sensorID integer, type TEXT, zone TEXT ) ')

#all the rows
rows=[ [1,'door', 'kitchen'],[2,'temperature', 'kitchen'],[3,'door', 'garage'],[4,'door', 'garage'],[5,'temperature', 'garage'] ]

for row in rows:
    cursor.execute('insert into sensors values('+str(row[0])+',"'+row[1]+'","'+row[2]+'")')
    dbconnect.commit()


# Displaying all the sensors in the kitchen
rows=cursor.execute('SELECT * FROM sensors WHERE zone="kitchen"').fetchall()
printResult(rows,' Displaying all the sensors in the kitchen ')

# Displaying all the door sensors 
rows=cursor.execute('SELECT * FROM sensors WHERE type="door"').fetchall()
printResult(rows,'Displaying all the door sensors ')





dbconnect.close()