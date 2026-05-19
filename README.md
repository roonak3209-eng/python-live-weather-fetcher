# Live Weather Fetcher

## Description

Live Weather Fetcher is a beginner-friendly Python application that fetches and displays current weather information for any city in the world. The program uses the Open-Meteo API to get coordinates and weather data, making it a great way to learn about API calls, JSON parsing, and error handling in Python.

## Technologies Used

- **Python 3.11** - Programming language
- **requests library** - For making HTTP API calls
- **Open-Meteo API** - Free weather and geocoding API (no API key required!)
- **JSON** - For parsing API responses

## How to Run

### Step 1: Install the Required Library
```bash
pip install -r requirements.txt
```

### Step 2: Run the Program
```bash
python main.py
```

### Step 3: Enter a City Name
When prompted, type any city name (e.g., "London", "New York", "Tokyo") and press Enter.

## What I Learned

This project teaches several important programming concepts:

- **API Calls** - How to make HTTP requests to external services using the `requests` library
- **requests Library** - Different HTTP methods, parameters, and error handling
- **JSON Parsing** - Extracting data from JSON responses
- **Error Handling** - Gracefully handling network errors, timeouts, and invalid input
- **Functions** - Writing reusable, well-documented functions with docstrings
- **Web Standards** - Understanding WMO Weather codes and API conventions

## Sample Terminal Output

```
==================================================
    Welcome to Live Weather Fetcher!
==================================================

Enter a city name: London

🔍 Searching for city coordinates...
✓ City found!

☁️  Fetching weather data...

==================================================
           WEATHER INFORMATION
==================================================
City:              London
Country:           United Kingdom
Temperature:       15°C
Condition:         Partly cloudy
==================================================
```

## Features

- 🌍 Search weather for any city worldwide
- 🌡️ Get current temperature in Celsius
- ☁️ Detailed weather condition descriptions
- 🛡️ Robust error handling for invalid cities and network issues
- 📚 Beginner-friendly, well-commented code
- ✅ No API key required!

## Project Structure

```
python-live-weather-fetcher/
├── main.py              # Main program script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## API Information

This project uses the **Open-Meteo API**, a free, open-source weather API with no authentication required.

- **Geocoding API** - Converts city names to coordinates
  - URL: `https://geocoding-api.open-meteo.com/v1/search`
  
- **Forecast API** - Provides weather information
  - URL: `https://api.open-meteo.com/v1/forecast`

## Future Improvements

- Add forecast for multiple days
- Display weather in Fahrenheit as an option
- Add more weather details (humidity, wind speed, etc.)
- Create a GUI version with tkinter
- Save favorite cities to a local file

## Notes

- Internet connection is required to fetch weather data
- Temperature is displayed in Celsius
- Weather data updates in real-time from the API

Enjoy exploring the weather! 🌤️
