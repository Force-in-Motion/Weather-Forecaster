from interface.service_db import AFacade
from service.model.weather import Weather
from service.operations.api_operations import RequestData as rd
from service.operations.db_operations import DBOperations
import time



class WeatherDataManager(AFacade):

    def __init__(self, api_key, city_list):
        super().__init__(api_key, city_list)
        self._db = DBOperations()
        self._list_weather_objects = [Weather(record) for record in self._db.get_records()]


    def _update_db(self):
        for city in self._city_list:
            result = rd.get_weather_data(self._api_key, city)

            existing_records = self._db.get_records()

            if any(record[0] == city for record in existing_records):
                self._db.update_record(city, *result[1:])

            else:
                self._db.add_record(*result)


    def update_list_weather_objects(self):
        if self._list_weather_objects:
            self._list_weather_objects.clear()

        records = self._db.get_records()
        for record in records:
            self._list_weather_objects.append(Weather(record))


    def automatically_updates_db(self):
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
                self._list_weather_objects = [Weather(record) for record in self._db.get_records()]

    @property
    def weather_objects(self):
        return self._list_weather_objects

