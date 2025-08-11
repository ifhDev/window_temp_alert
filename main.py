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
        daytime = is_daytime()

        if daytime:
            target = indoor <= outdoor
            diff = indoor - outdoor
            success_msg = "OK, close your window :)"
            status_msg = f"It is still {diff :.1f} °C cooler outside."
        else:
            target = outdoor < indoor
            diff = outdoor - indoor
            success_msg = "OK, open your window :)"
            status_msg = f"It is still {diff:.1f} °C warmer outside."
        
        # check for target
        if target:
            print(success_msg)
            input("Press Enter to exit...")
            break

        # status update
        print(f"Indoor: {indoor:.1f}°C | Outdoor: {outdoor:.1f}°C")
        print(status_msg)
        
        # check wait time
        wait_time(indoor, outdoor)

# Todo:
# * add "test call" that shows crossover time (part of weather_api.py?)
# * add Fahrenheit option ("units.py")

if __name__ == "__main__":
    main()