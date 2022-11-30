import requests, json

url = "https://love-calculator.p.rapidapi.com/getPercentage"

querystring = {"fname":"sdhfbksdfsfsfs","sname":"sjfdnsdfsdfd"}

headers = {
	"X-RapidAPI-Key": "9989e8d9c1mshd9e621bfaf2a690p1fabeajsn292bb4077585",
	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
#data = response.text

print(data["percentage"])