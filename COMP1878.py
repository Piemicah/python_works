import requests, json

key = "e16098e2d38a2dfc24546172e6fdff02"
headers = {"content-type": "application/json"}
url = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={key}"

response = requests.get(url)
data = json.loads(response.content.decode("utf-8"))
print(data)
