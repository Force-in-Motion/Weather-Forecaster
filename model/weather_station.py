from config.cities import city_list
from interface.weather_station import AWeatherStation
from service.model.weather import Weather



class WeatherStation(AWeatherStation):

    def __init__(self):
        super().__init__()
        self.__list_weather_objects: list[Weather] = []
        self.__update_list_weather_objects()


    def __update_list_weather_objects(self):
        self.__list_weather_objects.clear()

        for city in city_list:
            self.__list_weather_objects.append(Weather(city))


    def add_subscriber(self, subscribers) -> None:
        self._subscribers.append(subscribers)


    def remove_subscriber(self, subscribers) -> None:
        self._subscribers.remove(subscribers)


    def notification(self) -> None:
        for index, subscriber in enumerate(self._subscribers):
            subscriber.update_data(self.__list_weather_objects[index])

    def update(self):
        self.__update_list_weather_objects()
        self.notification()


    @property
    def count(self):
        return self.__list_weather_objects
