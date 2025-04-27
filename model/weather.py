from config.weather_token import api_key
from tools.processing import ProcessingData as pd
from tools.request import get_data_from_server


class Weather:
    def __init__(self, city):
        self.__city: str = city
        self.__current_temp: str | None = None
        self.__humidity: str | None = None
        self.__pressure: str | None = None
        self.__wind_speed: str | None = None
        self.__set_weather_data()

    def __set_weather_data(self):
        try:

            weather_data = get_data_from_server(api_key, self.__city)

            self.__current_temp = weather_data['current']['temp_c']

            self.__humidity = weather_data['current']['humidity']

            self.__pressure = pd.converts_to_bars(weather_data['current']['pressure_mb'])

            self.__wind_speed = pd.converts_wind_speed_in_mps(weather_data['current']['wind_kph'])

        except Exception as e:
            print(e)

    @property
    def current_temp(self):
        return self.__current_temp

    @property
    def humidity(self):
        return self.__humidity

    @property
    def pressure(self):
        return self.__pressure

    @property
    def wind_speed(self):
        return self.__wind_speed
