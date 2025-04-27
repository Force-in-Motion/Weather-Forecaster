from abc import ABC, abstractmethod


class ASubscriber(ABC):

    @abstractmethod
    def update(self) -> None:
        pass

