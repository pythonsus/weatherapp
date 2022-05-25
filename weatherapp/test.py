import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"Fort Mill,us","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"json"}

headers = {
	"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
	"X-RapidAPI-Key": "dc3de1e0b4mshfb4ca4e2c4e695ep121b91jsn25d854aa7129"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)