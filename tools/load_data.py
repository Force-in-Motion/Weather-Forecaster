import json
import os
import sqlite3
import threading
from config.variables import *


class LoadData:
    """ Класс, содержащий служебные методы получения пути и доступа к данным """

    @staticmethod
    def get_path(a: str, b: str, c: str) -> str:
        """
        Создает относительный путь к файлу
        :return: Путь в виде строки
        """
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, a, b, c)

        return os.path.abspath(path)


    @staticmethod
    def get_data() -> str:
        """
        Получает токен по указанному пути
        :return: Токен в виде строки
        """
        with open(LoadData.get_path(DOTS, CONFIG, API), 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['api_key']


    @staticmethod
    def connect(query: str, params: tuple = ()):
        """
        Выполняет SQL-запрос с параметрами (если есть) и возвращает курсор.

        :param query: SQL-запрос в виде строки
        :param params: кортеж параметров для запроса (по умолчанию пустой)
        :return: sqlite3.Cursor
        """
        conn = sqlite3.connect(LoadData.get_path(DOTS, STORAGE, DB))
        cursor = conn.cursor()

        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor, conn
        except Exception as e:
            raise RuntimeError(f"Ошибка при выполнении запроса: {e}")


    @staticmethod
    def loader(updates_db) -> None:
        """
        В потоке запускает метод обновления базы данных
        :param updates_db:
        :return:
        """
        threading.Thread(target=updates_db, daemon=True).start()
