#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

students = {}
with open('students.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students[row['id']] = [row['name'],row['age']]

print(students)
        

#print(students)


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

command = "drop table students;"         
c.execute(command)

command = "create table students(name text, age int, id int);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

for x in list(students.keys()):
    command = f"insert table students;"         



#==========================================================

db.commit() #save changes
db.close()  #close database


