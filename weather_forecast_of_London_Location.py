import requests
import os
from datetime import datetime

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    return response.json()

def get_weather_by_date(weather_data, date):
    for data in weather_data['list']:
        if data['dt_txt'].startswith(date):
            return data['main']['temp']
    return None

def get_wind_speed_by_date(weather_data, date):
    for data in weather_data['list']:
        if data['dt_txt'].startswith(date):
            return data['wind']['speed']
    return None

def get_pressure_by_date(weather_data, date):
    for data in weather_data['list']:
        if data['dt_txt'].startswith(date):
            return data['main']['pressure']
    return None

def main():
    weather_data = get_weather_data()

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD format): ")
            temperature = get_weather_by_date(weather_data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature}°C")
            else:
                print("No data available for the given date.")
        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD format): ")
            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed is not None:
                print(f"Wind speed on {date}: {wind_speed} m/s")
            else:
                print("No data available for the given date.")
        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD format): ")
            pressure = get_pressure_by_date(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("No data available for the given date.")
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
