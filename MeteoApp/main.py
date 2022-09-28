import requests

app_id = "ae97c65bf76cef416ac3b8aeb6e4cac0"

city = "Moscow, RU"


data = {
    'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': app_id
}


req_weather = requests.get(
    "http://api.openweathermap.org/data/2.5/weather", params=data).json()

wind_speed = req_weather["wind"]["speed"]
visibility = req_weather["visibility"]

print("Today:", wind_speed, visibility)

req_forecast = requests.get(
    "http://api.openweathermap.org/data/2.5/forecast", params=data).json()

for val in req_forecast["list"]:
    print(val["dt_txt"], val["wind"]["speed"], val['visibility'])
