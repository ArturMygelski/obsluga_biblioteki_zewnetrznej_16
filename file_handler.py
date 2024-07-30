import json

class WeatherForecast:

    def __init__(self, file):
        self.file = file
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file) as file:
            return json.loads(file.read())

    def save_data_to_file(self):
        with open(self.file, mode="w") as file:
            file.write(json.dumps(self.data))

    def get_weather_data(self, city, date):
        return self.data.get(city, {}).get(date)

    def save_weather_data(self, city, date, weather_info):
        if city not in self.data:
            self.data[city] = {}
        self.data[city][date] = weather_info
        self.save_data_to_file()
    def __setitem__(self, key, value):
        city, date = key
        if not self.data.get(city):
            self.data[city] = {}
        self.data[city][date] = value

    def __getitem__(self, item):
        city, date = item
        for key, info in self.data.items():
            if city == key:
                for date_key, weather_conditions in info.items():
                    if date == date_key:
                        return weather_conditions
    def __iter__(self):
        return iter(self.data)

    def items(self):
        for city, date in self.data.items():
            yield f"{city}, {date}"


