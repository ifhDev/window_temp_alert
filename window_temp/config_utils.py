import os

def ensure_config():
    """
    Checks for an existing config.py file.
    If not found, prompts the user for zip code, country code, and API key, then creates the file.
    """

    if not os.path.exists("config.py"):
        print("Config file not found. Please input data.")
        zip_code = input("Enter your postal/zip code: ").strip()
        country_code = input("Enter your country code (e.g., DE, US): ").strip().upper()
        print("If you do not have an OpenWeatherMap API key, register on this site to create one for free: https://home.openweathermap.org/")
        print("You can find your free key at the following link: https://home.openweathermap.org/myservices")
        api_key = input("Enter your OpenWeatherMap API key: ").strip()

        with open("config.py", "w", encoding="utf-8") as f:
            f.write(f"ZIP_CODE = \"{zip_code}\"\n")
            f.write(f"COUNTRY_CODE = \"{country_code}\"\n")
            f.write(f"API_KEY = \"{api_key}\"\n")
        print("Config file created! You won't be asked again and you can edit your details in the file at any time.")

if __name__ == "__main__":
    ensure_config()