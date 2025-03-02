

import requests 

city = input("Enter your city _")

api_key = "47bc95d7842b8c810826c7bfc18d0595"
url = "http://api.openweathermap.org/data/2.5/weather"
params = {

    "q": city,
    "appid": api_key,
    "units": "metric"

        }
re = requests.get(url , params=params)
info = re.json()

status = re.status_code


if status == 200:
    city = info["name"]
    temp = info["main"]["temp"]
    weather = info["weather"][0]["description"]
    hum = info["main"]["humidity"]
    wind = info["wind"]["speed"]
    see = info["main"]["sea_level"]

    print(f" weather in {city} ")
    print(f" Temprature of city {temp} .C")
    print(f" weather in {weather} ")
    print(f" humidity in {hum}%")
    print(f" wind_speed in {wind} m/s" ) 
    print(f" see_level of {city , see}")
    
else:
    print()
    print(f"** city {city} not Found **" )


