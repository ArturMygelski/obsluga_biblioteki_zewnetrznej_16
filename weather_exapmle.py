from geopy.geocoders import Nominatim
import requests

city = input("Podaj miasto: ")
date = input("Podaj datę: ")

geolocator = Nominatim(user_agent="michal_zietkowski_app")
location = geolocator.geocode(city)
latitude = location.latitude
longitude = location.longitude
print(latitude)
print(longitude)

url_address = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&"
               f"timezone=Europe%2FLondon&start_date={date}&end_date={date}")

get_request = requests.get(url_address)
print(get_request.status_code)
print(get_request.json())