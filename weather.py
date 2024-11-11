import requests

def get_weather(api_key, city):
    """Fetch the current weather for a specified city."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(weather_data):
    """Display the weather information."""
    city = weather_data['name']
    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {weather_description.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

def main():
    api_key = input("Enter your OpenWeatherMap API key: ")
    
    while True:
        city = input("\nEnter the city name (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Exiting the application.")
            break
        
        weather_data = get_weather(api_key, city)
        
        if weather_data:
            display_weather(weather_data)
        else:
            print("City not found. Please try again.")

if __name__ == "__main__":
    main()
