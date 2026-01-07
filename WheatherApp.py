import requests
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise RuntimeError("API key not found. Check your .env file.")



class WeatherApp:
    def __init__(self, api_key: str, lang: str = "pt_br"):
        self.api_key = api_key
        self.lang = lang

    def get_coordinates(self, city_name: str) -> tuple[float, float] | None:
        url = (
            f"http://api.openweathermap.org/geo/1.0/direct"
            f"?q={city_name}&limit=1&appid={self.api_key}"
        )

        response = requests.get(url)
        data = response.json()

        if not data:
            return None

        lat = data[0]['lat']
        lon = data[0]['lon']
        return lat, lon

    def get_weather(self, lat: float, lon: float) -> dict:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?lat={lat}&lon={lon}"
            f"&appid={self.api_key}"
            f"&units=metric"
            f"&lang={self.lang}"
        )

        response = requests.get(url)
        return response.json()


def run_menu():
    app = WeatherApp(API_KEY)


    city_name = input("City Name: ")
    coords = app.get_coordinates(city_name)

    if not coords:
        print("City not found.")
        return

    lat, lon = coords
    weather_data = app.get_weather(lat, lon)

    while True:
        print(f"""
            --------- Options for {city_name} ---------
            1. Current Temperature
            2. Weather Condition
            3. Pressure and Humidity
            4. Exit
            """)

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Temperature: {weather_data['main']['temp']:.1f}°C")

        elif choice == "2":
            print(f"Condition: {weather_data['weather'][0]['description']}")

        elif choice == "3":
            print(f"""
                Pressure: {weather_data['main']['pressure']} hPa
                Humidity: {weather_data['main']['humidity']}%
                """)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")



if __name__ == "__main__":
    run_menu()


