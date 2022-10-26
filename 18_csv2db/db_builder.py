#Brian Chen, Vansh Saboo, Weichen Liu
#SoftDev  
#k18 -- A Mare Widge Made in Hebben
#2022-10-26
#time spent: 60 mins

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

students = {}
with open('students.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students[row['id']] = [row['name'],row['age']]

grades = {}
classes = set()

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['id'] not in grades:
            grades[row['id']] = [(row['code'],int(row['mark']))]
        else:
            grades[row['id']].append([row['code'],int(row['mark'])])
        #print(grades[row['id']])
        classes.add(row['code']) #create a set of classes

class_template = {}

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

student_gradebook = "(id int, name text"

for i in classes:
    student_gradebook += f", {i} int" #student gradebook will be used to create the grades table
    class_template[i] = "null" #the class_template dict will be populated with grades, and will be in the same order as the table is made in
                    
student_gradebook += ")" #create the arguments for create table

#print(student_gradebook)

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


command = "drop table if exists students;" #creating tables if they DNE causes issues, so does dropping if they DNE
c.execute(command)

command = "drop table if exists grades;"         
c.execute(command)


command = "create table students(name text, age int, id int);"      
c.execute(command)   

command = f"create table grades{student_gradebook};" #created from a set of classes in the csv file   
c.execute(command)    


for x in list(students.keys()):
    command = f'''insert into students values('{students[x][0]}',{students[x][1]},{x});
    '''
    c.execute(command)


#print(student_gradebook)

for x in list(grades.keys()):
    current_grades = class_template.copy() #super important to use copy and not newdict=olddict

    name = students[x][0] #grab student names using id 

    for i in grades[x]:
        current_grades[i[0]] = i[1] #populate current_grades with class information with grades. grades only has 
                                    #values for classes with information, while current_grades has all possible classes. 
                                    #Some values of current_grades will not be populated but the default value is 'null',
                                    #which can be passed to sqlite 

    command_msg = f"({x}, '{name}'"

    for i in list(current_grades.keys()):
        command_msg += f", {current_grades[i]}"

    command_msg += ")"

    #print(command_msg)
    command = f"insert into grades values{command_msg}"
    c.execute(command)


#==========================================================

db.commit() #save changes
db.close()  #close database


