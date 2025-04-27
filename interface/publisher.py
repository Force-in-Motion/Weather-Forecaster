from abc import ABC, abstractmethod
from subscriber import ASubscriber


class APublisher(ABC):
    def __init__(self):
        self.__subscribers: list[ASubscriber]

    @abstractmethod
    def add_subscriber(self, subscriber: ASubscriber) -> None:
        pass


    @abstractmethod
    def remove_subscriber(self, subscriber: ASubscriber) -> None:
        pass


    @abstractmethod
    def notification(self) -> None:
        pass