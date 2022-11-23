from flask import session, Flask, render_template, json, request
from urllib.request import urlopen

app = Flask(__name__)




@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('main.html')

@app.route("/getinfo", methods=['GET', 'POST'])
def getinfo():
    if request.method == "POST":
        height = request.form.get('height')
        weight = request.form.get('weight')
        age = request.form.get('age')
        gender = request.form.get('gender')
        req = request.form.get('req')
        URL = f"https://urvipaithankar.herokuapp.com/{req}/index.php/{height}/{weight}/{age}/{gender}"

        response = urlopen(URL)
        data_json = json.loads(response.read())
        print(data_json)
        
        return render_template('response.html',
            height=height,
            weight=weight,
            age=age,
            gender=gender,
            req=req,
            number=data_json[req])





if __name__ == "__main__": #false if this file imported as module
#enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()