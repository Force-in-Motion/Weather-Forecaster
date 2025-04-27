import requests


def get_data_from_server(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve weather data: {response.status_code} {response.text}")
