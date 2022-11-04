# Brian, Vansh, Weichen
# SoftDev
# K19 -- Sessions Greetings
# 2022-11-03 
# time spent: 30 mins


from flask import Flask, redirect, url_for             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


users = {'m':'donky'}


@app.route("/") #, methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return render_template('response.html',
        user=session["username"])
    return render_template( 'login.html',)


@app.route("/auth") # , methods=[ 'POST'])
def authenticate():
    if request.method == 'GET':
        user = request.args.get('username')
        password = request.args.get('password')
        if user not in users.keys(): #check if user exists
            error = "User DNE"
            return render_template('login.html',
            error=error)
        if password != users[user]: #check if password matches user
            error = "Wrong Password"
            return render_template('login.html',
            error=error)
        session["username"] = user
        return redirect(url_for('index'))  #redirects to home page


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
