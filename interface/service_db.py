from abc import ABC, abstractmethod



class AWeather(ABC):

    def __init__(self, record):
        self._record: tuple = record
        self._city: str | None = None
        self._current_temp: float | None = None
        self._humidity: float | None = None
        self._pressure: float | None = None
        self._wind_speed: float | None = None
        self._set_weather_data()

    @abstractmethod
    def _set_weather_data(self) -> None:
        pass

    @abstractmethod
    def current_temp(self) -> str:
        pass

    @abstractmethod
    def humidity(self) -> str:
        pass

    @abstractmethod
    def pressure(self) -> str:
        pass

    @abstractmethod
    def wind_speed(self) -> str:
        pass

    @abstractmethod
    def city(self) -> str:
        pass



class ADB(ABC):

    @abstractmethod
    def __init__(self):
        self._create_table()

    @abstractmethod
    def _create_table(self) -> None:
        pass

    @abstractmethod
    def add_record(self, *args) -> None:
        pass

    @abstractmethod
    def get_records(self) -> tuple[tuple[str], ...]:
        pass

    @abstractmethod
    def update_record(self, *args) -> bool:
        pass



class AFacade(ABC):

    @abstractmethod
    def __init__(self, api_key, city_list):
        self._api_key = api_key
        self._city_list = city_list
        self._list_weather_objects = []

    @abstractmethod
    def _update_db(self):
        pass

    @abstractmethod
    def update_list_weather_objects(self):
        pass

    @abstractmethod
    def automatically_updates_db(self):
        pass


    @abstractmethod
    def weather_objects(self):
        pass
