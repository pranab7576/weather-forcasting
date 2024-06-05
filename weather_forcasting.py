import requests
import json
from urllib.request import urlopen

#findingd /accessing my current location by generating request to website
url='http://ipinfo.io/json'
response=urlopen(url)
data1=json.load(response)

preety_data=json.dumps(data1,indent=4)
my_location=data1['loc'].split(',')

lat=my_location[0]
lon=my_location[1]

#fetching data from the server using API
api_key="API KEY"
api_url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={"API KEY"}&units=metric"
get_info=requests.get(api_url)
data=get_info.json()

#formatting data in preety format
preety_data=json.dumps(data,indent=4)
Des=data["weather"][0]["description"]
temp=data["main"]["temp"]
feel_like=data["main"]["feels_like"]
print(f"Weather now: {temp}°C \t feels like: {feel_like}\n  {Des}")