# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
import csv

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. 
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

users = {}

def get_users():
    with open('users.csv','r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for x in csv_reader:
            users[x[0]] = x[1] #puts csv file into dict

get_users() #populates users for first time

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html',)


@app.route("/auth") # , methods=[ 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    newuser = request.args['username']
    password = request.args['password']
    if newuser not in users.keys(): #check if user exists
        error = "User DNE"
        return render_template('login.html',
        error=error)
    if users[newuser] != password: #check if password matches user
        error = "Wrong Password"
        return render_template('login.html',
        error=error)
    
    return render_template('home.html',
        user=newuser,
        password=password,)  #redirects to home page

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'GET': #if opening this route
        return render_template('signup.html') 
    if request.method == 'POST': #if submitting information
        usernames = users.keys()
        newuser = request.form.get('username') #when using "POST" request.args DNE
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')
        if newuser in usernames: #check if user exists
            error = "Username already exists"
            return render_template('signup.html', 
                error=error) #redirects back to page with error
        if password != confirmation: 
            error = "PASSWORDS DO NOT MATCH!!!!!!"
            return render_template('signup.html', 
                error=error)

        with open('users.csv','a') as csvfile: #if newuser works, add to csv
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([newuser,password])
        get_users() #update local dict to match csv

        return render_template('login.html')

@app.route("/logout")
def logout():
    return render_template( 'login.html' ) #brings back to homepage

@app.route("/allusers")
def allusers():
    usernames = list(users.keys())
    return render_template('allusers.html',
        usernames=usernames)



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
