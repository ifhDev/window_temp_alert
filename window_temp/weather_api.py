import requests
import json

def current_weather(lat, lon, api_key):
    """
    Fetches the current outdoor temperature (in °C) from OpenWeatherMap for a given latitude and longitude.

    Args:
        lat (float): Latitude.
        lon (float): Longitude.
        api_key (str): OpenWeatherMap API key.
    Returns:
        float: The current outdoor temperature in Celsius.
    Side effect:
        Saves the full JSON API response to 'weather.json' for debugging.
    """

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
    data = response.json()
    with open("weather.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    outdoor_temp = data["main"]["temp"]
    return outdoor_temp