
from flask import session, Flask, render_template, request

app = Flask(__name__)

key = "fyIy4iueEY2oLgyb1QISyNPtoANQZK26Nn6vhQGz"

@app.route("/")
def home():
    return render_template('main.html',
        key=key)




if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()


