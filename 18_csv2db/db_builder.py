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

courses = {}
with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        courses[row['code']] = [row['id'],row['mark']]


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
classes = {}

for i in list(courses.keys()):
    classes.add(i)

student_gradebook = "(id int"

for i in classes:
    student_gradebook += f", {i} text"

student_gradebook += ")"

print(student_gradebook)

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

command = "drop table students;"         
c.execute(command)


command = "create table students(name text, age int, id int)"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

student_ids = list(students.keys())
for x in student_ids:
    command = f"insert into students values('{students[x][0]}',{students[x][1]},{x});"  
    c.execute(command)



#==========================================================

db.commit() #save changes
db.close()  #close database


