from datetime import datetime
import requests


class WeatherForecast:
    def __init__(self, filename="weather_history.txt"):
        self.filename = filename
        self.historia = []

    def __getitem__(self, data):
        for line in self.historia:
            if data in line:
                return line + " to jest getter"

    def __setitem__(self, data, value):
        for index, item in enumerate(self.historia):
            if data in item:
                self.historia[index] = value

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.historia):
            result = self.historia[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration

    def items(self):
        for item in self.historia:
            if isinstance(item, tuple) and len(item) == 2:
                yield item

    def is_search_in_history(self, formatted_date):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if formatted_date in line:
                        return True
            return False
        except FileNotFoundError:
            return False

    def save_to_file(self):
        with open(self.filename, 'a') as file:
            file.write("Historia:\n")
            for item in self.historia:
                file.write(f"{item}\n")
            file.write("\n")

    def get_weather_forecast(self, latitude, longitude, date_string):
        try:
            if not date_string.strip():
                date_object = datetime.now()
            else:
                date_object = datetime.strptime(date_string, "%Y-%m-%d")
            formatted_date = date_object.strftime("%Y-%m-%d")

            # Check if the current search is in the history
            if self.is_search_in_history(formatted_date):
                print("Ta data już była wyszukiwana.")
            else:
                api_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={formatted_date}&end_date={formatted_date}'
                print("API URL:", api_url)
                response = requests.get(api_url)

                if response.status_code == 200:
                    posts = response.json()
                    self.historia.append(("date", formatted_date))
                    self.historia.append(("latitude", latitude))
                    self.historia.append(("longitude", longitude))

                    for x in range(0, len(posts["hourly"]["time"])):
                        if isinstance(posts["hourly"]["rain"][x], float):
                            if float(posts["hourly"]["rain"][x]) == 0.0:
                                komentarz = f"{posts['hourly']['time'][x]} nie bedzie padać"
                            elif float(posts["hourly"]["rain"][x]) > 0.0:
                                komentarz = f"{posts['hourly']['time'][x]} bedzie padać ({posts['hourly']['rain'][x]})"
                        else:
                            komentarz = f"{posts['hourly']['time'][x]} brak prognozy"

                        self.historia.append(komentarz)
                        print(komentarz)

                    # Save to file
                    self.save_to_file()

                else:
                    print(f"Error: Unable to fetch data, Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")



weather_forecast = WeatherForecast()

latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")
date_string = input("Enter a date (YYYY-MM-DD): ")

weather_forecast.get_weather_forecast(latitude, longitude, date_string)


print("2023-12-08T03:00" )
print(weather_forecast["2023-12-08T03:00"])
weather_forecast["2023-12-13T03:00"]="test"
weather_forecast["2023-12-13T03:00"]="test2"
for value in weather_forecast:
    print(value)

print("===========================")
for item in weather_forecast.items():
    print(item)
