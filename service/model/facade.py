
from config.cities import city_list
from interface.service_db import AFacade
from service.model.weather import Weather
from service.operations.api_operations import RequestData as rd
from service.operations.db_operations import DBOperations


import time
import asyncio

class WeatherDataManager(AFacade):

    def __init__(self, api_key, city_list):
        super().__init__(api_key, city_list)
        self._db = DBOperations()
        self._list_weather_objects = []
        self.__data = self._db.get_records()


    def _update_db(self):
        if self.__data:
            self._db.delete_records()

        for city in self._city_list:
            result = rd.get_weather_data(self._api_key, city)
            self._db.add_record(*result)

    def _update_list_weather_objects(self):
        self._list_weather_objects.clear()

        records = self._db.get_records()
        print(records)
        for record in records:
            self._list_weather_objects.append(Weather(record))

    async def _automatically_updates_db(self):
        last_db_update = 0
        while True:
            current_time = time.time()
            if current_time - last_db_update >= 360:
                try:
                    self._update_db()
                    print(f"DB updated at {time.strftime('%Y-%m-%d %H:%M:%S')}")
                except Exception as e:
                    print(f"Error updating DB: {e}")
                last_db_update = current_time
            await asyncio.sleep(1)

    async def _automatically_updates_list_weather_objects(self):
        last_list_update = 0

        while True:

            current_time = time.time()
            if current_time - last_list_update >= 360:
                try:
                    self._update_list_weather_objects()
                    print(f"Weather objects list updated at {time.strftime('%Y-%m-%d %H:%M:%S')}")
                except Exception as e:
                    print(f"Error updating weather objects list: {e}")
                last_list_update = current_time
            await asyncio.sleep(1)

    async def run_auto_updates(self):
        await asyncio.gather(
            self._automatically_updates_db(),
            self._automatically_updates_list_weather_objects()
        )
    @property
    def weather_objects(self):
        return self._list_weather_objects


a = WeatherDataManager("9fea0be2d914488e824173555251904", city_list)
asyncio.run(a.run_auto_updates())
print(a.weather_objects)
print(a.weather_objects)
print(a.weather_objects)
print(a.weather_objects)