import requests

API_KEY = "d2113bd5b2a9a835c173992a3264691b"
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"

weather_params = {
    "lon":-73.579770,
    "lat": 45.495329,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
    "units": "metric"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

temp_avg = 0
feels_like_avg = 0
text = []

for hour_data in weather_slice:
    temp_avg += hour_data["temp"]
    feels_like_avg += hour_data["feels_like"]
    text.append(hour_data["weather"][0]["main"])
temp_avg = round(temp_avg/12, 2)
feels_like_avg = round(feels_like_avg/12, 2)
print(f"Average temp = {temp_avg}, Average feels like = {feels_like_avg},\n{text}")


