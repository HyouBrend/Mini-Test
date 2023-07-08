import requests
from datetime import datetime

api_url = "http://api.openweathermap.org/data/2.5/forecast?lat=-6.21462&lon=106.84513&appid=69e94e1a4a7a2d781d9b00ec0921d3da"

response = requests.get(api_url)
weather_data = response.json()

current_time = datetime.now()

print("Weather Forecast for the Next 5 Days:")
forecast = []
day_count = 0

for data in weather_data["list"]:
    forecast_time = datetime.fromtimestamp(data["dt"])

    if forecast_time.date() != current_time.date():
        day_name = forecast_time.strftime("%a")
        date = forecast_time.strftime("%d %b %Y")

        temperature = round(data["main"]["temp"] - 273.15)

        forecast.append((day_name, date, temperature))
        current_time = forecast_time

        day_count += 1
        if day_count == 5:
            break

for day_name, date, temperature in forecast:
    print(f"{day_name}, {date}: {temperature}°C")


