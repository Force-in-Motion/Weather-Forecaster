from abc import ABC, abstractmethod


class AWeatherStation(ABC):
    def __init__(self, facade):
        self._facade = facade
        self._subscribers: list = []

    @abstractmethod
    def add_subscriber(self, subscriber) -> None:
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber) -> None:
        pass

    @abstractmethod
    def notification(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass