from flask import Flask, render_template, request

import requests, json

app = Flask(__name__)

summonerID = ""
api_key = "RGAPI-e30db9bf-29d6-4147-b6b7-e8cd04f279bd"

params = {
    "api_key":api_key
}

champs = {}
def get_champs():
    url = "http://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion.json"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    #print(data)
    data = data["data"]
    for x in list(data.keys()):
        champs[int(data[x]["key"])] = x
    print(champs)
    
get_champs()

def get_champ(id):
    return(champs[id])


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return(render_template("main.html"))
    if request.method == "POST":
        user = request.form.get("user")
        summonerName = user

        userURL = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?"

        response = requests.request("GET", userURL, params=params)
        
        data = json.loads(response.text)

        summonerID = data["id"]

        masteryURL = f"https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summonerID}?"

        response = requests.request("GET", masteryURL, params=params)
        
        data = json.loads(response.text)
        
        for x in data:
            x["championName"] = get_champ(x["championId"])
        
        return(render_template("response.html",
            champs = data,
            ))




if __name__ == "__main__": #false if this file imported as module
#enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()