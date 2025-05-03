from src.interface.weather_station import AWeatherStation



class WeatherPublisher(AWeatherStation):
    """ Основной класс - издатель """

    def __init__(self, facade):
        super().__init__(facade)


    def add_subscriber(self, subscriber) -> None:
        """
        Добавляет подписчика в список
        :param subscriber: принимает подписчика
        :return: None
        """
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)


    def remove_subscriber(self, subscriber) -> None:
        """
        Удаляет подписчика из списка
        :param subscriber: принимает подписчика
        :return: None
        """
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)


    def notification(self) -> None:
        """
        Уведомляет подписчиков об обновлении данных
        :return: None
        """
        for subscriber, weather_object in zip(self._subscribers, self._facade.weather_objects):
            subscriber.update_data(weather_object)


    @property
    def subscribers(self) -> list:
        """
        Возвращает список подписчиков
        :return: list[subscriber]
        """
        return self._subscribers


    @property
    def count(self) -> list:
        """
        Возвращает список объектов
        :return: list[Weather]
        """
        return self._facade.weather_objects


