import json
import requests
import os
from datetime import datetime


def fetch_weather_data(city_coordinate):
    url = 'https://api.open-meteo.com/v1/forecast'

    params = {
        'latitude': city_coordinate['lat'],
        'longitude': city_coordinate['long'],
        'current': 'temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m',
        'daily': 'temperature_2m_max,temperature_2m_min',
        'timezone': 'auto'
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        print(f"\nWeather for {city_coordinate['name']}:")
        current = data.get('current', {})
        print(f"Temperature: {current.get('temperature_2m')}°C")
        print(f"Humidity: {current.get('relative_humidity_2m')}%")
        print(f"Feels like: {current.get('apparent_temperature')}°C")
        print(f"Wind Speed: {current.get('wind_speed_10m')} km/h")

        daily = data.get('daily', {})
        print('\nDaily Forecast:')
        print(f"Max Temp: {daily.get('temperature_2m_max')}")
        print(f"Min Temp: {daily.get('temperature_2m_min')}")

        return data

    except requests.RequestException as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None


def save_weather_data(weather_data, city_name):
    filename = 'weather.json'

    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
                if not isinstance(existing_data, list):
                    existing_data = [existing_data]
        except json.JSONDecodeError:
            existing_data = []
    else:
        existing_data = []

    weather_data['city_name'] = city_name
    weather_data['fetched_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    is_duplicate = False

    for entry in existing_data:
        if (entry.get('city_name') == weather_data['city_name'] and
                entry.get('current', {}).get('temperature_2m') == weather_data.get('current', {}).get('temperature_2m') and
                entry.get('current', {}).get('relative_humidity_2m') == weather_data.get('current', {}).get(
                    'relative_humidity_2m')):
            is_duplicate = True
            break

    if is_duplicate:
        print(f"\nDuplicate data found for {city_name}. Skipping save.")
    else:
        existing_data.append(weather_data)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)
        print(f"\nWeather data for {city_name} saved to {filename}")


def main():
    city_name = input("Enter your city name: ").strip()
    latitude = float(input("Enter latitude: ").strip())
    longitude = float(input("Enter longitude: ").strip())

    weather_data = fetch_weather_data({'name': city_name, 'lat': latitude, 'long': longitude})

    if weather_data:
        save_weather_data(weather_data, city_name)
    else:
        print("No data fetched.")


if __name__ == "__main__":
    main()
