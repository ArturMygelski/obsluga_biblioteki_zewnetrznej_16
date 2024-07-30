from file_handler import WeatherForecast
from weather_data import get_weather_data
from datetime import datetime, timedelta


file_handler = WeatherForecast("data.json")

city = input("Podaj miasto: ")
date_input = input("Podaj datę  w formacie (YYYY-MM-DD): ")

if not date_input:
    date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
else:
    date = date_input

file_handler[("Legnica", "2024-07-30")] = "nie pada"
file_handler.save_data_to_file()
# weather_info = file_handler.get_weather_data(city, date)
# if weather_info:
#     print(f"Dane dla {city} na dzień {date} już istnieją: {weather_info}")
# else:
#     weather_info = get_weather_data(city, date)
#     file_handler.save_weather_data(city, date, weather_info)
#     print(f"Pobrane dane dla {city} na dzień {date}: {weather_info}")