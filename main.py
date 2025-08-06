from window_temp import *
from config import ZIP_CODE, COUNTRY_CODE, API_KEY

def main():
    """
    Checks local outdoor temperature at regular intervals and notifies you
    when it is cooler outside than inside. Ctrl+C exits at any time.
    """

    ensure_config()
    zip_code = ZIP_CODE
    country_code = COUNTRY_CODE
    api_key = API_KEY
    lat, lon = get_lat_lon(zip_code, country_code)
    while True:
        try:
            indoor = float(input("Input the current temperature inside (°C): "))
            break
        except ValueError:
            print("Please enter a valid number.")
    print("Remember: You can safely exit this app at any time using Ctrl+C (or Cmd+C on Mac) or by closing the window.")

    while True:
        outdoor = current_weather(lat, lon, api_key)
        if outdoor < indoor:
            print("OK, open your window :)")
            input("Press Enter to exit...")
            break
        print(f"Indoor: {indoor:.1f}°C | Outdoor: {outdoor:.1f}°C")
        print(f"It is still {outdoor - indoor:.1f} °C warmer outside.")
        wait_time(indoor, outdoor)

# Todo:
# * add "test call" that shows crossover time (part of weather_api.py?)
# * add Fahrenheit option ("units.py")
# * add functionality for morning/evening (when to close vs when to open, part of time_utils.py)

if __name__ == "__main__":
    main()