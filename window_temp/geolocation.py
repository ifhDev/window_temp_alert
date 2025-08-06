import pgeocode


def get_lat_lon(zip_code, country_code):
    """
    Returns the latitude and longitude for a given zip code and country code using pgeocode.
    
    Args:
        zip_code (str): The postal/zip code.
        country_code (str): The two-letter country code (e.g., 'DE', 'US').
    Returns:
        tuple: (latitude, longitude) as floats.
    Raises:
        ValueError: If geocoordinates cannot be found for the input.
    """

    nomi = pgeocode.Nominatim(country_code.upper())
    result = nomi.query_postal_code(zip_code)
    if result is None or result.latitude is None or result.longitude is None:
        raise ValueError(f"Could not find geo-coordinates for {zip_code} in {country_code}.")
    return float(result.latitude), float(result.longitude)

if __name__ == "__main__":
    """
    Standalone test for get_lat_lon utility.
    Run as a script to check geocoordinates for given zip/country.
    """

    zip_code = input("Enter your postal/zip code: ").strip()
    country_code = input("Enter your country code (e.g., DE, US): ").strip().upper()
    lat, lon = get_lat_lon(zip_code, country_code)
    print(f"Latitude: {lat}, Longitude: {lon}")