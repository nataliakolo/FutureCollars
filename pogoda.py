from datetime import datetime

import requests


def is_search_in_history(formatted_date):
    try:
        with open("weather_history.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                if formatted_date in line:
                    return True
        return False
    except FileNotFoundError:
        return False


def save_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write("Historia:\n")
        for item in data:
            file.write(f"{item}\n")
        file.write("\n")


latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")
date_string = input("Enter a date (YYYY-MM-DD): ")

historia = []

try:
    if not date_string.strip():
        date_object = datetime.now()
    else:
        date_object = datetime.strptime(date_string, "%Y-%m-%d")
    formatted_date = date_object.strftime("%Y-%m-%d")

    # Check if the current search is in the history
    if is_search_in_history(formatted_date):
        print("Ta data juz był wyszukiwana")
    else:
        api_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={formatted_date}&end_date={formatted_date}'
        print("API URL:", api_url)
        response = requests.get(api_url)

        if response.status_code == 200:
            posts = response.json()
            historia.append(("date", formatted_date))
            historia.append(("latitude", latitude))
            historia.append(("longitude", longitude))

            for x in range(0, len(posts["hourly"]["time"])):
                if isinstance(posts["hourly"]["rain"][x], float):
                    if float(posts["hourly"]["rain"][x]) == 0.0:
                        komentarz = f"{posts['hourly']['time'][x]} nie bedzie padać"
                    elif float(posts["hourly"]["rain"][x]) > 0.0:
                        komentarz = f"{posts['hourly']['time'][x]} bedzie padać ({posts['hourly']['rain'][x]})"
                else:
                    komentarz = f"{posts['hourly']['time'][x]} brak prognozy"

                historia.append(komentarz)
                print(komentarz)

            # Save to file
            save_to_file("weather_history.txt", historia)

        else:
            print(f"Error: Unable to fetch data, Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")