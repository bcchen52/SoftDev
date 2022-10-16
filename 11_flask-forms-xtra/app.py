# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

import re
from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

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
logged_in = False

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
    return render_template( 'login.html' )


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
    if newuser not in users.keys():
        error = "User DNE"
        return render_template('login.html',
        error=error)
    if users[newuser] != password:
        error = "Wrong Password"
        return render_template('login.html',
        error=error)
    return render_template('home.html',
        user=newuser,
        password=password,)  #response to a form submission

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        usernames = users.keys()
        newuser = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')
        if newuser in usernames:
            error = "Username already exists"
            return render_template('signup.html', 
                error=error)
        if password != confirmation:
            error = "PASSWORDS DO NOT MATCH!!!!!!"
            return render_template('signup.html', 
                error=error)
        users[newuser] = password
        return render_template('login.html')


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
