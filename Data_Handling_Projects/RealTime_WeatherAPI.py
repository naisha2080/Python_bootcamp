"""
Real Time Weather Logger (API + CSV)

Built a python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

It should : 
- Ask the user for a city name
- Fetch the data using API and store it into a csv `weather_log.csv`:
    date, city, temp, weather conditions
- Prevent duplicate entries.
- Allow users to add new weather logs, view all logs, show average, highest, lowest temp and most freq conditions.
"""

import os
import csv
import requests
from datetime import datetime


FILENAME = "weather_logs.csv"
API_KEY = ""
#keys are usually hidden in .env file but that is for later.

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Condition"])

def weather_log():
    city = input("Enter the city name: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["City"].lower() == city.lower() and row["Date"] == date:
                print("Entry for this city with this date already exists ")
                return
            
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print("API Error! ")
            return
        
        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]

        with open(FILENAME, "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date, city.title(), temp, condition])
            print(f"Logged: {temp} {condition} in {city.title()} on {date}")

    except Exception as e:
        print("Failed to make API call")


def view_logs():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) <= 1:
            print("No Entries")
            return
        
        for row in reader:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")


def main():
    while True:
        print("Real-Time Weather Logger")
        print("1. Add weather log")
        print("2. View all logs")
        
        choice = input("Choose an option(1-4): ")

        match choice:
            case "1": weather_log()
            case "2": view_logs()
            case _: print("Choose a valid Option")

if __name__ == "__main__":
    main()