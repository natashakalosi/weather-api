# weather-api
A Python command-line tool that fetches live weather data for any city in the world using the Open-Meteo API.

### Key Features
- **Smart Search:** Uses Geocoding to find coordinates (Latitude/Longitude) from a city name.
- **Live Data:** Fetches real-time temperature from global weather stations.
- **Robustness:** Includes error handling for network issues or invalid city names.

### Built With
- **Python**
- **Requests Library:** For API communication.
- **Open-Meteo API:** A free and reliable weather data source.

### How to Run
1. Install requirements: `pip install requests`
2. Run the script: `python weather.py`
3. Enter any city name (e.g., "Athens", "London", "Tokyo").
