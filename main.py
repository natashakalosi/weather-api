import requests

# 1. Ask the user for a location
city_name = input("Enter your city: ")

# --- STEP 1: Geocoding (Convert City Name to Coordinates) ---
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {
    "name": city_name,
    "count": 1,
    "language": "en",  # Changed to English
    "format": "json"
}

try:
    geo_response = requests.get(geo_url, params=geo_params)
    geo_response.raise_for_status() # Check if the request was successful
    geo_data = geo_response.json()

    # Check if the city was found
    if "results" in geo_data:
        location = geo_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        full_name = location["name"]
        country = location.get("country", "")

        print(f"Location found: {full_name}, {country} (Lat: {lat}, Lon: {lon})")

        # --- STEP 2: Fetch Weather Data using coordinates ---
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": "true"
        }

        weather_response = requests.get(weather_url, params=weather_params)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        temp = weather_data["current_weather"]["temperature"]
        print(f"The current temperature is: {temp}°C")

    else:
        print("Sorry, I couldn't find that location. Please try again!")

except requests.exceptions.RequestException as e:
    print(f"Error: Could not connect to the weather service. ({e})")
