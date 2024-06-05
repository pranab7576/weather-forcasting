import requests
import json
from urllib.request import urlopen

url='http://ipinfo.io/json'
response=urlopen(url)
data1=json.load(response)

preety_data=json.dumps(data1,indent=4)
my_location=data1['loc'].split(',')

lat=my_location[0]
lon=my_location[1]

#print(f'{lat} \n {lon}')


# api to fetch weather of city
#city_name=input("Enter city name: ")
api_key="0e68d61e3eb270ef1335a6081ec0dbb6"
api_url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={"0e68d61e3eb270ef1335a6081ec0dbb6"}&units=metric"
get_info=requests.get(api_url)
data=get_info.json()
#print(data)
#formatting data in preety format
preety_data=json.dumps(data,indent=4)
#print(preety_data)
Des=data["weather"][0]["description"]
temp=data["main"]["temp"]
feel_like=data["main"]["feels_like"]
print(f"Weather now: {temp}°C \t feels like: {feel_like}\n  {Des}")