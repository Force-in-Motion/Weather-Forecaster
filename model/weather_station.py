from interface.weather_station import AWeatherStation



class WeatherPublisher(AWeatherStation):

    def __init__(self, facade):
        super().__init__(facade)

    def add_subscriber(self, subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notification(self):
        for subscriber, weather_object in zip(self._subscribers, self._facade.weather_objects):
            subscriber.update_data(weather_object)


    def update(self):
        self._facade.update_list_weather_objects()
        self.notification()


    @property
    def subscribers(self):
        return self._subscribers

    @property
    def count(self):
        return self._facade.weather_objects


