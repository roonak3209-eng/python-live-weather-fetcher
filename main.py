# Live Weather Fetcher - Main Script
# This program fetches and displays live weather information for any city

import requests
import json


def get_city_coordinates(city_name):
    """
    Convert city name to latitude and longitude using Open-Meteo Geocoding API.
    
    Args:
        city_name (str): Name of the city to search for
    
    Returns:
        tuple: (latitude, longitude, country) if found, None if not found or error occurs
    """
    try:
        # Build the API URL for geocoding
        geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
        
        # Parameters for the geocoding API
        params = {
            "name": city_name,
            "count": 1,           # Get only the first result
            "language": "en",     # Results in English
            "format": "json"
        }
        
        # Make the API request
        response = requests.get(geocoding_url, params=params, timeout=5)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the JSON response
        data = response.json()
        
        # Check if we got any results
        if "results" in data and len(data["results"]) > 0:
            result = data["results"][0]
            latitude = result["latitude"]
            longitude = result["longitude"]
            country = result["country"]
            return latitude, longitude, country
        else:
            return None
            
    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out. Please check your internet connection.")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Error: Unable to connect to the server. Please check your internet connection.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return None
    except (KeyError, json.JSONDecodeError):
        print("❌ Error: Unable to parse the response from the server.")
        return None


def get_current_weather(latitude, longitude):
    """
    Fetch current weather information from Open-Meteo Forecast API.
    
    Args:
        latitude (float): Latitude of the location
        longitude (float): Longitude of the location
    
    Returns:
        dict: Weather data if successful, None if error occurs
    """
    try:
        # Build the API URL for weather forecast
        forecast_url = "https://api.open-meteo.com/v1/forecast"
        
        # Parameters for the forecast API
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,weather_code",  # Get temperature and weather code
            "timezone": "auto"  # Automatically detect timezone
        }
        
        # Make the API request
        response = requests.get(forecast_url, params=params, timeout=5)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse and return the JSON response
        return response.json()
        
    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out. Please check your internet connection.")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Error: Unable to connect to the server. Please check your internet connection.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return None
    except json.JSONDecodeError:
        print("❌ Error: Unable to parse the weather data.")
        return None


def convert_weather_code(weather_code):
    """
    Convert WMO Weather interpretation code to human-readable text.
    
    Args:
        weather_code (int): Weather code from Open-Meteo API
    
    Returns:
        str: Human-readable weather description
    """
    # Dictionary to map weather codes to descriptions
    weather_descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Foggy",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Heavy drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }
    
    # Return the description, or "Unknown" if code not found
    return weather_descriptions.get(weather_code, "Unknown weather condition")


def main():
    """Main function - orchestrates the weather fetching program."""
    print("=" * 50)
    print("    Welcome to Live Weather Fetcher!")
    print("=" * 50)
    print()
    
    # Ask user for city name
    city_name = input("Enter a city name: ").strip()
    
    # Check if user entered something
    if not city_name:
        print("❌ Error: Please enter a city name.")
        return
    
    print("\n🔍 Searching for city coordinates...")
    
    # Get coordinates for the city
    coordinates = get_city_coordinates(city_name)
    
    if coordinates is None:
        print(f"❌ Error: City '{city_name}' not found. Please check the spelling and try again.")
        return
    
    latitude, longitude, country = coordinates
    
    print("✓ City found!")
    print("\n☁️  Fetching weather data...")
    
    # Get the weather data
    weather_data = get_current_weather(latitude, longitude)
    
    if weather_data is None:
        print("❌ Error: Unable to fetch weather data.")
        return
    
    # Extract relevant information from the response
    current_weather = weather_data["current"]
    temperature = current_weather["temperature_2m"]
    weather_code = current_weather["weather_code"]
    weather_condition = convert_weather_code(weather_code)
    
    # Display the weather information
    print("\n" + "=" * 50)
    print("           WEATHER INFORMATION")
    print("=" * 50)
    print(f"City:              {city_name}")
    print(f"Country:           {country}")
    print(f"Temperature:       {temperature}°C")
    print(f"Condition:         {weather_condition}")
    print("=" * 50)
    print()


if __name__ == "__main__":
    main()
