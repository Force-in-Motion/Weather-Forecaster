import json
import os
import sqlite3
import threading
from src.config.variables import *


class FileLoader:
    """ Класс, содержащий служебные методы получения пути и доступа к данным """

    @staticmethod
    def get_path(dots: str, name_directory: str, name_module: str) -> str:
        """
        Создает относительный путь к файлу
        :return: Путь в виде строки
        """
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, dots, name_directory, name_module)

        return os.path.abspath(path)


    @staticmethod
    def get_data() -> str:
        """
        Получает токен по указанному пути
        :return: Токен в виде строки
        """
        with open(FileLoader.get_path(DOTS, CONFIG, API), 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['api_key']



class DBConnector:

    @staticmethod
    def connect(query: str, params: tuple = ()):
        """
        Выполняет SQL-запрос с параметрами (если есть) и возвращает курсор.

        :param query: SQL-запрос в виде строки
        :param params: кортеж параметров для запроса (по умолчанию пустой)
        :return: sqlite3.Cursor
        """
        conn = sqlite3.connect(FileLoader.get_path(DOTS, STORAGE, DB))
        cursor = conn.cursor()

        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor, conn
        except Exception as e:
            raise RuntimeError(f"Ошибка при выполнении запроса: {e}")



class UpdateThreadLauncher:
    
    @staticmethod
    def loader(updates_db) -> bool:
        """
        В потоке запускает метод обновления базы данных
        :param updates_db:
        :return:
        """
        try:
            threading.Thread(target=updates_db, daemon=True).start()
            return True

        except Exception as e:
            print(f"Ошибка при запуске потока: {e}")
            return False
