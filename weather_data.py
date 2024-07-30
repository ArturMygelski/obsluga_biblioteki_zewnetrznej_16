import requests
from utils import get_coordinates


def get_weather_data(city, date):
    latitude, longitude = get_coordinates(city)

    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&"
        f"timezone=Europe%2FLondon&start_date={date}&end_date={date}")

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rain_sum = data.get('daily', {}).get('rain_sum', [None])[0]
        if not rain_sum or rain_sum < 0:
            return "Nie wiem"
        elif rain_sum > 0:
            return "Pada"
        else:
            return "Nie pada"
    else:
        return "Nie wiem"
