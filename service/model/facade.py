from interface.service_db import AFacade
from service.model.weather import Weather
from service.operations.api_operations import RequestData as rd
import time



class WeatherDataService(AFacade):
    """ Ключевой объект жизненного цикла и обновления сервиса базы данных и списка объектов Weather """

    def __init__(self, api_key, city_list, db_service):
        super().__init__(api_key, city_list, db_service)
        self._list_weather_objects = [Weather(record) for record in self._db_service.get_records()]


    def _update_db(self) -> None:
        """
        Обновляет данные в базе или дописывает недостающие
        :return: None
        """
        existing_records = self._db_service.get_records()

        for city in self._city_list:

            result = rd.get_weather_data(self._api_key, city)

            if any(record[0] == city for record in existing_records):
                self._db_service.update_record(*result[1:], result[0])

            else:
                self._db_service.add_record(*result)


    def automatically_updates_db(self) -> None | Exception:
        """
        Запускает главный жизненный цикл сервиса
        :return: None
        """
        last_db_update = 0

        while True:
            current_time = time.time()
            if current_time - last_db_update >= 7:
                try:
                    self._update_db()
                    print(f"База данных обновлена: {time.strftime('%Y-%m-%d %H:%M:%S')}")
                except Exception as e:
                    print(f"Ошибка обновления базы данных: {e}")
                last_db_update = current_time

                self._list_weather_objects = [Weather(record) for record in self._db_service.get_records()]


    @property
    def weather_objects(self) -> list:
        """
        Возвращает список объектов Weather
        :return: list[Weather]
        """
        return self._list_weather_objects

