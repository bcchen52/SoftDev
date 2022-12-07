import requests, json

#nba testing

#year gets nab schedule for any year
year = "2022"

url = f"https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/{year}/league/00_full_schedule.json"

response = requests.request("GET", url)

data = json.loads(response.text)
data = data['lscd']
data = data[7]['mscd']['g']

#the 7 is for the month. The data in "lcsd" is a list, and it is numbered numberically from
#0-7, which has each month the NBA is in season with 7 being december, the last month
#Then you enter the 'mscd' or match schedule for the month you are in, and 'g' for the list of games

print(len(data))

for x in data:
    print(f"The {x['h']['tc']} {x['h']['tn']} will be playing the {x['v']['tc']} {x['v']['tn']} at {x['stt']} on {x['gdte']}") 

#h for home team, v for visiting team. Within those two, tn is team name and tc is team city
#stt is time in ET, and gdte is the date