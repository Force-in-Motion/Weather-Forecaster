
import requests


class RequestData:

    @staticmethod
    def get_data_from_server(api_key, city):
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve weather data: {response.status_code} {response.text}")

    @staticmethod
    def get_weather_data(api_key, city):

        response = RequestData.get_data_from_server(api_key, city)

        city = response.get('location', {}).get('name')

        current_temp = response.get('current', {}).get('temp_c')

        humidity = response.get('current', {}).get('humidity')

        pressure = response.get('current', {}).get('pressure_mb')

        wind_speed = response.get('current', {}).get('wind_kph')

        return city, current_temp, humidity, pressure, wind_speed

