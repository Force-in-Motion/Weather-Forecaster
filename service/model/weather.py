from interface.service_db import AWeather
from tools.converter import Converter as c



class Weather(AWeather):
    """ Основная сущность приложения, содержащая все данные о погоде в конкретном городе """

    def __init__(self, record):
        super().__init__(record)


    def _set_weather_data(self) -> None:
        """
        Заполняет описание объекта данными, полученными из внешнего ресурса при помощи инструментов
        :return: None
        """
        self._city = self._record[0]

        self._current_temp = self._record[1]

        self._humidity = self._record[2]

        self._pressure = c.converts_pressure_in_mm_hg(self._record[3])

        self._wind_speed = c.converts_wind_speed_in_mps(self._record[4])


    @property
    def current_temp(self) -> float:
        """
        :return: Возвращает текущую температуру, для конкретного города
        """
        return self._current_temp


    @property
    def humidity(self) -> float:
        """
         :return: Возвращает текущую влажность, для конкретного города
         """
        return self._humidity


    @property
    def pressure(self) -> float:
        """
         :return: Возвращает текущее атмосферное давление, для конкретного города
         """
        return self._pressure


    @property
    def wind_speed(self) -> float:
        """
         :return: Возвращает текущую скорость ветра, для конкретного города
         """
        return self._wind_speed


    @property
    def city(self) -> str:
        """
         :return: Возвращает название города
         """
        return self._city
