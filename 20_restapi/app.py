"""
Soup Noodles (Jeff Chen, Brian Chen)
SoftDev
K20: A RESTful Journey Skyward
2022-11-22
time spent: 1
"""
from flask import session, Flask, render_template, json
from urllib.request import urlopen

app = Flask(__name__)


@app.route("/")
def home():
    api = None
    with open('key_nasa.txt', 'r') as f:
        api = f.read() 
    #print(api)#checks for api reading
    URL = f"https://api.nasa.gov/planetary/apod?api_key={api}"
    #print(URL)#checks for getting correct URL
    response = urlopen(URL)#grabs the JSON from the page
    data_json = json.loads(response.read())#reads the JSON of the page and turns it into a dictionary
    #print(data_json)#checks for correct retrieval of JSON

    return render_template('main.html', title=data_json['title'], image=data_json['url'], desc=data_json['explanation'])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()


